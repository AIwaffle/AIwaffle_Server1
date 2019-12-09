import json
import logging
import socketserver

import numpy as np

import server1_extra.model as model


class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        """
        Handles one request
        """
        data = self.rfile.readline().strip()
        self.server.logger.debug("Data received: {}".format(data))
        res = self.from_user_input(data.decode())
        self.wfile.write(res.encode())
        self.server.logger.debug("Data sent: {}".format(res))

    def from_user_input(self, data: str) -> str:
        assert isinstance(self.server.model, Model)
        args, kw = json.loads(data)
        print(args, kw)
        if len(args) == 0:
            return ""
        if args[0] == "model":
            return json.dumps([list(self.server.model.W), [self.server.model.b]])
        elif args[0] == "params":
            if "learning_rate" in kw:
                self.server.model.learningRate = float(kw["learning_rate"])
            return json.dumps(self.server.model.learningRate)
        elif args[0] == "forward":
            if "X" not in kw:
                return ""
            x = np.array(kw["X"])
            return json.dumps(self.server.model.forward(x))
        elif args[0] == "backward":
            self.server.model.backward()
            return json.dumps(self.server.model.A)
        elif args[0] == "output":
            return json.dumps(self.server.model.A)
        elif args[0] == "optimize":
            self.server.model.optimize()
            return ""


class Server(socketserver.UnixStreamServer):

    def server_activate(self):
        """
        Initializes the server
        """
        self.logger = logging.getLogger("server1_model1")
        self.model = model.Model()
        self.logger.debug("Activated server")
        super(Server, self).server_activate()
