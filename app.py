"""Flask main file."""

from flask import Flask
from rq import Queue
from worker import conn

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
