from server1.models import db, OAuth2AuthorizationCode, OAuth2Client, OAuth2Token


def get_clients(uuid: str) -> list:
    return OAuth2Client.query.filter(uuid == uuid).all()
