#!/usr/bin/env python3
"""
Flask Babel instantiation
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Babel Class configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale():
    """
    Getting the suited language for a locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def index():
    """
    Index page routing
    """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run()
