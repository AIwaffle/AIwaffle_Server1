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

GET ```/auth/logout```

## Get current user

GET ```/auth/current```

Login is required

Response:

Name | Format | Description
-----|--------|------------
uuid | str | The uuid of the account
username | str | The username of the account
