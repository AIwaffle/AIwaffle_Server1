import logging
import os

import server1_extra.server

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)
    fh = logging.FileHandler(os.path.join(os.curdir, "instance", "server1_extra.log"))
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
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
