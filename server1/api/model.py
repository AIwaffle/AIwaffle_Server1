import json
import logging
import os
import socket

import flask

import server1_extra.server

# Helper variable to store the models
# This variable is only used when config["USE_EXTRA_SERVER"] is False
MODEL_FACTORY = None


def model(*args, **kw):
    data = json.dumps((args, kw))
    if flask.current_app.config["USE_EXTRA_SERVER"]:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.connect(os.path.join(os.curdir, 'instance', 'ext_sock'))
            rfile = sock.makefile("rb", -1)
            wfile = sock.makefile("wb", 1024)
            wfile.write(data.encode() + b'\n')
            wfile.flush()
            res = rfile.readline().strip()
            wfile.close()
            rfile.close()
            return json.loads(res)
    global MODEL_FACTORY
    if MODEL_FACTORY is None:
        logger = logging.getLogger("server1_extra")
        logger.info("Created server1_extra instance")
        MODEL_FACTORY = server1_extra.server.ModelFactory(logger)

    return json.loads(MODEL_FACTORY.parse(data))
