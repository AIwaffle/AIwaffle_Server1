# AIwaffle_server1
Backend server for [IDl0T/AIwaffle](https://github.com/IDl0T/AIwaffle)
## Components
### Web server
#### Network
Using Flask framework
#### Database
SQLAlchemy + SQLite

Models
 - Users: stores user information
#### Site map
 - **/** index page (TODO)
 - **/auth/register** register page for user
 - **/auth/login** login page for user
 - **/auth/logout** logout for user
 - **/model/** the model view (TODO)
#### API
See [docs/api.md](docs/api.md) for details
#### Other routes
 - **/static** static files
### Extra server
An internal server that runs a something unrelated to web
#### Network
Using UNIX socket
#### Communication
Sending and receiving JSON objects
#### Functions
 - A numpy model
## Development notes
### TODOs
 - [x] TODO: Implement model api
 - [x] TODO: Complete model tests
 - [x] TODO: Complete general tests
## License and copyright
Licensed under the MIT license

Copyright 2019 <jimmy-zx, DanielDAIDLaw>
### Model
 - [jimmy-zx/AIwaffle](https://github.com/jimmy-zx/AIwaffle)
forked from [IDl0T/AIwaffle](https://github.com/IDl0T/AIwaffle)
### Front end
 - [AlienKevin/elm-neural-net](https://github.com/AlienKevin/elm-neural-net)
 - [Flask example](https://github.com/pallets/flask)
