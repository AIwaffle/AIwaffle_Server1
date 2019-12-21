
# Table of Contents

1.  [API Documentation](#org51cb485)
    1.  [User](#org10d7b6c)
        1.  [Register a new user](#orgcce3137)
        2.  [Login an existing user](#org1a2e977)
    2.  [Model](#org01fc33e)
        1.  [New session](#orgb6d5430)
        2.  [General for all the following](#org96e534f)
        3.  [Forward the model](#orga6fabfc)
        4.  [Backward the model](#orgedb2ea8)
        5.  [Optimize the model](#orgdb0696f)
        6.  [Get the loss of the model](#orgbd3cf19)
        7.  [Get the model](#org47fce46)
        8.  [Iterate one step](#org2c96456)


<a id="org51cb485"></a>

# API Documentation

For each API, we use POST to deliver form data, and use json for passing of
data structures. The response is a json string.


<a id="org10d7b6c"></a>

## User


<a id="orgcce3137"></a>

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


<a id="org1a2e977"></a>

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


<a id="org01fc33e"></a>

## Model


<a id="orgb6d5430"></a>

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


<a id="org96e534f"></a>

### General for all the following

POST /api/model/\*

1.  JSON data

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


<a id="orga6fabfc"></a>

### Forward the model

POST /api/model/forward

1.  JSON data

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
    <td class="org-left">X</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">The input value</td>
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
    <td class="org-left">&#xa0;</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">Predicted value</td>
    </tr>
    </tbody>
    </table>


<a id="orgedb2ea8"></a>

### Backward the model

POST /api/model/backward

1.  JSON data

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
    <td class="org-left">Y</td>
    <td class="org-left">int[]</td>
    <td class="org-left">The real value</td>
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
    <td class="org-left">params</td>
    <td class="org-left">int[][][]</td>
    <td class="org-left">The weight matrix</td>
    </tr>
    
    
    <tr>
    <td class="org-left">grads</td>
    <td class="org-left">int[][][]</td>
    <td class="org-left">The gradient matrix</td>
    </tr>
    </tbody>
    </table>


<a id="orgdb0696f"></a>

### Optimize the model

POST /api/model/optimize

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
    <td class="org-left">params</td>
    <td class="org-left">int[][][]</td>
    <td class="org-left">The weight matrix</td>
    </tr>
    
    
    <tr>
    <td class="org-left">grads</td>
    <td class="org-left">int[][][]</td>
    <td class="org-left">The gradient matrix</td>
    </tr>
    </tbody>
    </table>


<a id="orgbd3cf19"></a>

### Get the loss of the model

POST /api/model/loss

1.  JSON data

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
    <td class="org-left">Y</td>
    <td class="org-left">int[]</td>
    <td class="org-left">The real value</td>
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
    <td class="org-left">&#xa0;</td>
    <td class="org-left">int</td>
    <td class="org-left">The loss of the model</td>
    </tr>
    </tbody>
    </table>


<a id="org47fce46"></a>

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
    <td class="org-left">params</td>
    <td class="org-left">int[][][]</td>
    <td class="org-left">The weight matrix</td>
    </tr>
    
    
    <tr>
    <td class="org-left">grads</td>
    <td class="org-left">int[][][]</td>
    <td class="org-left">The gradient matrix</td>
    </tr>
    </tbody>
    </table>


<a id="org2c96456"></a>

### Iterate one step

POST /api/model/iter

1.  JSON data

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
    <td class="org-left">X</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">The input value</td>
    </tr>
    
    
    <tr>
    <td class="org-left">Y</td>
    <td class="org-left">int[]</td>
    <td class="org-left">The real value</td>
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
    <td class="org-left">params</td>
    <td class="org-left">int[][][]</td>
    <td class="org-left">The weight matrix</td>
    </tr>
    
    
    <tr>
    <td class="org-left">grads</td>
    <td class="org-left">int[][][]</td>
    <td class="org-left">The gradient matrix</td>
    </tr>
    
    
    <tr>
    <td class="org-left">output</td>
    <td class="org-left">int[][]</td>
    <td class="org-left">Predicted value</td>
    </tr>
    </tbody>
    </table>

