"""Producer of messages submitted for the message broker."""
from __future__ import annotations

import base64
import json
import threading
from datetime import datetime
from itertools import count
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from deprogressapi import BaseReport
from websocket import WebSocket

from demessaging.messaging.connection import WebsocketConnection
from demessaging.PulsarMessageConstants import (
    MessageType,
    PropertyKeys,
    Status,
)

if TYPE_CHECKING:
    from demessaging.config import BaseMessagingConfig


class MessageProducer(WebsocketConnection):
    """Producer class to send requests to a registered backend module (topic)"""

    SOCKET_PING_INTERVAL = 5  # 1min

    def __init__(self, pulsar_config: BaseMessagingConfig):
        super().__init__(pulsar_config)
        self.subscription_name: str = (
            "python-backend-" + datetime.now().isoformat()
        )
        self.context_counter = count()

    def _socket_ping(
        self, sockets: List[WebSocket], timeout, event: threading.Event
    ):
        while not event.wait(timeout):
            for sock in sockets:
                if sock.connected:
                    try:
                        print("ping {}".format(datetime.now()))
                        sock.ping()
                    except Exception as e:
                        print("error in socket ping routine: {}".format(e))
                        break
                else:
                    print(
                        "quitting socket ping loop due to unconnected or missing socket"
                    )
                    break

    def start_ping_loop(self, sockets: List[WebSocket]):
        event = threading.Event()
        thread = threading.Thread(
            target=self._socket_ping,
            args=(sockets, MessageProducer.SOCKET_PING_INTERVAL, event),
        )
        thread.setDaemon(True)
        thread.start()

    async def send_request(
        self, request_msg, topic: Optional[str] = None
    ) -> Any:
        """Sends the given request to the backend module bound to the topic provided in the pulsar configuration.
        In order to increase re-usability the destination topic can be overridden with the optional topic argument.

        :param request_msg: dictionary providing a 'property' dictionary, a payload string, or both
        :param topic: overrides the used topic for this request
        :return: received response from the backend module
        """
        # establish connections
        out_topic = self.pulsar_config.topic
        # topic override if given
        if topic is not None:
            out_topic = topic
        out_socket: WebSocket = self.open_socket(
            topic=out_topic, header=self.pulsar_config.header
        )
        # To be thread safe, we generate the response topic here
        response_topic: str = self.generate_response_topic()
        in_socket: WebSocket = self.open_socket(
            subscription=self.subscription_name,
            topic=response_topic,
            header=self.pulsar_config.header,
        )

        self.start_ping_loop([in_socket, out_socket])

        try:
            # create message context (from counter)
            context = next(self.context_counter)
            request_msg["context"] = context
            if "properties" not in request_msg:
                request_msg["properties"] = {}
            request_msg["properties"][
                PropertyKeys.RESPONSE_TOPIC
            ] = response_topic
            request_msg["properties"][
                PropertyKeys.REQUEST_CONTEXT
            ] = request_msg["context"]
            request_msg["properties"][
                PropertyKeys.MESSAGE_TYPE
            ] = MessageType.REQUEST

            # send message via outgoing connection to request topic
            out_socket.send(json.dumps(request_msg))
            ack = out_socket.recv()
            ack = json.loads(ack)
            if "error" in ack["result"]:
                # error - return
                return {
                    "status": "error",
                    "error": "error sending the request",
                    "msg": ack,
                }

            # wait for response on response topic
            response = in_socket.recv()

            # parse json message
            response = json.loads(response)
            props = response["properties"]

            # acknowledge the response
            in_socket.send(json.dumps({"messageId": response["messageId"]}))

            # mapping from ids to existing reports
            reports: Dict[str, BaseReport] = {}

            while props[PropertyKeys.MESSAGE_TYPE] == MessageType.PROGRESS:
                # we received a progress report - print and ignore
                # decode progress data
                progress_data = base64.b64decode(response["payload"]).decode(
                    "utf-8"
                )

                report = BaseReport.from_payload(progress_data)
                if report.report_id in reports:
                    base_report = reports[report.report_id]
                    for field in report.__fields__:
                        setattr(base_report, field, getattr(report, field))
                else:
                    reports[report.report_id] = base_report = report
                if base_report.status != Status.RUNNING:
                    base_report.complete(base_report.status)
                else:
                    base_report.submit()

                # wait for next response
                response = in_socket.recv()

                # parse json message
                response = json.loads(response)
                props = response["properties"]

            # assert that we received a 'response' message and check for matching context
            if props[PropertyKeys.MESSAGE_TYPE] != MessageType.RESPONSE:
                return {
                    "status": "error",
                    "error": "received message is not a response to the sent request",
                    "msg": response,
                }

            if int(props[PropertyKeys.REQUEST_CONTEXT]) != int(context):
                return {
                    "status": "error",
                    "error": "received message belongs to a different request",
                    "msg": response,
                }

            if "payload" in response:
                status = "success"
                if "status" in props:
                    # we might successfully get a response, but it might contain an error from the backend
                    status = props["status"]

                # decode b64 payload msg
                payload: str = response["payload"]

                try:
                    payload = base64.b64decode(payload).decode("utf-8")
                except Exception as e:
                    status = "error"
                    payload = "error decoding payload: {0}".format(e)

                if status == "error":
                    return {
                        "status": "error",
                        "error": payload,
                        "msg": response,
                    }
                else:
                    return {"status": status, "msg": payload}
            else:
                return {
                    "status": "error",
                    "error": "missing response payload",
                    "msg": response,
                }
        finally:
            # close the sockets
            if out_socket:
                out_socket.close()
            if in_socket:
                in_socket.close()
