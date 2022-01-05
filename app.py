"""
    app module deals with server configs
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """hello_world returns  html response

    Returns:
        [html]: [response]
    """
    return "<h2>first application in flask</h2>"
