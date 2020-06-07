import json
import os
import urllib.parse

import authlib.oauth2.auth
import authlib.oauth2.client
import bs4
import requests.auth

os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'


def test_create_client(client, auth):
    auth.login()

    resp = client.get("/oauth/create_client")
    assert resp.status_code == 200

    # Create a client
    resp = client.post("/oauth/create_client", data={
        "client_name": "Hi",
        "client_uri": "https://example.com/",
        "scope": "profile",
        "redirect_uri": "https://example.com/redirect",
        "grant_type": "authorization_code\npassword",
        "response_type": "code",
        "token_endpoint_auth_method": "client_secret_basic",
    })
    assert resp.status_code == 302

    # Fetch client data
    resp = client.get("/oauth/")
    assert resp.status_code == 200
    soup = bs4.BeautifulSoup(resp.data, "html.parser")
    oauth_clients = soup.find_all("pre")
    assert len(oauth_clients) == 1
    oauth_client = oauth_clients[0]
    assert isinstance(oauth_client, bs4.element.Tag)
    client_data = json.loads(oauth_client.text.strip().split("\n")[0])

    client_id = client_data["client_id"]
    client_secret = client_data["client_secret"]
    scope = "profile"

    # Generate authorize url
    authlib_client = authlib.oauth2.OAuth2Client(
        None,
        client_id=client_id,
        client_secret=client_secret,
        scope=scope,
    )
    uri, state = authlib_client.create_authorization_url("/oauth/authorize")

    # Get authorize url
    resp = client.get(uri)
    assert resp.status_code == 200
    assert "profile" in resp.data.decode()

    # Authorize user
    resp = client.post(
        uri,
        headers={"Referer": uri},
        data={"confirm": "on"}
    )
    assert resp.status_code == 302

    # Authorize code
    authorization_response = resp.headers["Location"]
    parser = urllib.parse.urlparse(authorization_response)
    query = urllib.parse.parse_qs(parser.query)
    code = query.get("code")[0]
    params = {
        "redirect_uri": "https://example.com/redirect",
        "code": code,
        "grant_type": "authorization_code",
    }
    req = requests.Request(
        "POST",
        "https://example.com",
        auth=requests.auth.HTTPBasicAuth(client_id, client_secret),
    )
    headers = dict(req.prepare().headers)

    # Authorize Token
    resp = client.post(
        "/oauth/token",
        headers=headers,
        data=params,
    )
    token_data = json.loads(resp.data)
    token_type = token_data["token_type"]
    access_token = token_data["access_token"]

    # Get user information
    headers = {
        "Authorization": "{} {}".format(token_type, access_token),
    }
    resp = client.get(
        "/oauth/api/me",
        headers=headers,
    )
    user_data = json.loads(resp.data)

    assert user_data["username"] == "test_u1"
