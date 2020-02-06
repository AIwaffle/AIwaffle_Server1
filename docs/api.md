
# Table of Contents

1.  [API Documentation](#org33f8616)
    1.  [User](#org2533591)
        1.  [Register a new user](#orga0de7c8)
        2.  [Login an existing user](#org5dcf286)
    2.  [Blog](#org98fc326)
        1.  [Get all blogs](#org2c53463)
        2.  [Get one post](#org179128e)
        3.  [Create](#orgc6ded0a)
        4.  [Delete](#orgeef90b8)
        5.  [JSON data](#orgd059009)
    3.  [Model](#org6e1d6fc)
        1.  [New session](#org90ea787)
        2.  [Iterate one step](#org0ada64a)


<a id="org33f8616"></a>

# API Documentation

For each API, we use POST to deliver form data, and use json for passing of
data structures. The response is a json string.


<a id="org2533591"></a>

## User


<a id="orga0de7c8"></a>

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


<a id="org5dcf286"></a>

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


<a id="org98fc326"></a>

## Blog


<a id="org2c53463"></a>

### Get all blogs

GET /api/blog/all

1.  Response

    A json dict, with post\\<sub>id</sub> as key and post object as value.
    
    Post object:
    
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
    <td class="org-left">id</td>
    <td class="org-left">int</td>
    <td class="org-left">The id of the post</td>
    </tr>
    
    
    <tr>
    <td class="org-left">author\\<sub>uuid</sub></td>
    <td class="org-left">string</td>
    <td class="org-left">The uuid of the author</td>
    </tr>
    
    
    <tr>
    <td class="org-left">created</td>
    <td class="org-left">datetime: isoformat</td>
    <td class="org-left">The created time</td>
    </tr>
    
    
    <tr>
    <td class="org-left">title</td>
    <td class="org-left">string</td>
    <td class="org-left">The title of the post</td>
    </tr>
    
    
    <tr>
    <td class="org-left">body</td>
    <td class="org-left">string</td>
    <td class="org-left">The body of the post</td>
    </tr>
    </tbody>
    </table>


<a id="org179128e"></a>

### Get one post

POST /api/blog/get

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
    <td class="org-left">id</td>
    <td class="org-left">int</td>
    <td class="org-left">The id of the post</td>
    </tr>
    </tbody>
    </table>

2.  Response

    The post object(json), when the post is found
    
    404 when the post is not found


<a id="orgc6ded0a"></a>

### Create

POST /api/blog/create

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
    <td class="org-left">uuid</td>
    <td class="org-left">string</td>
    <td class="org-left">The uuid of the user</td>
    </tr>
    
    
    <tr>
    <td class="org-left">expires</td>
    <td class="org-left">float</td>
    <td class="org-left">The expire time of the session</td>
    </tr>
    
    
    <tr>
    <td class="org-left">token</td>
    <td class="org-left">string</td>
    <td class="org-left">The token of the session</td>
    </tr>
    
    
    <tr>
    <td class="org-left">title</td>
    <td class="org-left">string</td>
    <td class="org-left">The title of the post</td>
    </tr>
    
    
    <tr>
    <td class="org-left">body</td>
    <td class="org-left">string</td>
    <td class="org-left">The body of the post</td>
    </tr>
    </tbody>
    </table>

2.  Response

    The id of the post when success


<a id="orgeef90b8"></a>

### Delete

POST /api/blog/delete


<a id="orgd059009"></a>

### JSON data

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
<td class="org-left">The expire time of the session</td>
</tr>


<tr>
<td class="org-left">token</td>
<td class="org-left">string</td>
<td class="org-left">The token of the session</td>
</tr>


<tr>
<td class="org-left">id</td>
<td class="org-left">int</td>
<td class="org-left">The id of the post</td>
</tr>
</tbody>
</table>

1.  Response

    true when the post was successfully deleted


<a id="org6e1d6fc"></a>

## Model


<a id="org90ea787"></a>

### New session

POST /api/model/new

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


<a id="org0ada64a"></a>

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
    <td class="org-left">session\\<sub>id</sub></td>
    <td class="org-left">string</td>
    <td class="org-left">The id of the model session</td>
    </tr>
    
    
    <tr>
    <td class="org-left">learning\\<sub>rate</sub></td>
    <td class="org-left">float</td>
    <td class="org-left">The learning rate (optional)</td>
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
    <td class="org-left">W</td>
    <td class="org-left">float[][][]</td>
    <td class="org-left">The weight matrix</td>
    </tr>
    
    
    <tr>
    <td class="org-left">dW</td>
    <td class="org-left">float[][][]</td>
    <td class="org-left">The gradient matrix</td>
    </tr>
    
    
    <tr>
    <td class="org-left">A</td>
    <td class="org-left">float[][]</td>
    <td class="org-left">Predicted value</td>
    </tr>
    
    
    <tr>
    <td class="org-left">loss</td>
    <td class="org-left">float[]</td>
    <td class="org-left">The loss record for every few steps (50 for default)</td>
    </tr>
    
    
    <tr>
    <td class="org-left">eval</td>
    <td class="org-left">float[]</td>
    <td class="org-left">The eval record for every few steps</td>
    </tr>
    
    
    <tr>
    <td class="org-left">avg\\<sub>loss</sub></td>
    <td class="org-left">float</td>
    <td class="org-left">The average loss</td>
    </tr>
    </tbody>
    </table>

