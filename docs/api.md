
# Table of Contents

1.  [API Documentation](#org2d22a4f)
    1.  [User](#org1a3cc8b)
        1.  [Register a new user](#orge0e0dc4)
        2.  [Login an existing user](#org71e0a77)
    2.  [Blog](#orgcf2191c)
        1.  [Get all blogs](#org8b8a8f3)
        2.  [Get one post](#org4230519)
        3.  [Create](#orgc53a73d)
        4.  [Delete](#org03f6166)
        5.  [JSON data](#org9a4843d)
    3.  [Model](#org2faf58d)
        1.  [New session](#orgdf66709)
        2.  [Iterate one step](#org99a337c)


<a id="org2d22a4f"></a>

# API Documentation

For each API, we use POST to deliver form data, and use json for passing of
data structures. The response is a json string.


<a id="org1a3cc8b"></a>

## User


<a id="orge0e0dc4"></a>

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


<a id="org71e0a77"></a>

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


<a id="orgcf2191c"></a>

## Blog


<a id="org8b8a8f3"></a>

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
    <td class="org-left">author_ uuid</td>
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


<a id="org4230519"></a>

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


<a id="orgc53a73d"></a>

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


<a id="org03f6166"></a>

### Delete

POST /api/blog/delete


<a id="org9a4843d"></a>

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


<a id="org2faf58d"></a>

## Model


<a id="orgdf66709"></a>

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


<a id="org99a337c"></a>

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
    <td class="org-left">session_ id</td>
    <td class="org-left">string</td>
    <td class="org-left">The id of the model session</td>
    </tr>
    
    
    <tr>
    <td class="org-left">learning_ rate</td>
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
    <td class="org-left">avg_ loss</td>
    <td class="org-left">float</td>
    <td class="org-left">The average loss</td>
    </tr>
    </tbody>
    </table>

