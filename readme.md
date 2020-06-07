# AIwaffle_server1

Develop branch

Version 0.1.7

![Python application](https://github.com/AIwaffle/AIwaffle_Server1/workflows/Python%20application/badge.svg?branch=dev)

Backend server for [IDl0T/AIwaffle](https://github.com/IDl0T/AIwaffle)

## Components

### Web server

#### Network

Using Flask framework

#### Database

SQLite

Models
 - Users: stores user auth information
 
#### Site map

 - **/** Index page
 - **/auth/** the user login/register pages
 - **/blog/** the blog page
 - **/model/** the model view
 - **/api/** restful api
 - **/static/** static files
#### Documentation

Auth: TODO

OAuth2: TODO

API: [docs/api.md](docs/api.md)

 
### Extra server

An internal server that runs a something unrelated to web

Could be integrated to the web server

## Deploy
TODO


## Release notes

### Latest

### Version 0.1.7
 - Removed posts view
 - Removed statistics
 - Switched to flask-sqlalchemy
 - Added flask-login
 - Removed front-end submodule
 - Added OAuth2 authorization
 - Fixed tests
 - Fixed OAuth2
 - Added OAuth2 tests
 
### Older versions

<details>
    <summary>Click to expand</summary>
    
<p>

#### Version 0.1.6

 - Updated and fixed routing
 - Updated new submodule

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

### Version 0.1.8
 - [ ] Uniform coding style (Google)
 - [ ] Support logging configuration
 
### Version 0.2.0

 - [ ] Finish auth documentation
 - [ ] Finish OAuth2 documentation
 - [ ] Finish backend documentation
 - [ ] Add deployment note
 
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
