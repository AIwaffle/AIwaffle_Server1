import flask


def handle404(e):
    return flask.send_from_directory("../AIWaffle-website/dist", "index.html"), 200
