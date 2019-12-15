import json
import logging
import socketserver

import server1_extra.model as model
import AIwaffle.MLsource.LogisticRegressionModel.DataGenerator as data_gen


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
            self.server.models[session_id] = model.Model(self.server.data)
        elif command == "forward":
            return json.dumps(self.server.models[session_id].forward())
        elif command == "backward":
            return json.dumps(self.server.models[session_id].backward())
        elif command == "loss":
            return json.dumps(self.server.models[session_id].loss())
        elif command == "evaluate":
            return json.dumps(self.server.models[session_id].evaluate())
        elif command == "data":
            return json.dumps(self.server.models[session_id].get_data())
        return ""


class Server(socketserver.UnixStreamServer):

    def server_activate(self):
        """
        Initializes the server
        """
        self.logger = logging.getLogger("server1_model1")
        self.data = data_gen.generate_data(100, 1, 0, noise=0.2)
        self.models = dict()
        self.logger.debug("Activated server")
        super(Server, self).server_activate()
