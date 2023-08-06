from __future__ import annotations

import json
import logging
import os
import pathlib
import pprint
import pwd
import queue
import signal
import subprocess
import sys
import threading
import time
import typing as t
from datetime import datetime

import psutil
import setproctitle
from funcx import FuncXClient

from funcx_endpoint.endpoint.endpoint import Endpoint
from funcx_endpoint.endpoint.rabbit_mq.command_queue_subscriber import \
    CommandQueueSubscriber
from funcx_endpoint.endpoint.utils.config import Config
from funcx_endpoint import __version__


if t.TYPE_CHECKING:
    # import pika.exceptions
    # from pika.channel import Channel
    # from pika.frame import Method
    from pika.spec import BasicProperties


log = logging.getLogger(__name__)


_child_args: dict[int, tuple[str, str]] = {}

class InvalidCommandError(Exception): pass


class EndpointManager:
    def __init__(
        self,
        conf_dir: pathlib.Path,
        endpoint_uuid: str,
        config: Config,
    ):
        log.info("Endpoint Manager initialization")

        self._time_to_stop = False
        self._kill_event = threading.Event()

        self._wait_for_child = False

        self._command_queue: queue.SimpleQueue[
            tuple[int, BasicProperties, bytes]
        ] = queue.Queue()
        self._command_stop_event = threading.Event()
        funcx_client_options = {
            "funcx_service_address": config.funcx_service_address,
            "environment": config.environment,
        }

        fxc = FuncXClient(**funcx_client_options)
        endpoint_uuid = Endpoint.get_or_create_endpoint_uuid(conf_dir, endpoint_uuid)

        # * == "multi-tenant"; not important until it is, so let it be subtle
        ptitle = f"funcX Endpoint *({endpoint_uuid}, {conf_dir.name})"
        if config.environment:
            ptitle += f" - {config.environment}"
        ptitle += f" [{setproctitle.getproctitle()}]"
        setproctitle.setproctitle(ptitle)

        try:
            reg_info = fxc.register_endpoint(
                conf_dir.name,
                endpoint_uuid,
                endpoint_version=__version__,
                multi_tenant=True
            )
        except GlobusAPIError as e:
            if e.http_status == 409 or e.http_status == 423:
                # RESOURCE_CONFLICT or RESOURCE_LOCKED
                log.warning(f"Endpoint registration blocked.  [{e.message}]")
                exit(os.EX_UNAVAILABLE)
            raise
        except NetworkError as e:
            log.exception("Network error while registering multi-tenant endpoint")
            log.critical(f"Network failure; unable to register endpoint: {e}")
            exit(os.EX_TEMPFAIL)

        if reg_info.get("endpoint_id") != endpoint_uuid:
            log.error(
                "Unexpected response from server: mismatched endpoint id."
                f"\n  Expected: {endpoint_uuid}, found: {reg_info.get('endpoint_id')}"
            )
            exit(os.EX_SOFTWARE)

        try:
            cq_info = reg_info["command_queue_info"]
            cq_url, cq_queue = cq_info["connection_url"], cq_info["queue"]
        except Exception as e:
            log.debug("%s", reg_info)
            log.error(
                f"Invalid or unexpected registration data structure: (%s) %s",
                e.__class__.__name__,
                e,
            )
            exit(os.EX_DATAERR)

        self._command = CommandQueueSubscriber(
            queue_info={"connection_url": cq_url, "queue": cq_queue},
            command_queue=self._command_queue,
            stop_event=self._command_stop_event,
        )

        signal.signal(signal.SIGTERM, self.request_shutdown)
        signal.signal(signal.SIGINT, self.request_shutdown)
        signal.signal(signal.SIGQUIT, self.request_shutdown)

        signal.signal(signal.SIGCHLD, self.set_child_died)
        print("ADD MORE HANDLERS")

    def request_shutdown(self, sig_num, curr_stack_frame):
        self._time_to_stop = True

    def set_child_died(self, sig_num, curr_stack_fframe):
        self._wait_for_child = True

    def wait_for_children(self):
        try:
            self._wait_for_child = False
            wflags = os.WEXITED | os.WCONTINUED | os.WSTOPPED | os.WNOHANG
            siginfo = os.waitid(os.P_ALL, 0, wflags)
            while siginfo is not None:
                pid = siginfo.si_pid
                if os.WIFEXITED(siginfo.si_status):
                    *_, proc_args = _child_args.pop(pid, (None, None))
                    rc = os.WEXITSTATUS(siginfo.si_status)
                    if rc == 0 and proc_args:
                        log.info(f"User endpoint stopped normally ({pid}) [{proc_args}]")
                    elif rc:
                        if proc_args:
                            log.warning(f"User endpoint return code: {rc} ({pid}) [{proc_args}]")
                        else:
                            log.warning(f"Command return code: {rc} ({pid})")
                elif os.WIFSIGNALED(siginfo.si_status):
                    termsig = os.WTERMSIG(siginfo.si_status)
                    *_, proc_args = _child_args.pop(pid, (None, None))
                    if proc_args:
                        log.warning(
                            f"User endpoint terminated by signal: {termsig} ({pid}) [{proc_args}]"
                        )
                    else:
                        log.warning(f"Command terminated by signal: {termsig} ({pid})")
                siginfo = os.waitid(os.P_ALL, 0, wflags)

        except ChildProcessError:
            pass
        except Exception as e:
            log.exception(f"Failed to wait for a child process: {e}")

    # def
    def start(self):
        log.info("\n\n---------- Endpoint Manager begins ----------")

        try:
            self._event_loop()
        except Exception:
            log.exception("Unhandled exception; shutting down endpoint master")

        ptitle = f"[shutdown in progress] {setproctitle.getproctitle()}"
        setproctitle.setproctitle(ptitle)
        self._command_stop_event.set()
        self._kill_event.set()

        os.killpg(os.getpgid(0), signal.SIGTERM)

        proc_uid, proc_gid = os.getuid(), os.getgid()
        for msg_prefix, signum in (
            ("Signaling shutdown", signal.SIGTERM), ("Forcibly killing", signal.SIGKILL)
        ):
            for pid, (local_user, proc_args) in list(_child_args.items()):
                log.info(f"{msg_prefix} of user endpoint ({pid}) [{proc_args}]")
                try:
                    pw_rec = pwd.getpwnam(local_user)
                    uid, gid = pw_rec.pw_uid, pw_rec.pw_gid
                    os.setresgid(pw_rec.pw_gid, pw_rec.pw_gid, -1)
                    os.setresuid(pw_rec.pw_uid, pw_rec.pw_uid, -1)
                    os.killpg(os.getpgid(pid), signum)
                except Exception as e:
                    log.warning(
                        f"User endpoint signal failed: {e} ({pid}) [{proc_args}]"
                    )
                finally:
                    os.setresuid(proc_uid, proc_uid, -1)
                    os.setresgid(proc_gid, proc_gid, -1)

            deadline = time.time() + 10
            while _child_args and time.time() < deadline:
                time.sleep(0.5)
                self.wait_for_children()

        self._command.join(5)
        log.info("Shutdown complete.\n---------- Endpoint Manager ends ----------")

    def _event_loop(self, *args):
        self._command.start()

        max_skew_s = 180  # 3 minutes; ignore commands with out-of-date timestamp
        while not self._time_to_stop:
            if self._wait_for_child:
                self.wait_for_children()

            try:
                _command = self._command_queue.get(timeout=1.0)
                d_tag, props, body = _command
            except queue.Empty:
                if self._command_stop_event.is_set():
                    self._time_to_stop = True
                if sys.stdout.isatty():
                    print(f"\r{time.strftime('%c')}", end="", flush=True)
                continue

            try:
                server_cmd_ts = props.timestamp
                if props.content_type != "application/json":
                    raise ValueError("Invalid message type; expecting JSON")
                # log.debug(
                #     "\n  HEADERS (R): %s"
                #     "\n  HEADERS    : %s"
                #     "\n  CONTENT_TYPE    : %s"
                #     "\n  CONTENT_ENCODING: %s"
                #     "\n  TIMESTAMP: %s (%s)"
                #     "\n  PROPS    : %s",
                #     repr(props.headers),
                #     props.headers,
                #     props.content_type,
                #     props.content_encoding,
                #     props.timestamp,
                #     type(props.timestamp),
                #     props,
                # )

                msg = json.loads(body)
                command = msg.get("command")
                command_args = msg.get("args", [])
                command_kwargs = msg.get("kwargs", {})
                # log.debug("MESSAGE BODY: %s", str(msg))
            except Exception:
                log.exception("Unable to deserialize funcX services command")
                self._command.ack(d_tag)
                continue

            now = round(time.time())
            if abs(now - server_cmd_ts) > max_skew_s:
                server_pp_ts = datetime.fromtimestamp(server_cmd_ts).strftime("%c")
                endp_pp_ts = datetime.fromtimestamp(now).strftime("%c")
                log.warning(
                    "Ignoring command from server"
                    "\nCommand too old or skew between system clocks is too large."
                    f"\n  Command timestamp:  {server_cmd_ts:,} ({server_pp_ts})"
                    f"\n  Endpoint timestamp: {now:,} ({endp_pp_ts})"
                )
                self._command.ack(d_tag)
                continue

            local_user_lookup = {
                "kevin@globus.org": "kevin"
            }
            try:
                globus_uuid = msg.get("globus_uuid")
                globus_username = msg.get("globus_username")
                local_user = local_user_lookup[globus_username]

                # log.info(
                #     f"Requested to execute command: {command} ("
                #     f"args: {pprint.pformat(command_args)}, "
                #     f"kwargs: {pprint.pformat(command_kwargs)})"
                # )

                command_func = getattr(EndpointManager, command, None)
                if not command_func:
                    raise InvalidCommandError(f"Invalid command: {command}")
                command_func(local_user, command_args, command_kwargs)
                log.debug("Command successfully initiated.")
            except InvalidCommandError as err:
                log.error(str(err))

            except Exception:
                log.exception(
                    f"Unable to execute command: {command}\n"
                    f"    args: {command_args}\n"
                    f"  kwargs: {command_kwargs}"
                )

            self._command.ack(d_tag)

    @staticmethod
    def manage_endpoint(
        local_username: str, args: list[str | bytes] | None, kwargs: dict | None
    ):
        log.info("Launching ...")
        try:
            pid = os.fork()
        except Exception as err:
            print(f"Unable to fork child process: {err}")
            return

        if pid > 0:
            # Parent process branch
            return

        setproctitle.setproctitle("Endpoint starting up ...")

        if not args:
            log.warning(f"Invalid endpoint command: no arguments ({local_username})")
            exit(1)
        if not kwargs:
            kwargs = {}

        if args[0] in ("start", "restart"):
            log.warning(
                "Manage endpoint command may not (re)start an endpoint."
                f"  Use `start_endpoint`. ({local_username})"
            )
            exit(1)

        pw_rec = pwd.getpwnam(local_username)
        udir, uid, gid = pw_rec.pw_dir, pw_rec.pw_uid, pw_rec.pw_gid
        uname = pw_rec.pw_name

        proc_args = ["funcx-endpoint", *args]
        env = kwargs.get("env", {})
        env.update({"HOME": udir, "USER": uname})
        if not os.path.isdir(udir):
            udir = "/"

        wd = env.get("PWD", udir)

        try:
            # TODO: Get debugging information.  F.e.: if CWD is invalid ("/root"),
            # how to pass back permission error text?
            os.chdir("/")
            os.setpgrp()
            # TODO: Not done yet -- grave security error to not check error conditions
            # of setresgid() and setresuid()
            os.setresgid(gid, gid, gid)
            os.setresuid(uid, uid, uid)
            os.chdir(wd)
            env["PWD"] = wd
            env["CWD"] = wd
            os.execvpe(proc_args[0], args=proc_args, env=env)
        finally:
            exit(1)


    @staticmethod
    def start_endpoint(
        local_username: str, args: list[str] | None, kwargs: dict | None
    ):
        try:
            parent_pid = os.getpid()
            pid = os.fork()
        except Exception as err:
            log.error(f"Unable to fork child process: {err}")
            return

        if not args:
            args = []
        if not kwargs:
            kwargs = {}

        ep_name = kwargs.get("name", "")
        proc_args = ["funcx-endpoint", "start", ep_name, "--die-with-parent", *args]

        pw_rec = pwd.getpwnam(local_username)
        udir, uid, gid = pw_rec.pw_dir, pw_rec.pw_uid, pw_rec.pw_gid
        uname = pw_rec.pw_name

        if pid > 0:
            proc_args_s = f"({uname}, {ep_name}) {' '.join(proc_args)}"
            _child_args[pid] = (local_username, proc_args_s)
            log.info(f"Creating new user endpoint ({pid}) [{proc_args_s}]")
            return
        os.setsid()

        if not ep_name:
            exit(os.EX_DATAERR)

        try:
            env = kwargs.get("env", {})
            env.update({"HOME": udir, "USER": uname})
            if not os.path.isdir(udir):
                udir = "/"

            wd = env.get("PWD", udir)

            # TODO: Get debugging information.  e.g.: if CWD is invalid ("/root"),
            # how to pass back permission error text?

            os.chdir("/")  # always succeeds, so start from known place
            os.setresgid(gid, gid, gid)  # raises (good!) on error
            os.setresuid(uid, uid, uid)  # raises (good!) on error
            os.chdir(wd)
            env["PWD"] = wd
            env["CWD"] = wd

            startup_proc_title = f"Endpoint starting up ... ({uname}) {' '.join(proc_args)}"
            setproctitle.setproctitle(startup_proc_title)

            amqp_creds = json.dumps(kwargs.get("amqp_creds"))
            with open(os.devnull, 'w') as stdout:
                if os.dup2(stdout.fileno(), 1) != 1:
                    raise Exception(f"Unable to close stdout")
            with open(os.devnull, 'w') as stderr:
                if os.dup2(stderr.fileno(), 2) != 2:
                    raise Exception(f"Unable to close stderr")

            read_handle, write_handle = os.pipe()
            if os.dup2(read_handle, 0) != 0:  # close old stdin, use read_handle
                raise Exception(f"Unable to close stdin")
            os.close(read_handle)

            with os.fdopen(write_handle, "w") as cred_pipe:  # side-effect: close handle
                cred_pipe.write(amqp_creds)

            os.execvpe(proc_args[0], args=proc_args, env=env)
        except Exception as exc:
            log.warning(f"EXCEPTION: {exc} - refusing to exec for {uname}")
        finally:
            log.info("EXITING FAILURE ...")
            exit(1)
