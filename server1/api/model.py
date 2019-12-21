import json
import os
import socket


def model(*args, **kw):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.connect(os.path.join(os.curdir, 'instance', 'ext_sock'))
        rfile = sock.makefile("rb", -1)
        wfile = sock.makefile("wb", 1024)
        data = json.dumps((args, kw))
        wfile.write(data.encode() + b'\n')
        wfile.flush()
        res = rfile.readline().strip()
        wfile.close()
        rfile.close()
        return res
