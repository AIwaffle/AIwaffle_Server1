import uuid
import json
import logging
import socketserver

import server1_extra.model as model


class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        """
        Handles one request
        """
        data = self.rfile.readline().strip()
        self.server.logger.debug("Data received: {}".format(data))
        res = self.parse(data.decode())
        self.wfile.write(res.encode())
        # self.server.logger.debug("Data sent: {}".format(res))
        self.server.logger.debug("Data sent")

    def parse(self, data: str) -> str:
        args, kw = json.loads(data)
        if len(args) == 0:
            return ""
        command = args[0]
        if command == "new":
            session_id = uuid.uuid4().__str__()
            self.server.models[session_id] = model.Model()
            self.server.logger.debug("Created new model: {}".format(session_id))
            return json.dumps(dict(code=200, session_id=session_id))
        session_id = kw.get("session_id", None)
        if session_id not in self.server.models:
            self.server.logger.error("session_id does not exist")
            return json.dumps({"code": 404})
        if command == "iterate":
            learning_rate = float(kw.get("learning_rate", 0.01))
            epoch_num = int(kw.get("epoch_num", 1))
            res = self.server.models[session_id].iterate(learning_rate, epoch_num)
            res.update({"code": 200})
            return json.dumps(res)
        self.server.logger.error("Unknown command")
        return json.dumps({"code": 500})


class Server(socketserver.UnixStreamServer):

    def server_activate(self):
        """
        Initializes the server
        """
        self.logger = logging.getLogger(__name__)
        self.models = dict()
        self.logger.debug("Activated server")
        super(Server, self).server_activate()
