from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for, json
from passlib.apps import custom_app_context as pwd_context
from werkzeug import secure_filename
import os

db = SQL("sqlite:///website.db")

class Trophies:

    def manage_trophies(self, userid):

        # UPDATE or INSERT new info
        if db.execute("SELECT user_id FROM trophies WHERE user_id=:user_id", user_id = userid):
            # update valuation, followers, follows and uploads
            db.execute("UPDATE trophies SET valuation_trophy = (SELECT COUNT (user_id) FROM valuation WHERE user_id=:user_id)", \
            user_id = userid)

            db.execute("UPDATE trophies SET followers_trophy = (SELECT COUNT (f_user_id) FROM follow WHERE f_user_id=:user_id)", \
            user_id = userid)

            db.execute("UPDATE trophies SET follows_trophy = (SELECT COUNT (user_id) FROM follow WHERE user_id=:user_id)", \
            user_id = userid)

            db.execute("UPDATE trophies SET uploads_trophy = (SELECT COUNT (user_id) FROM photos WHERE user_id=:user_id)", \
            user_id = userid)

            # init list for completed trophies
            completed_trophies = []

            # select user's trophy progress
            progress = db.execute("SELECT valuation_trophy AS valuations, followers_trophy AS followers, follows_trophy AS follows, uploads_trophy AS uploads FROM trophies WHERE user_id=:user_id", user_id = userid)

            # check for trophy valuations
            valuations_check = int(progress[0]["valuations"])
            if valuations_check >= 10:
                completed_trophies.append("You have valuated 10 photos!")

            # check for trophy followers
            followers_check = int(progress[0]["followers"])
            if followers_check >= 10:
                completed_trophies.append("You have 10 followers!")

            # check for trophy follows
            follows_check = int(progress[0]["follows"])
            if follows_check >= 10:
                completed_trophies.append("You are following 10 other people!")

            # check for trophy uploads
            upload_check = int(progress[0]["uploads"])
            if upload_check >= 10:
                completed_trophies.append("You have uploaded 10 photos!")

            # turn list into json format
            readable = json.dumps(completed_trophies)
            # remove unwanted characters
            for char in ['[',']','"']:
                readable=readable.replace(char," ")

            # check if any trophy in json
            if len(readable) <= 2:
                readable = "You currently have no trophies!"

            return readable

        else:
            # insert valuation, followers, follows and uploads
            db.execute("INSERT INTO trophies (user_id) VALUES (:user_id)", \
            user_id = userid)





