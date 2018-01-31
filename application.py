from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from flask import send_from_directory
import models.photos
import models.users

from helpers import *

import safygiphy

user_class = models.users.Users()
friends = models.photos.Friends()
profile = models.photos.Profile()
upl = models.photos.Upload()
surrounding = models.photos.Omgeving()



# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response


# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["UPLOAD_FOLDER"] = 'upload'
Session(app)


@app.route('/postmethod', methods = ['POST'])
@login_required
def get_post_javascript_data():
    print(lookup(request.form['javascript_data'])[5])
    return user_class.setLocation(lookup(request.form['javascript_data'])[5], session["user_id"])

@app.route("/")
@login_required
def index():
    if session["user_id"] == "":
        return redirect(url_for("login"))
    else:

        return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        user_class.register(request)

        if user_class.valid == False:
            return redirect(request.url)

        else:
            session["user_id"] = user_class.userid
            return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""
    # forget any user_id
    session["user_id"] = ""

    if request.method == "POST":
        user_class.login(request)

        if user_class.valid == False or user_class.userid == "":
            return redirect(request.url)

        else:
            session["user_id"] = user_class.userid
            return redirect(url_for("index"))
    else:
        g = safygiphy.Giphy()
        gif = [g.trending()["data"][x]["id"] for x in range(2,20)]

        # Will return a random GIF with the tag "success"
        return render_template("login.html", gif_id=gif)

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))


@app.route("/vrienden", methods=["GET", "POST"])
@login_required
def vrienden():
    """Fotos van Vrienden."""
    if request.method == "GET":
        # foto's van vrienden hier

        g = safygiphy.Giphy()
        gif = [g.trending()["data"][x]["id"] for x in range(2,20)]
        return render_template("vrienden.html", vrienden_photos = friends.getFriendsPhotos(session["user_id"]), gif_id=gif)

    else:
        return render_template("vrienden.html")


@app.route("/trofee")
@login_required
def trofee():
    """Trofee's laten zien."""
    return render_template("trofee.html")

@app.route("/omgeving", methods=["GET", "POST"])
@login_required
def omgeving():
    """Fotos uit je omgeving."""
    if request.method == "GET":
        # foto's van omgeving hier
        return render_template("omgeving.html", omgeving_photos = surrounding.getOmgevingPhotos(session["user_id"]))

    else:
        return surrounding.setLike(request, session["user_id"])

@app.route("/profiel", methods=["GET"])
@login_required
def profiel():
    """Profiel Laten Zien"""
    if request.method == "GET":
        return render_template("profiel.html", profile_photos = profile.getProfilePhotos(session["user_id"]))


@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    """Upload pictures."""
    if request.method == "POST":
        plaats = request.form.get("plaats")
        file = request.files['upload']
        if file.filename == '':
            flash('Select a file')
            return redirect(request.url)
        return upl.picUpload(file, session["user_id"], app, plaats)

    else:
        return render_template("upload.html")

@app.route('/upload/<filename>')
def uploaded(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route("/follow", methods=["GET", "POST"])
@login_required
def follow():
    """Fotos uit je omgeving."""
    if request.method == "POST":
        return user_class.followUser(request, session["user_id"])

    else:
        return render_template("follow.html")

@app.route("/unfollow", methods=["GET", "POST"])
@login_required
def unfollow():
    """Fotos uit je omgeving."""
    if request.method == "POST":
        return user_class.unfollowUser(request, session["user_id"])

    else:
        return render_template("unfollow.html")
