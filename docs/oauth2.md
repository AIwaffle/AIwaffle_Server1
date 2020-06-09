# OAuth2 Documentation

## Create a client

POST ```/oauth/create_client```

Login is required

Form data:

Name | Format | Description | Example
-----|--------|-------------|--------
client_name | str | The name of the client | Demo
client_uri | str | The link to the client | https://example.com/
grant_types | str | Type of grant to the client | authorization_code
redirect_uris | str | The callback uri of the client | https://example.com/redirect
response_types | str | The response | code
scope | str | Scope of data to be granted | profile
token_endpoint_auth_method | str | client_secret_basic

## Authorize a client

POST ```/oauth/authorize```

Login is required

Parameters are required

Form data:

Name | Format | Description | Example
-----|--------|-------------|--------
confirm | bool | Whether to confirm the grant | on 

## Issue a token

POST ```/oauth/authorize```

Refer to OAuth2 Documentation for details

## Revoke a token

POST ```/oauth/revoke```

Refer to OAuth2 Documentation for details

## Get the information of the authorized user

GET ```/oauth/api/me```

OAuth2 with scope profile is required
