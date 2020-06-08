import json
import logging
import os
import socketserver
import uuid

import server1_extra.model as model


class ModelFactory:
    """A factory for multiple models
    """

    def __init__(self, logger: logging.Logger = logging.getLogger(__name__)):
        self.models = dict()
        self.logger = logger

    def parse(self, data: str) -> str:
        """Parser function

        Args:
            data (str): decoded str from the server
                should be a json dict

        Returns: a json string of a dict
            code: http status code for the server
            ...: behavior related to data
        """
        self.logger.debug("Started processing request")
        try:
            args, kw = json.loads(data)
        except json.JSONDecodeError as ex:
            self.logger.error("JSON decode error: possible caused by backend")
            self.logger.debug(ex)
            return json.dumps({"code": 500})
        if len(args) == 0:
            self.logger.error("Empty command: possibly caused by backend")
            return json.dumps({"code": 400})
        command = args[0]
        if command == "new":
            session_id = uuid.uuid4().__str__()
            self.models[session_id] = model.Model()
            self.logger.info("Created new model: {}".format(session_id))
            return json.dumps(dict(code=200, session_id=session_id))
        session_id = kw.get("session_id", None)
        if session_id not in self.models:
            self.logger.error("session_id does not exist: possibly caused by frontend")
            return json.dumps({"code": 404})
        if command == "iterate":
            learning_rate = float(kw.get("learning_rate", 0.01))
            epoch_num = int(kw.get("epoch_num", 1))
            res = self.models[session_id].iterate(learning_rate, epoch_num)
            res.update({"code": 200})
            self.logger.debug("Iterated model {} for {} epochs".format(session_id, epoch_num))
            return json.dumps(res)
        self.logger.error("Unknown command: possibly caused by backend")
        return json.dumps({"code": 500})


class Handler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        """Handles one request
        """
        data = self.rfile.readline().strip()
        # self.server.logger.debug("Data received: {}".format(data))
        res = self.parse(data.decode())
        self.wfile.write(res.encode())
        # self.server.logger.debug("Data sent: {}".format(res))

    def parse(self, data: str) -> str:
        return self.server.model_factory.parse(data)


class Server(socketserver.UnixStreamServer):

    def server_activate(self) -> None:
        """Initializes the server
        """
        if getattr(self, "logger", None) is None:
            self.logger = logging.getLogger(__name__)
        self.model_factory = ModelFactory(self.logger)
        self.logger.debug("Activated server")
        super(Server, self).server_activate()

    def handle_error(self, request, client_address):
        self.logger.error("Exception caught when processing request")
