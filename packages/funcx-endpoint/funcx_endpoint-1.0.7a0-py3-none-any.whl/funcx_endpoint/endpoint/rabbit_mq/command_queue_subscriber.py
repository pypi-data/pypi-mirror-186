from __future__ import annotations

import logging
import os
import queue
import random
import threading
import time
import typing as t

import pika

if t.TYPE_CHECKING:
    # import pika.exceptions
    from pika.channel import Channel
    from pika.frame import Method
    from pika.spec import Basic, BasicProperties

log = logging.getLogger(__name__)


class CommandQueueSubscriber(threading.Thread):
    def __init__(
        self,
        *,
        queue_info: dict,
        command_queue: queue.SimpleQueue[tuple[int, BasicProperties, bytes]],
        stop_event: threading.Event,
        poll_period_s=0.5,
        connect_attempt_limit = 3,
        channel_close_window_s=10,
        channel_close_window_limit=3,
    ):
        """

        Parameters
        ----------
        queue_info - A structure containing the AMQP connection credentials
        command_queue - Messages from upstream will be placed in this queue; consumers
        of this queue must call .to_ack() with the message id when finished processing
        stop_event - If set, shutdown and stop thread; will be set regardless at thread end.
        poll_period_s - How often to perform housekeeping tasks (ACKing messages upstream,
        connect_attempt_limit
        channel_close_window_s
        channel_close_window_limit
        """
        super().__init__()

        self.queue_info = queue_info
        self._command_queue = command_queue
        self._stop_event = stop_event
        self._to_ack: queue.SimpleQueue[int] = queue.SimpleQueue()
        self._channel_closed = threading.Event()

        self._connection: pika.SelectConnection | None = None
        self._channel: Channel | None = None
        self._consumer_tag: str | None = None
        
        # how many times to attempt connection before giving up and shutting
        # down the thread
        self.connect_attempt_limit = connect_attempt_limit
        self._connection_tries = 0  # count of connection events; reset on success

        # list of times that channel was last closed
        self._channel_closes: list[float] = []

        # how long a time frame to keep previous channel close times
        self.channel_close_window_s = channel_close_window_s

        # how many times allowed to retry opening a channel in the above time
        # window before giving up and shutting down the thread
        self.channel_close_window_limit = channel_close_window_limit

        self._poll_period_s = poll_period_s

    def __repr__(self):
        return "{}<{}; pid={}>".format(
            self.__class__.__name__,
            "✓" if self._consumer_tag else "✗",
            os.getpid(),
        )

    def run(self):
        log.debug("%s AMQP thread begins", self)
        idle_for_s = 0.0
        while self._connection_tries < self.connect_attempt_limit and not self._stop_event.is_set():
            if self._connection or self._connection_tries:
                idle_for_s = random.uniform(0.5, 10)
                msg = f"%s AMQP reconnecting in {idle_for_s:.1f}s."
                log.debug(msg, self)
                if self._connection_tries == self.connect_attempt_limit - 1:
                    log.warning(f"{msg}  (final attempt)", self)

            if self._stop_event.wait(idle_for_s):
                break

            self._connection_tries += 1
            try:
                log.debug(
                    "%s Opening connection to AMQP service.  Attempt: %s (of %s)",
                    self,
                    self._connection_tries,
                    self.connect_attempt_limit,
                )
                self._connection = self._connect()
                self._event_watcher()
                self._connection.ioloop.start()
            except Exception:
                log.exception("%s Unhandled exception: shutting down connection.", self)
        self._stop_event.set()
        log.debug("%s Shutdown complete", self)

    def _connect(self) -> pika.SelectConnection:
        pika_params = pika.URLParameters(self.queue_info["connection_url"])
        return pika.SelectConnection(
            pika_params,
            on_close_callback=self._on_connection_closed,
            on_open_error_callback=self._on_open_failed,
            on_open_callback=self._on_connection_open,
        )

    def _on_open_failed(self, _mq_conn: pika.BaseConnection, exc: str | Exception):
        assert self._connection is not None, "Strictly called *by ioloop*"
        count = f"[attempt {self._connection_tries} (of {self.connect_attempt_limit})]"
        pid = f"(pid: {os.getpid()})"
        exc_text = f"Failed to open connection - ({exc.__class__.__name__}) {exc}"
        msg = f"{count} {pid} {exc_text}"
        log.debug("%s %s", self, msg)

        if not (self._connection_tries < self.connect_attempt_limit):
            self._stop_event.set()
            log.warning("%s %s", self, msg)
        self._connection.ioloop.stop()

    def _on_connection_closed(self, _mq_conn: pika.BaseConnection, exc: Exception):
        assert self._connection is not None, "Strictly called *by ioloop*"
        log.debug("%s Connection closed: %s", self, exc)
        self._consumer_tag = None
        self._connection.ioloop.stop()

    def _on_connection_open(self, _mq_conn: pika.BaseConnection):
        log.debug("%s Connection established; creating channel", self)
        self._open_channel()

    def _open_channel(self):
        if self._connection.is_open:
            self._connection.channel(on_open_callback=self._on_channel_open)

    def _on_channel_open(self, mq_chan: Channel):
        self._channel = mq_chan

        mq_chan.add_on_close_callback(self._on_channel_closed)
        mq_chan.add_on_cancel_callback(self._on_consumer_cancelled)

        log.debug(
            "%s Channel %s opened (%s)",
            self,
            mq_chan.channel_number,
            mq_chan.connection.params,
        )
        self._start_consuming()

    def _on_channel_closed(self, mq_chan: Channel, exc: Exception):
        self._consumer_tag = None
        assert self._connection is not None, "Strictly called _by_ ioloop"
        now = time.monotonic()
        then = now - self.channel_close_window_s
        self._channel_closes = [cc for cc in self._channel_closes if cc > then]
        self._channel_closes.append(now)
        if len(self._channel_closes) < self.channel_close_window_limit:
            if self._stop_event.is_set():
                return
            msg = f"{self} Channel closed  [{mq_chan}\n  ({exc})]"
            log.debug(msg, exc_info=exc)
            log.warning(msg)
            self._connection.ioloop.call_later(1, self._open_channel)

        else:
            msg = (
                f"Unable to sustain channel after {len(self._channel_closes)} attempts"
                f" in {self.channel_close_window_limit} seconds. ({exc})"
            )
            log.error(f"%s %s", self, msg)
            self._stop_event.set()

    def _on_consumer_cancelled(self, frame: Method[Basic.CancelOk]):
        log.debug("%s Consumer cancelled remotely, shutting down: %r", self, frame)
        if self._channel:
            self._channel.close()

    def _start_consuming(self):
        try:
            self._consumer_tag = self._channel.basic_consume(
                queue=self.queue_info["queue"],
                on_message_callback=self._on_message,
            )
            self._connected_at = time.time()
        except ValueError as e:
            log.warning("%s Unable to start consuming messages: %s", self, e)
            self._stop_ioloop()
        else:
            log.debug("%s Awaiting messages", self)

    def _on_message(
        self,
        mq_chan: Channel,
        basic_deliver: Basic.Deliver,
        properties: BasicProperties,
        body: bytes,
    ):
        # log.debug(
        #     "%s Received message from %s: %s, %s",
        #     self
        #     basic_deliver.delivery_tag,
        #     properties.app_id,
        #     body,
        # )

        try:
            self._command_queue.put((basic_deliver.delivery_tag, properties, body))
        except Exception:
            # No sense in waiting for the RMQ default 30m timeout; let it know
            # *now* that this message failed.
            log.exception("%s Command queue put failed", self)
            mq_chan.basic_nack(basic_deliver.delivery_tag, requeue=True)

    def ack(self, msg_tag: int):
        self._to_ack.put(msg_tag)

    def _on_cancelok(self, _frame: Method[Basic.CancelOk]):
        self._close_channel()

    def _close_channel(self):
        log.debug("%s Closing the channel", self)
        self._channel.close()

    def _stop_ioloop(self):
        """
        Gracefully stop the ioloop.

        In an effort play nice with upstream, attempt to follow the AMQP protocol
        by closing the channel and connections gracefully.  This method will
        rearm itself while the connection is still open, continually working
        toward eventually and gracefully stopping the connection, before finally
        stopping the ioloop.
        """
        if self._connection:
            self._connection.ioloop.call_later(0.1, self._stop_ioloop)
            if self._connection.is_open:
                if self._channel:
                    if self._channel.is_open:
                        self._channel.close()
                    elif self._channel.is_closed:
                        self._channel = None
                else:
                    self._connection.close()
            elif self._connection.is_closed:
                self._connection.ioloop.stop()
                self._connection = None

    def _event_watcher(self):
        """Polls the stop_event periodically to trigger a shutdown"""
        if self._stop_event.is_set():
            log.debug("%s Shutting down per stop event", self)
            try:
                self._stop_ioloop()
            except Exception:
                log.exception("%s error while shutting down", self)
                raise
            return

        if self._connection_tries and self._consumer_tag:
            # we're connected ...
            if time.time() - self._connected_at > 60:
                # ... and connection stable for 60s; good to reset connection tries
                self._connection_tries = 0

        delivery_tags = []
        try:
            while True:
                delivery_tags.append(self._to_ack.get(block=False))
        except queue.Empty:
            pass
        if delivery_tags:
            delivery_tags.sort()  # nominally a no-op
            latest_msg_id = delivery_tags[-1]
            self._channel.basic_ack(latest_msg_id, multiple=True)
            log.debug("%s Acknowledged through message: %s", self, latest_msg_id)

        self._connection.ioloop.call_later(self._poll_period_s, self._event_watcher)
