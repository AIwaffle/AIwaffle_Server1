
# Table of Contents

1.  [API Documentation](#org1d13e10)
    1.  [User](#orga61740e)
        1.  [Register a new user](#org0c3a474)
        2.  [Login an existing user](#orgb69fc98)
    2.  [Model](#org2a1ff18)
        1.  [New session](#org076eeb0)
        2.  [General for all the following](#org5e96ceb)
        3.  [Forward the model](#orgb9431ba)
        4.  [Backward the model](#org2dc017a)
        5.  [Evaluate the model](#org6ef7196)
        6.  [Get the loss of the model](#org7dd6926)
        7.  [Get the model](#orge6b223a)


<a id="org1d13e10"></a>

# API Documentation

For each API, we use POST to deliver form data, and use json for passing of
data structures. The response is a json string.


<a id="orga61740e"></a>

## User


<a id="org0c3a474"></a>

### Register a new user

POST /api/auth/register

1.  Form data

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Format</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">username</td>
    <td class="org-left">string</td>
    <td class="org-left">The username of the user</td>
    </tr>
    
    
    <tr>
    <td class="org-left">password</td>
    <td class="org-left">string</td>
    <td class="org-left">The password of the user (or hash of the password)</td>
    </tr>
    </tbody>
    </table>

2.  Response

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Format</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">success</td>
    <td class="org-left">bool</td>
    <td class="org-left">Whether the register is success</td>
    </tr>
    
    
    <tr>
    <td class="org-left">uuid</td>
    <td class="org-left">string</td>
    <td class="org-left">The uuid of the user (only when success)</td>
    </tr>
    
    
    <tr>
    <td class="org-left">reason</td>
    <td class="org-left">string</td>
    <td class="org-left">Human readable reason of failure (when fail)</td>
    </tr>
    </tbody>
    </table>


<a id="orgb69fc98"></a>

### Login an existing user

POST /api/auth/login

1.  Form data

    See POST /api/auth/register

2.  Response

    400 error when the username and/or password is not valid.
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Format</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">uuid</td>
    <td class="org-left">string</td>
    <td class="org-left">The uuid of the user</td>
    </tr>
    
    
    <tr>
    <td class="org-left">expires</td>
    <td class="org-left">float</td>
    <td class="org-left">The timestamp when the session expires</td>
    </tr>
    
    
    <tr>
    <td class="org-left">token</td>
    <td class="org-left">string</td>
    <td class="org-left">The token of the session</td>
    </tr>
    </tbody>
    </table>


<a id="org2a1ff18"></a>

## Model


<a id="org076eeb0"></a>

### New session

GET /api/model/new

1.  Response

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Format</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">&#xa0;</td>
    <td class="org-left">string</td>
    <td class="org-left">The id of the created model session</td>
    </tr>
    </tbody>
    </table>


<a id="org5e96ceb"></a>

### General for all the following

POST /api/model/\*

1.  Form data

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Format</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">session<sub>id</sub></td>
    <td class="org-left">string</td>
    <td class="org-left">The id of the model session</td>
    </tr>
    </tbody>
    </table>


<a id="orgb9431ba"></a>

### Forward the model

POST /api/model/forward

1.  Response

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Format</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">&#xa0;</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">Predicted value</td>
    </tr>
    </tbody>
    </table>


<a id="org2dc017a"></a>

### Backward the model

POST /api/model/backward

1.  Response

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Format</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">&#xa0;</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">The weight matrix</td>
    </tr>
    
    
    <tr>
    <td class="org-left">&#xa0;</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">The gradient matrix</td>
    </tr>
    </tbody>
    </table>


<a id="org6ef7196"></a>

### Evaluate the model

POST /api/model/evaluate

1.  Response

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Format</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">&#xa0;</td>
    <td class="org-left">int</td>
    <td class="org-left">The result of evaluation</td>
    </tr>
    </tbody>
    </table>


<a id="org7dd6926"></a>

### Get the loss of the model

POST /api/model/loss

1.  Response

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Format</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">&#xa0;</td>
    <td class="org-left">int</td>
    <td class="org-left">The loss of the model</td>
    </tr>
    </tbody>
    </table>


<a id="orge6b223a"></a>

### Get the model

POST /api/model/model

1.  Response

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Format</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">data</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">The random generated data</td>
    </tr>
    
    
    <tr>
    <td class="org-left">X</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">The input</td>
    </tr>
    
    
    <tr>
    <td class="org-left">Y</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">The output</td>
    </tr>
    
    
    <tr>
    <td class="org-left">n</td>
    <td class="org-left">int</td>
    <td class="org-left">X.shape[0]</td>
    </tr>
    
    
    <tr>
    <td class="org-left">m</td>
    <td class="org-left">int</td>
    <td class="org-left">X.shape[1]</td>
    </tr>
    
    
    <tr>
    <td class="org-left">W</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">The weight matrix</td>
    </tr>
    
    
    <tr>
    <td class="org-left">A</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">The predicted value</td>
    </tr>
    </tbody>
    </table>

