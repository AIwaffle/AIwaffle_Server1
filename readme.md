# AIwaffle_server1

Version 0.1.10

![Python application](https://github.com/AIwaffle/AIwaffle_Server1/workflows/Python%20application/badge.svg?branch=dev)

Backend server for [AIwaffle](https://github.com/AIwaffle)


## Site map

 - **/** Index page
 - **/auth/** the user login/register pages
 - **/oauth/** the OAuth2 authorization
 - **/api/model/** the model APIs
 
## Documentation

Auth: [auth](/docs/auth.md)

OAuth2: [oauth2](/docs/oauth2.md)

Auth API: [api_auth](/docs/api_auth.md)

Model API: [model](/docs/model.md)

 
## Extra server

An internal server that runs a something unrelated to web (e.g.: computation)

Could be integrated to the web server

## Deploy

1. Clone this repo and initialize submodules
   ```shell script
   git clone https://github.com/AIwaffle/AIwaffle_Server1.git
   git submodule update --init
   ```
1. Install the project and dependencies
   ```shell script
   pip3 install -e .
   ```
1. Create instance directory
   ```shell script
   mkdir instance
   ```
1. Edit ```instance/config.py``` with the following contents
   ```python
   SECRET_KEY = "Your Secret Key"  # Require a random string or bytes
   SQLALCHEMY_DATABASE_URI = "sqlite://"  # Change if you want different databases
   USE_EXTRA_SERVER = True  # Whether you want to run a separate extra server
   ```
   1. Other approaches
   
      Edit ```app.py```
1. Run with uWSGI
   ```shell script
   uwsgi uwsgi.ini
   ```
   1. (Optional) Run the extra server if ```USE_EXTRA_SERVER=True```
   ```shell script
   python3 -m server1_extra
   ```
   1. (Optional): Configure uWSGI
   
      Edit ```uwsgi.ini```

## Upcoming Changes

### Version 0.1.11

 - [ ] Support logging configuration
 
## License and copyright

Licensed under the MIT license

Copyright 2019-2020

### Model

 - [jimmy-zx/AIwaffle](https://github.com/jimmy-zx/AIwaffle)


### Acknowledgements

 - [Flask](https://github.com/pallets/flask)
 - [example-oauth2-server](https://github.com/authlib/example-oauth2-server)
 - [AIwaffle/AIwaffle](https://github.com/AIwaffle/AIwaffle)
