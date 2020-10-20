import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/all_plants")
def all_plants():
    all_plants = mongo.db.all_plants.find()
    return render_template("all_plants.html", all_plants=all_plants)


@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already in user, please try another")
            return redirect(url_for("join"))

        confirm_password = request.form.get("confirm_password")
        password = request.form.get("password")

        if confirm_password == password:
            join = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(join)
            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("success")
        else:
            flash("passwords don't match")
            return redirect(url_for("join"))
    return render_template("join.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
