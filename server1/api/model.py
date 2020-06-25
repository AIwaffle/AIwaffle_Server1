import json
import os
import socket

from flask import current_app

from server1_extra.server import ModelFactory

# Helper variable to store the models
# This variable is only used when config["USE_EXTRA_SERVER"] is False
MODEL_FACTORY = None
LOGGER = None


def model(*args, **kw):
    data = json.dumps((args, kw))
    if current_app.config["USE_EXTRA_SERVER"]:
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
    global LOGGER
    if MODEL_FACTORY is None:
        if LOGGER is None:
            LOGGER = current_app.logger
        LOGGER.info("Created server1_extra instance")
        # Model logs will be recorded into server1_extra.log
        MODEL_FACTORY = ModelFactory(logger=LOGGER)

    return json.loads(MODEL_FACTORY.parse(data))
