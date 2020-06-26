# API Authentication Documentation

## Register
POST ```/api/auth/register```

Json data:

Name | Format | Description
-----|--------|------------
username | str | The username
password | str | The password

Json Response:

Name | Format | Description
-----|--------|------------
success | bool | Whether the registration is success
reason | str | Why the operation fails (when not success)
uuid | str | The uuid of the registered user

## Login

POST ```/api/auth/login```

Json data:

Name | Format | Description
-----|--------|------------
username | str | The username
password | str | The password
session | int | Whether to store the login in session, 1 for store

Json response:

Name | Format | Description
-----|--------|------------
success | bool | Whether the registration is success
reason | str | Why the operation fails (when not success)

Status code:

Status | Description
-------|------------
200 | OK
501 | The non-session login is not implemented yet (when `session` != 1)
