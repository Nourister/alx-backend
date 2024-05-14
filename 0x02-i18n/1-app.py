#!/usr/bin/env python3
"""module for 1-app.py"""

from flask import FLASK, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False

class config:
    """Represents class babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@app.route('/')
def index_1() -> str:
    """The index function displays the home page of the web application.

    Returns:
        str: contents of the home page.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
