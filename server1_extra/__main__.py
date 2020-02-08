import logging
import os

import server1_extra.server

if __name__ == "__main__":
    logger = logging.getLogger("server1_extra")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)
    fh = logging.FileHandler("server1_extra.log")
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    address = os.path.join(os.curdir, "instance", "ext_sock")

    if os.path.exists(address):
        os.remove(address)

    logger.info("Serving server1_extra on ./instance/ext_sock")
    try:
        with server1_extra.server.Server(address, server1_extra.server.Handler) as server:
            server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("Server closed")
        os.remove(address)
