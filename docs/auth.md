# Authentication Documentation
Session information is stored encrypted in cookies. 

## Register
POST ```/auth/register```

Form data:

Name | Format | Description
-----|--------|------------
username | str | The unique user name
password | str | The password of the account, will be hashed in backend

## Login

POST ```/auth/login```

Form data:

Name | Format | Description
-----|--------|------------
username | str | The unique user name
password | str | The password of the account

## Logout

POST ```/auth/logout```

## Get current user

GET ```/auth/current```

Response:

Name | Format | Description
-----|--------|------------
(None) | uuid | The uuid of the account