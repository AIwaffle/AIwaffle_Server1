
# Table of Contents

1.  [API Documentation](#orgd793fbd)
    1.  [User](#orgecb82b3)
        1.  [Register a new user](#org90379cb)
        2.  [Login an existing user](#org8e029da)
    2.  [Blog](#org4962cc9)
        1.  [Get all blogs](#orged5209a)
        2.  [Get one post](#orgd6ec590)
        3.  [Create](#org92e5491)
        4.  [Delete](#org8d30993)
        5.  [JSON data](#orgae94a02)
    3.  [Model](#org8251d4c)
        1.  [New session](#org5f1fd5f)
        2.  [Iterate several steps](#org45fcf40)


<a id="orgd793fbd"></a>

# API Documentation

For each API, we use POST to deliver form data, and use json for passing of
data structures. The response is a json string.


<a id="orgecb82b3"></a>

## User


<a id="org90379cb"></a>

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


<a id="org8e029da"></a>

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


<a id="org4962cc9"></a>

## Blog


<a id="orged5209a"></a>

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


<a id="orgd6ec590"></a>

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


<a id="org92e5491"></a>

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


<a id="org8d30993"></a>

### Delete

POST /api/blog/delete


<a id="orgae94a02"></a>

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


<a id="org8251d4c"></a>

## Model


<a id="org5f1fd5f"></a>

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


<a id="org45fcf40"></a>

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
    <td class="org-left">Predicted value with length of epoch_num</td>
    </tr>
    
    
    <tr>
    <td class="org-left">loss</td>
    <td class="org-left">float[]</td>
    <td class="org-left">The loss record for every epochs</td>
    </tr>
    
    
    <tr>
    <td class="org-left">accuracy</td>
    <td class="org-left">float[]</td>
    <td class="org-left">The accuracy record for every epochs</td>
    </tr>
    
    
    <tr>
    <td class="org-left">avg_loss</td>
    <td class="org-left">float</td>
    <td class="org-left">The average loss</td>
    </tr>
    </tbody>
    </table>

