import numpy as np
import json
import logging
import socketserver

from AIwaffle.MLsource.LogisticRegressionModel.source import LogisticRegressionModel as Model


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

    def get_model_data(self) -> str:
        pass

    def from_user_input(self, data: str) -> str:
        data = json.loads(data)
        self.server.model.load_data(np.array([1, 2], 1))


class Server(socketserver.UnixStreamServer):

    def server_activate(self):
        """
        Initializes the server
        """
        self.logger = logging.getLogger("server1_model1")
        self.model = Model()
        self.logger.debug("Activated server")
        super(Server, self).server_activate()
