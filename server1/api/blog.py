import datetime

import server1.api.auth
import server1.db
import server1.models


def get_posts(db_session) -> list:
    posts = server1.models.Post.query.all()
    return posts


def get_post(c_id, db_session) -> server1.models.Post:
    post = server1.models.Post.query.filter(server1.models.Post.id == c_id).first()
    return post


def delete_post(c_id, db_session) -> bool:
    post = get_post(c_id, db_session)
    if post is None:
        return False
    db_session.delete(post)
    db_session.commit()
    return True


def create_post(c_uuid, title, body, db_session) -> bool:
    c_post = server1.models.Post(c_uuid, datetime.datetime.utcnow(), title, body)
    db_session.add(c_post)
    db_session.commit()
    return c_post.id
