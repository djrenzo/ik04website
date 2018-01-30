from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from passlib.apps import custom_app_context as pwd_context
from werkzeug import secure_filename
import os

db = SQL("sqlite:///website.db")

class Upload:
    def picUpload(self, file, userid, app, plaats):
        filename = secure_filename(file.filename)
        unieke_foto = (str(session["user_id"]), filename)
        unieke_foto_join = "-".join(unieke_foto)
        path_filename = os.path.join(app.config["UPLOAD_FOLDER"], unieke_foto_join)
        file.save(path_filename)

        caption = request.form.get("photo_caption")

        db.execute("INSERT INTO photos (user_id, file_name,locatie, caption) VALUES (:user_id, :file_name,:locatie,:caption)", \
        user_id = userid, file_name = unieke_foto_join, locatie = plaats, caption = caption)
        return redirect(url_for("profiel"))

class Friends:

    def getFriendsPhotos(self, userid):
        return db.execute("SELECT CASE WHEN p.caption IS NULL THEN '' ELSE p.caption END as caption, p.photo_id, " + \
        "p.file_name, u.username, count(vl.photo_id) as likes, count(vd.photo_id) as dislikes " + \
        "FROM users u, photos p, follow f " + \
        "LEFT OUTER JOIN valuation vl ON (vl.photo_id = p.photo_id and vl.like = 'TRUE') " + \
        "LEFT OUTER JOIN valuation vd ON (vd.photo_id = p.photo_id and vd.like = 'FALSE') " + \
        "WHERE f.user_id = :user_id and f.f_user_id = u.id and p.user_id = f.f_user_id " + \
        "GROUP BY p.photo_id", \
        user_id = userid)


    def setLike(self, request, userid):

        for i in request.form:
            if i[:4] == "like":
                photo_like_id = i[5:]
            elif i[:7] == "dislike":
                photo_like_id = i[8:]

            if db.execute ("SELECT valuation_id FROM valuation WHERE user_id = :user_id and photo_id = :photo_id", \
                            photo_id = photo_like_id, user_id = userid):
                if i[:4] == "like":
                    db.execute("UPDATE valuation set like = :like WHERE user_id = :user_id and photo_id = :photo_id", \
                                like = "TRUE", photo_id = photo_like_id, user_id = userid)
                elif i[:7] == "dislike":
                    db.execute("UPDATE valuation set like = :like WHERE user_id = :user_id and photo_id = :photo_id", \
                                like = "FALSE", photo_id = photo_like_id, user_id = userid)
            else:
                if i[:4] == "like":
                    db.execute("INSERT INTO valuation (photo_id, user_id, like) VALUES (:photo_id, :user_id,:like)", \
                            photo_id = photo_like_id, user_id = userid, like = "TRUE")
                elif i[:7] == "dislike":
                    db.execute("INSERT INTO valuation (photo_id, user_id, like) VALUES (:photo_id, :user_id,:like)", \
                            photo_id = photo_like_id, user_id = userid, like = "FALSE")

        return redirect(url_for("vrienden"))


class Profile:
    def getProfilePhotos(self, userid):
        return [file["file_name"] for file in db.execute("SELECT file_name FROM photos WHERE user_id=:user_id", user_id = userid)]




