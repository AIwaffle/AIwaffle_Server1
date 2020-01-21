
# Table of Contents

1.  [Blog documentation](#org2927f35)
    1.  [Blog base url](#org4c74767)
        1.  [Index](#orgbae99d4)
        2.  [Create](#org47b586c)
        3.  [Delete](#org6a461a3)


<a id="org2927f35"></a>

# Blog documentation

For each page, we use GET to deliver the html page, and use POST form data for
actions.


<a id="org4c74767"></a>

## Blog base url

/blog


<a id="orgbae99d4"></a>

### Index

1.  GET

    GET *blog*
    Returns the blog page
    Jinja templates are used for rendering posts
    See /server1/templates/blog/index.html for details


<a id="org47b586c"></a>

### Create

1.  GET

    GET /blog/create
    Returns the create page

2.  POST

    POST /blog/create
    Cookies are automatically used for getting username and passwords
    Form data:
    
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


<a id="org6a461a3"></a>

### Delete

1.  POST

    POST /blog/<id>/delete
    Cookies are automatically used for getting username and passwords

