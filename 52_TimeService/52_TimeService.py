"""

Consuming external services is one thing, but it's important to be
able to create and consume your own service that others can use,
so you can support other developers who want to use services you'll
provide.

Create a simple web service that returns the current time as JSON
data, such as {"currentTime": "2050-01-24 15:06:26"}.

Then create a client application that connects to the web service,
parses the response, and displays the time.

___________________
Example Output
___________________

The current time is 15:06:26 UTC January 4 2050.

___________________
Constraints
___________________
- In your server application, be sure to set the content type to
application/json when you send the response.
- Build the server app with as little code as possible.

"""


"""
Server app will be written using Flask
To run the server (after installing flask (pip install...)):

export FLASK_APP=<<script name>>
flask run
"""

import flask
import datetime
import json

app = flask.Flask(__name__)


@app.route("/current-time")
def api_time():
    current_time = datetime.datetime.utcnow()
    current_time = current_time.strftime("%H:%M:%S UTC %B %d %Y")
    data = {"currentTime": current_time}
    js = json.dumps(data)

    resp = flask.Response(js, status=200, mimetype="application/json")
    return resp


if __name__ == "__main__":
    app.run()
