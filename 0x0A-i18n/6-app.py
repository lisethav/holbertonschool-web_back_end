#!/usr/bin/env python3
"""Aplicación Flask para traducir i18n
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


babel = Babel(app)


class Config ():
    """configurar el idioma de la aplicaci
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
    """Encuentra un usuario por él id
    """
    k = request.args.get("login_as")
    if k is not None:
        usr = users.get(int(k))
        return usr
    return None


@app.before_request
def before_request():
    """antes de la solicitud hecha
    """
    usr = get_user()
    if usr is not None:
        g.user = usr


@ babel.localeselector
def get_locale():
    """localizar el idioma y la zona horaria de la aplicación
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


@ app.route('/')
def home():
    """página de inicio de la aplicación del matraz
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
