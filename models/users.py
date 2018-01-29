from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from passlib.apps import custom_app_context as pwd_context

db = SQL("sqlite:///website.db")

class Users:
    userid = ""
    valid = False

    def register(self, request):
        username = request.form.get("username")
        password = request.form.get("password")
        self.valid = False

        # ensure username and password was submitted
        if not username or not password:
            flash('Provide a username and password')
            return redirect(request.url)

        # ensure passwords are equal
        elif not password == request.form.get("password2"):
            flash('Passwords must match')
            return redirect(request.url)

        # check if username already taken
        if db.execute("SELECT * FROM users WHERE username = :username", username=username):
            flash('This username already exists')
            return redirect(request.url)

        # query database for username
        db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",username=username, hash=pwd_context.hash(password))

        self.userid = db.execute("SELECT * FROM users WHERE username = :username", username=username)[0]["id"]
        self.valid = True
        return "OK"



    def login(self,request):
        username = request.form.get("username")
        password = request.form.get("password")
        self.valid = False

        # ensure username was submitted
        if not username:
            flash('Provide a username')
            return False

        # ensure password was submitted
        elif not password:
            flash('Provide a password')
            return False

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            flash('Invalid username/password')
            return False

        # remember which user has logged in
        self.userid = rows[0]["id"]

        # redirect user to home page
        self.valid = True
        return "OK"

    def setLocation(self, locatie, userid):
        db.execute("UPDATE users SET locatie = :locatie WHERE id = :userid", locatie=locatie, userid=userid)
        return "OK"

    def followUser(self, request, userid):

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
        user_id = userid, f_user_id = f_user_id)

        flash("You now follow " + request.form.get("follow_username"))
        return redirect(request.url)

