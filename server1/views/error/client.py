import flask


def handle404(e):
    flask.current_app.logger.debug("Redirecting 404 request {} {}".format(flask.request.method, flask.request.url))
    return flask.send_from_directory("../AIWaffle-website/dist", "index.html"), 200
