from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from passlib.apps import custom_app_context as pwd_context
from werkzeug import secure_filename
import os

db = SQL("sqlite:///website.db")

class Trophies:
    def manage_trophies(self, userid):


        if db.execute("SELECT user_id FROM trophies WHERE user_id=:user_id", user_id = userid):
            # update amount of valuation given
            db.execute("UPDATE trophies SET valuation_trophy = (SELECT COUNT (user_id) FROM valuation WHERE user_id=:user_id)", \
            user_id = userid)

            # update amount of followers
            db.execute("UPDATE trophies SET followers_trophy = (SELECT COUNT (f_user_id) FROM follow WHERE f_user_id=:user_id)", \
            user_id = userid)

            # update amount of follows
            db.execute("UPDATE trophies SET follows_trophy = (SELECT COUNT (user_id) FROM follow WHERE user_id=:user_id)", \
            user_id = userid)

            # update amount of uploads
            db.execute("UPDATE trophies SET uploads_trophy = (SELECT COUNT (user_id) FROM photos WHERE user_id=:user_id)", \
            user_id = userid)

        else:
            # insert amount of valuation given
            db.execute("INSERT INTO trophies (user_id, valuation_trophy) SELECT user_id, COUNT(user_id) FROM valuation WHERE user_id=:user_id", \
            user_id = userid)

            # insert amout of followers
            db.execute("INSERT INTO trophies (user_id, followers_trophy) SELECT user_id, COUNT(f_user_id) FROM follow WHERE user_id=:user_id", \
            user_id = userid)

            # insert amout of follows
            db.execute("INSERT INTO trophies (user_id, follows_trophy) SELECT user_id, COUNT(user_id) FROM follow WHERE user_id=:user_id", \
            user_id = userid)

            # insert amount of uploads
            db.execute("INSERT INTO trophies (user_id, uploads_trophy) SELECT user_id, COUNT(user_id) FROM photos WHERE user_id=:user_id", \
            user_id = userid)

    def trophy_progress(self, userid):

        completed_trophies = []

        # check valuations
        valuation = db.execute("SELECT COUNT (user_id) AS valuations FROM valuation WHERE user_id=:user_id", user_id = userid)
        valuations_check = int(valuation[0]["valuations"])
        if valuations_check >= 15:
            completed_trophies.append(valuations_check)

        # check followers
        follower = db.execute("SELECT COUNT(f_user_id) AS followers FROM follow WHERE user_id=:user_id", user_id = userid)
        followers_check = int(follower[0]["followers"])
        if followers_check >= 10:
            completed_trophies.append(followers_check)

        # check follows
        follow = db.execute("SELECT COUNT(user_id) AS follows FROM follow WHERE user_id=:user_id", user_id = userid)
        follows_check = int(follow[0]["follows"])
        if follows_check >= 2:
            completed_trophies.append(follows_check)

        # check uploads
        upload = db.execute("SELECT COUNT(user_id) AS uploads FROM photos WHERE user_id=:user_id", user_id = userid)
        upload_check = int(upload[0]["uploads"])
        if upload_check >= 10:
            completed_trophies.append(upload_check)


        return completed_trophies