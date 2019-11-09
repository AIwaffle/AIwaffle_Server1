import click
import flask.cli
import sqlalchemy.ext.declarative
import sqlalchemy.orm

Base = sqlalchemy.ext.declarative.declarative_base()


def get_db():
    if "db" not in flask.g:
        flask.g.engine = sqlalchemy.create_engine(flask.current_app.config["SQLALCHEMY_DATABASE_URI"])
        flask.g.db = sqlalchemy.orm.scoped_session(
            sqlalchemy.orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=flask.g.engine
            )
        )
        Base.query = flask.g.db.query_property()
    return flask.g.db


def init_db():
    get_db()
    Base.metadata.create_all(bind=flask.g.engine)


@click.command("init-db")
@flask.cli.with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


def close_db(exception=None):
    db = flask.g.pop("db", None)
    if db is not None:
        db.remove()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
