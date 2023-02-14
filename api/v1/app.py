#!/usr/bin/python3
"""Main Entry point for API set up"""

from api.v1 import views
from flask import Flask
from models import storage
from os import getenv


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Handle session closing on app exit"""
    storage.close()


if __name__ == '__main__':
    app.register_blueprint(views.app_views)
    host = getenv("HBNB_API_HOST") or "0.0.0.0"
    port = getenv("HBNB_API_PORT") or "5000"
    app.run(host=host, port=port, threaded=True)
