from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from werkzeug import secure_filename
import os
from flask import send_from_directory

from helpers import *

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

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///website.db")

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    db.execute("UPDATE users SET locatie = :locatie WHERE id = :id", locatie=lookup(jsdata)[5], id=session["user_id"])
    print(lookup(jsdata)[5])
    return jsdata

@app.route("/")
@login_required
def index():

    return render_template("index.html")


@app.route("/vrienden", methods=["GET", "POST"])
@login_required
def vrienden():
    """Fotos van Vrienden."""
    if request.method == "GET":
        # foto's van vrienden hier

        vrienden_photos_list = db.execute("SELECT p.photo_id, p.file_name, u.username FROM users u, photos p, follow f " + \
                   "WHERE f.user_id = :user_id and f.f_user_id = u.id and p.user_id = f.f_user_id", \
                   user_id = session["user_id"])
        return render_template("vrienden.html", vrienden_photos = vrienden_photos_list)

    else:
        for i in request.form:
            if i[:4] == "like":
                photo_like_id = i[5:]
            elif i[:7] == "dislike":
                photo_like_id = i[8:]

            if db.execute ("SELECT valuation_id FROM valuation WHERE user_id = :user_id and photo_id = :photo_id", \
                            photo_id = photo_like_id, user_id = session["user_id"]):
                if i[:4] == "like":
                    db.execute("UPDATE valuation set like = :like WHERE user_id = :user_id and photo_id = :photo_id", \
                                like = "TRUE", photo_id = photo_like_id, user_id = session["user_id"])
                elif i[:7] == "dislike":
                    db.execute("UPDATE valuation set like = :like WHERE user_id = :user_id and photo_id = :photo_id", \
                                like = "FALSE", photo_id = photo_like_id, user_id = session["user_id"])
            else:
                if i[:4] == "like":
                    db.execute("INSERT INTO valuation (photo_id, user_id, like) VALUES (:photo_id, :user_id,:like)", \
                            photo_id = photo_like_id, user_id = session["user_id"], like = "TRUE")
                elif i[:7] == "dislike":
                    db.execute("INSERT INTO valuation (photo_id, user_id, like) VALUES (:photo_id, :user_id,:like)", \
                            photo_id = photo_like_id, user_id = session["user_id"], like = "FALSE")

        return redirect(url_for("vrienden"))

@app.route("/trofee")
@login_required
def trofee():
    """Trofee's laten zien."""
    return render_template("trofee.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    #session.clear()
    session["user_id"] = ""

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            flash('Provide a username')
            return redirect(request.url)

        # ensure password was submitted
        elif not request.form.get("password"):
            flash('Provide a password')
            return redirect(request.url)

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            flash('Invalid username/password')
            return redirect(request.url)

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/omgeving", methods=["GET", "POST"])
@login_required
def omgeving():
    """Fotos uit je omgeving."""
    if request.method == "GET":
        return render_template("omgeving.html", items=[i for i in range(20)])

    else:
        return render_template("omgeving.html")

@app.route("/profiel", methods=["GET", "POST"])
@login_required
def profiel():
    """Profiel Laten Zien"""
    if request.method == "GET":
        paths_profile = db.execute("SELECT file_name FROM photos WHERE user_id=:user_id", user_id = session["user_id"])
        paths_profile_2 = [file["file_name"] for file in paths_profile]
        return render_template("profiel.html", profile_photos = paths_profile_2)
    else:
        return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # ensure username was submitted
        if not username:
            flash('Provide a username')
            return redirect(request.url)

        # ensure password was submitted
        elif not password:
            flash('Provide a password')
            return redirect(request.url)

        # ensure passwords are equal
        elif not password == request.form.get("password2"):
            flash('Passwords must match')
            return redirect(request.url)

        # check if username already taken
        elif db.execute("SELECT * FROM users WHERE username = :username", username=username):
            flash('This username already exists')
            return redirect(request.url)

        # query database for username
        db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",username=username, hash=pwd_context.hash(password))

        # remember which user has logged in
        session["user_id"] = db.execute("SELECT * FROM users WHERE username = :username", username=username)[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    """Upload pictures."""
    if request.method == "POST":
        file = request.files['upload']
        if file.filename == '':
            flash('Select a file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        streepje = "-"
        unieke_foto = (str(session["user_id"]), filename)
        unieke_foto_join = streepje.join(unieke_foto)
        path_filename = os.path.join(app.config["UPLOAD_FOLDER"], unieke_foto_join)
        file.save(path_filename)

        db.execute("INSERT INTO photos (user_id, file_name,locatie) VALUES (:user_id, :file_name,:locatie)", \
        user_id = session["user_id"], file_name = unieke_foto_join, locatie = 6)
        return redirect(url_for("index"))

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

        if not request.form.get("follow_username"):
            flash('Provide a username')
            return redirect(request.url)

        user_row =  db.execute("SELECT id FROM users WHERE username=:username", username = request.form.get("follow_username"))

        if not user_row:
            flash('Provide an existing username')
            return redirect(request.url)

        f_user_id = user_row[0]["id"]
        if f_user_id == session["user_id"]:
            flash("You can't follow your own account")
            return redirect(request.url)

        if db.execute("SELECT user_id FROM follow WHERE user_id=:user_id and f_user_id=:f_user_id", \
        user_id = session["user_id"], f_user_id = f_user_id):
            flash("You already follow this account")
            return redirect(request.url)

        db.execute("INSERT INTO follow (user_id, f_user_id) VALUES (:user_id, :f_user_id)", \
        user_id = session["user_id"], f_user_id = f_user_id)

        return render_template("follow.html")

    else:
        return render_template("follow.html")
