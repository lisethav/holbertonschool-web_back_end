#!/usr/bin/env python3
"""Aplicación Flask para traducir i18n
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """página de inicio de la aplicación del matraz
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
