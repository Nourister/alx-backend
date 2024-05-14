#!/usr/bin/env python3
"""Module for task 0
"""

from flask import FLASK, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
    def index() -> str:
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
