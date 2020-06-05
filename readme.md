# AIwaffle_server1

Develop branch

Version 0.1.6

![Python application](https://github.com/AIwaffle/AIwaffle_Server1/workflows/Python%20application/badge.svg?branch=dev)

Backend server for [IDl0T/AIwaffle](https://github.com/IDl0T/AIwaffle)

## Components

### Web server

#### Network

Using Flask framework

#### Database

SQLAlchemy + SQLite

Models
 - Users: stores user auth information
 - Posts: stores post information
 
#### Site map

 - **/** Index page
 - **/auth/** the user login/register pages
 - **/blog/** the blog page
 - **/model/** the model view
 - **/api/** restful api
 - **/static/** static files
 - **/tutorial/** tutorial web pages
 - **/home** Index page (same as **/**)
 - All the other routes (include 404) will be required to **/**
 
#### Documentation

Auth: TODO

Blog: [docs/blog.md](docs/blog.md)

API: [docs/api.md](docs/api.md)

 
### Extra server

An internal server that runs a something unrelated to web

Could be integrated to the web server

## How to deploy

1. Clone this repo
    ```shell script
    git clone https://github.com/jimmy-zx/AIwaffle_Server1.git
    cd AIwaffle_Server1
    ```
1. Initialize submodules ```git submodule update --init```
1. Install dependencies ```pip3 install -r requirements.txt```
1. Config the server
    ```shell script
    mkdir instance
    $EDITOR instance/config.py
    ```
    - A secret key is recommend to config
    - If you don't want an extra\_server, set
        ```python
    USE_EXTRA_SERVER=False
        ```
1. Choose an production server to run the application
   - Current environment uses waitress
    ```shell script
    pip3 install waitress
    waitress-run --call 'server1.create_app
    ```

## Release notes

### Latest

#### Version 0.1.6

 - Updated and fixed routing
 - Updated new submodule
 
### Older versions

<details>
    <summary>Click to expand</summary>
    
<p>

#### Version 0.1.5

 - Completed documentation for statistics
 - Updated tests
 - Added production deployment documentation

#### Version 0.1.4
- Added statistics support

    Records the total requests on the server
       
    Could be accessed via ```/api/statistics/total```
       
    See the api documentation for details

</p>
</details>

## TODO List

### Version 0.1.7
 - [x] Remove posts view
 - [x] Remove statistics
 - [x] Switch to flask-sqlalchemy
 - [x] Add flask-login
 - [x] Remove front-end submodule
 - [x] Add external authorization (OAuth)
 - [ ] Fix tests

### Version 0.1.8
 - [ ] Uniform import style
 
### Version 0.2.0

 - [ ] Finish auth documentation
 - [ ] Finish backend documentation
 
### Version 0.2.1

 - [ ] Automatic deploy
 
## License and copyright

Licensed under the MIT license

Copyright 2019-2020

### Model

 - [jimmy-zx/AIwaffle](https://github.com/jimmy-zx/AIwaffle)


### Acknowledgements

 - [Flask](https://github.com/pallets/flask)
 - [example-oauth2-server](https://github.com/authlib/example-oauth2-server)
 - [AIwaffle/AIwaffle](https://github.com/AIwaffle/AIwaffle)
