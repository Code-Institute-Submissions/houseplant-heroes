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
    all_plants = mongo.db.plant_posts.find()
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
            return redirect(url_for("profile", username=session["user"]))
        else:
            flash("passwords don't match")
            return redirect(url_for("join"))
    return render_template("join.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check that hashed password matches input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    if request.method == "POST":
        plant_post = {
            "plant_name": request.form.get("plant_name"),
            "plant_description": request.form.get("plant_description"),
            "plant_image_url": request.form.get("plant_image_url"),
            "best_environment": request.form.get("best_environment"),
            "temperature": request.form.get("temperature"),
            "water": request.form.get("water"),
            "feeding": request.form.get("feeding"),
            "maintenance_level": request.form.get("maintenance_level"),
            "posted_by": session["user"]
        }
        mongo.db.plant_posts.insert_one(plant_post)
        flash("added")
        return redirect(url_for("all_plants"))
    maintenance_level = mongo.db.maintenance_level.find().sort("level_name", 1)
    return render_template(
        "add_plant.html", maintenance_level=maintenance_level)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
