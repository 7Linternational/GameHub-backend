"""Flask main file."""

import os
from flask import Flask
# from flask import Response
from flask import render_template
from rq import Queue
from worker import conn
from testing.Testing import test_commitment_api
from testing.Testing import check_test

app = Flask(__name__)
q = Queue(os.environ['QUEUE_NAME'], connection=conn)


@app.route('/')
def index():
    """Testing page."""
    return render_template('index.html')


@app.route('/testing', methods=['GET', 'POST'])
def testing():
    """Testing endpoint."""
    res = q.enqueue(test_commitment_api, timeout=7200)
    print(res)
    return "Test started"


@app.route('/check', methods=['GET'])
def check():
    """Check."""
    return check_test()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
