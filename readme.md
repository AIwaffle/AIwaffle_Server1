# AIwaffle_server1
Version 0.0.5

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
 - **/** Index page
 - **/auth/** the user login/register pages
 - **/blog/** the blogs page
 - **/model/** the model view
#### Documentation
Auth: TODO

Blog: [docs/blog.md](docs/blog.md)

API: [docs/api.md](docs/api.md)
#### Other routes
 - **/static** static files
### Extra server
An internal server that runs a something unrelated to web
#### Network
Using UNIX socket
#### Communication
Sending and receiving JSON objects
## License and copyright
Licensed under the MIT license

Copyright 2019-2020
### Model
 - [jimmy-zx/AIwaffle](https://github.com/jimmy-zx/AIwaffle)
forked from [IDl0T/AIwaffle](https://github.com/IDl0T/AIwaffle)
### Front end
 - [AlienKevin/elm-neural-net](https://github.com/AlienKevin/elm-neural-net)
 - [Flask example](https://github.com/pallets/flask)
