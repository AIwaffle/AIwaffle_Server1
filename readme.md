# AIwaffle_server1

Version 0.1.4

[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fjimmy-zx%2FAIwaffle_Server1%2Fbadge%3Fref%3Dmaster&style=flat)](https://actions-badge.atrox.dev/jimmy-zx/AIwaffle_Server1/goto?ref=master)

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
 - **/static** static files
 - All the other routes will be required to **/**
 
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
### Version 0.1.5
 - Completed documentation for statistics
 - Updated tests
 - Added production deployment documentation
### Version 0.1.4
 - Added statistics support
 
   Records the total requests on the server
   
   Could be accessed via ```/api/statistics/total```
   
   See the api documentation for details
## TODO List
### Version 0.1.5
 - [x] Documentation for statistics
 - [x] Update tests
 - [x] Add production documentation
### Version 0.1.6
 - [ ] Finish posts view
### Version 0.2.0
 - [ ] Finish auth documentation
 - [ ] Finish backend documentation
 - [ ] Finish posts documentation
### Version 0.2.1
 - [ ] Automatic deploy
## License and copyright
Licensed under the MIT license

Copyright 2019-2020
### Model
 - [jimmy-zx/AIwaffle](https://github.com/jimmy-zx/AIwaffle)
forked from [IDl0T/AIwaffle](https://github.com/IDl0T/AIwaffle)
### Front end
 - [AlienKevin/AIWaffle-website](https://github.com/AlienKevin/AIWaffle-website)
 - [AlienKevin/elm-neural-net](https://github.com/AlienKevin/elm-neural-net)
 - [Flask example](https://github.com/pallets/flask)
