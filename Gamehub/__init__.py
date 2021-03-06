"""Flask main file."""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Index."""
    return "hello"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
