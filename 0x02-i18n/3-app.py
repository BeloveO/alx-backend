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


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Retrieves suited locale
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """
    Index page routing
    """
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run()
