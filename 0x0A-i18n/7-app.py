#!/usr/bin/env python3
"""Aplicación Flask para traducir i18n
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
app = Flask(__name__)


babel = Babel(app)


class Config ():
    """configurar el idioma de la aplicación
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """finds a user by it id
    """
    k = request.args.get("login_as")
    if k is not None:
        usr = users.get(int(k))
        return usr
    return None


@app.before_request
def before_request():
    """before the request made
    """
    usr = get_user()
    if usr is not None:
        g.user = usr


@ babel.localeselector
def get_locale():
    """locate the language and timezone for the app
    """
    lg = request.args.get("locale")
    if lg is not None:
        if lg in Config.LANGUAGES:
            return lg
    usr = get_user()
    if usr is not None:
        if usr["locale"] in Config.LANGUAGES:
            return usr["locale"]
    hr = request.headers.get("locale")
    if hr is not None:
        if hr in Config.LANGUAGES:
            return usr["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """function for the timezone
    """
    timez_arg = request.args.get("timezone")
    if timez_arg is None:
        usr = get_user()
        if usr is not None:
            timez_arg = usr.get("timezone")
    try:
        pytz.timezone(timez_arg)
        return timez_arg
    except pytz.exceptions.UnknownTimeZoneError:
        return Config.BABEL_DEFAULT_TIMEZONE


@ app.route('/')
def home():
    """home page of flask app
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
