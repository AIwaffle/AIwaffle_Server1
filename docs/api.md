
# Table of Contents

1.  [API Documentation](#org222e948)
    1.  [User](#orgbe35673)
        1.  [Register a new user](#orgb0807df)
        2.  [Login an existing user](#org005be84)
    2.  [Blog](#org75a0cc1)
        1.  [Get all blogs](#orgda51388)
        2.  [Get one post](#orgfb32f37)
        3.  [Create](#org786a9c2)
        4.  [Delete](#org092135a)
        5.  [JSON data](#org2a0c425)
    3.  [Model](#orgc3ac53b)
        1.  [New session](#orgb301f24)
        2.  [Iterate several steps](#orgec1a1d2)


<a id="org222e948"></a>

# API Documentation

For each API, we use POST to deliver form data, and use json for passing of
data structures. The response is a json string.


<a id="orgbe35673"></a>

## User


<a id="orgb0807df"></a>

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


<a id="org005be84"></a>

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


<a id="org75a0cc1"></a>

## Blog


<a id="orgda51388"></a>

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
    <td class="org-left">author_uuid</td>
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


<a id="orgfb32f37"></a>

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


<a id="org786a9c2"></a>

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


<a id="org092135a"></a>

### Delete

POST /api/blog/delete


<a id="org2a0c425"></a>

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


<a id="orgc3ac53b"></a>

## Model


<a id="orgb301f24"></a>

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


<a id="orgec1a1d2"></a>

### Iterate several steps

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
    <td class="org-left">session_id</td>
    <td class="org-left">string</td>
    <td class="org-left">The id of the model session</td>
    </tr>
    
    
    <tr>
    <td class="org-left">epoch<sub>num</sub></td>
    <td class="org-left">int</td>
    <td class="org-left">The number of epochs (optional, default=1)</td>
    </tr>
    
    
    <tr>
    <td class="org-left">learning_rate</td>
    <td class="org-left">float</td>
    <td class="org-left">The learning rate (optional, default=0.01)</td>
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
    <td class="org-left">X</td>
    <td class="org-left">float[][]</td>
    <td class="org-left">The input data matrix</td>
    </tr>
    
    
    <tr>
    <td class="org-left">Y</td>
    <td class="org-left">float[][]</td>
    <td class="org-left">The output data matrix</td>
    </tr>
    
    
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
    <td class="org-left">float[][][]</td>
    <td class="org-left">Predicted value with length of epoch<sub>num</sub></td>
    </tr>
    
    
    <tr>
    <td class="org-left">loss</td>
    <td class="org-left">float[]</td>
    <td class="org-left">The loss record for every epochs</td>
    </tr>
    
    
    <tr>
    <td class="org-left">eval</td>
    <td class="org-left">float[]</td>
    <td class="org-left">The eval record for every epochs</td>
    </tr>
    
    
    <tr>
    <td class="org-left">avg_ loss</td>
    <td class="org-left">float</td>
    <td class="org-left">The average loss</td>
    </tr>
    </tbody>
    </table>

