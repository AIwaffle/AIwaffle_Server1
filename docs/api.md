- [API Documentation](#sec-1)
  - [User](#sec-1-1)
    - [Register a new user](#sec-1-1-1)
    - [Login an existing user](#sec-1-1-2)
  - [Model](#sec-1-2)
    - [Forward the model](#sec-1-2-1)
    - [Backward the model](#sec-1-2-2)
    - [Evaluate the model](#sec-1-2-3)
    - [Get the loss of the model](#sec-1-2-4)
    - [Get the model](#sec-1-2-5)

# API Documentation<a id="sec-1"></a>

For each API, we use POST to deliver form data, and use json for passing of data structures. The response is a json string.

## User<a id="sec-1-1"></a>

### Register a new user<a id="sec-1-1-1"></a>

POST /api/auth/register

1.  Form data

    | Name     | Format | Description                                        |
    |-------- |------ |-------------------------------------------------- |
    | username | string | The username of the user                           |
    | password | string | The password of the user (or hash of the password) |

2.  Response

    | Name    | Format | Description                                  |
    |------- |------ |-------------------------------------------- |
    | success | bool   | Whether the register is success              |
    | uuid    | string | The uuid of the user (only when success)     |
    | reason  | string | Human readable reason of failure (when fail) |

### Login an existing user<a id="sec-1-1-2"></a>

POST /api/auth/login

1.  Form data

    See POST /api/auth/register

2.  Response

    400 error when the username and/or password is not valid.
    
    | Name    | Format | Description                            |
    |------- |------ |-------------------------------------- |
    | uuid    | string | The uuid of the user                   |
    | expires | float  | The timestamp when the session expires |
    | token   | string | The token of the session               |

## Model<a id="sec-1-2"></a>

### Forward the model<a id="sec-1-2-1"></a>

GET /api/model/forward

1.  Response

    | Name | Format  | Description     |
    |---- |------- |--------------- |
    |      | int[][] | Predicted value |

### Backward the model<a id="sec-1-2-2"></a>

GET /api/model/backward

1.  Response

    | Name | Format  | Description         |
    |---- |------- |------------------- |
    |      | int[][] | The weight matrix   |
    |      | int[][] | The gradient matrix |

### Evaluate the model<a id="sec-1-2-3"></a>

GET /api/model/evaluate

1.  Response

    | Name | Format | Description              |
    |---- |------ |------------------------ |
    |      | int    | The result of evaluation |

### Get the loss of the model<a id="sec-1-2-4"></a>

GET /api/model/loss

1.  Response

    | Name | Format | Description           |
    |---- |------ |--------------------- |
    |      | int    | The loss of the model |

### Get the model<a id="sec-1-2-5"></a>

GET /api/model/model

1.  Response

    | Name | Format  | Description               |
    |---- |------- |------------------------- |
    | data | int[][] | The random generated data |
    | X    | int[][] | The input                 |
    | Y    | int[][] | The output                |
    | n    | int     | X.shape[0]                |
    | m    | int     | X.shape[1]                |
    | W    | int[][] | The weight matrix         |
    | A    | int[][] | The predicted value       |
