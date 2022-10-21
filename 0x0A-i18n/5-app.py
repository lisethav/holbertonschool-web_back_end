#!/usr/bin/env python3
"""Aplicación Flask para traducir i18n
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

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
    """Encuentra una usuario por ella id
    """
    key = request.args.get("login_as")
    if key is not None:
        user = users.get(int(key))
        return user
    return None


@app.before_request
def before_request():
    """antes de la solicitud hecha
    """
    user = get_user()
    if user is not None:
        g.user = user


@ babel.localeselector
def get_locale():
    """localizar el idioma y la zona horaria de la aplicación
    """
    lg = request.args.get("locale")
    if lg is not None:
        if lg in Config.LANGUAGES:
            return lg
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@ app.route('/')
def home():
    """página de inicio de la aplicación del matraz
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
