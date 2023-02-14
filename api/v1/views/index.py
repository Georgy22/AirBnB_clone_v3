#!/usr/bin/python3
"""Defining the base endpoints"""

from api.v1 import views


app_views = views.app_views


@app_views.route("/status")
def get_status():
    return {"status": "OK"}
