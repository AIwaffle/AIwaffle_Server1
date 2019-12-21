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
        self.server.logger.debug("Data sent: {}".format(res))

    def parse(self, data: str) -> str:
        args, kw = json.loads(data)
        print(args, kw)
        if len(args) == 0:
            return ""
        command = args[0]
        session_id = kw["sid"]
        if command == "new":
            if session_id in self.server.models:
                return ""
            self.server.models[session_id] = model.Model([2, 4, 3])
            return ""
        if session_id not in self.server.models:
            self.server.logger.error("sid does not exist")
        if command == "forward":
            x = kw["X"]
            return json.dumps(self.server.models[session_id].forward(x))
        elif command == "backward":
            y = kw["Y"]
            return json.dumps(self.server.models[session_id].backward(y))
        elif command == "optimize":
            return json.dumps(self.server.models[session_id].optimize())
        elif command == "loss":
            y = kw["Y"]
            print(y)
            return json.dumps(self.server.models[session_id].loss(y))
        elif command == "data":
            return json.dumps(self.server.models[session_id].get_data())
        elif command == "iter":
            x = kw["X"]
            y = kw["Y"]
            return json.dumps(self.server.models[session_id].iter_(x, y))
        self.server.logger.error("Unknown command")


class Server(socketserver.UnixStreamServer):

    def server_activate(self):
        """
        Initializes the server
        """
        self.logger = logging.getLogger("server1_model1")
        self.models = dict()
        self.logger.debug("Activated server")
        super(Server, self).server_activate()
