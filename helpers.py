import csv
import urllib.request

from flask import redirect, render_template, request, session
from functools import wraps

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(ip):
    """Look up quote for symbol."""

    # query IP API for location
    try:

        # GET CSV
        url = f"http://ip-api.com/csv/{ip}"
        webpage = urllib.request.urlopen(url)

        # read CSV
        datareader = csv.reader(webpage.read().decode("utf-8").splitlines())

        # parse first row
        row = next(datareader)

        # ensure ip exists
        try:
            success = row[0]
        except:
            return None

        # return location name
        return row

    except:
        return None

