# Project Notes

## Setting the environment

~~~cmd
set FLASK_APP=hello.py
set FLASK_DEBUG = 1
flask run
~~~

## The url_for() function

Route to particular function from the webpage.
e.g: routing to hello(pincode) from index.html

## HTTP Verb

- POST --> POST is used to send data to a server to create/update a resource.
- GET --> GET is used to request data from a specified resource.
- PUT --> PUT is used to send data to a server to create/update a resource.
- HEAD --> HEAD is almost identical to GET, but without the response body.
- PATCH
- DELETE --> The DELETE method deletes the specified resource.

POST is used for sensitive data. The post values doesn't displays on url.

## Cookies and Sessions

Sessions are more secure than cookies, so we are replacing make_response with session.

To generate secure code, use
import os; print(os.urandom(16))
