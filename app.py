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


# Read and display all posts in all_plants.html
@app.route("/all_plants")
def all_plants():
    all_plants = mongo.db.plant_posts.find()
    return render_template("all_plants.html", all_plants=all_plants)


# Register username and password in join.html
@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already in user, please try another")
            return redirect(url_for("join"))

        # check that the first password matched the "confirm password"
        confirm_password = request.form.get("confirm_password")
        password = request.form.get("password")

        if confirm_password == password:
            join = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(join)
            # put the new user into session cookie
            session["user"] = request.form.get("username").lower()
            flash("success")
            return redirect(url_for("profile", username=session["user"]))
        else:
            flash("passwords don't match")
            return redirect(url_for("join"))
    return render_template("join.html")


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check that hashed password matches user inputted password
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

    return render_template("login.html")


# User profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        my_plants = mongo.db.plant_posts.find()
        return render_template(
            "profile.html", username=username, my_plants=my_plants)

    return redirect(url_for("login"))


# Logout function
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Create a new plant post
@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    is_air_purifying = "on" if request.form.get("is_air_purifying") else "off"
    if request.method == "POST":
        plant_post = {
            "plant_botanical_name": request.form.get("plant_botanical_name"),
            "plant_nickname": request.form.get("plant_nickname"),
            "plant_description": request.form.get("plant_description"),
            "plant_image_url": request.form.get("plant_image_url"),
            "best_environment": request.form.get("best_environment"),
            "temperature": request.form.get("temperature"),
            "water": request.form.get("water"),
            "feeding": request.form.get("feeding"),
            "is_air_purifying": is_air_purifying,
            "maintenance_level": request.form.get("maintenance_level"),
            "posted_by": session["user"]
        }
        mongo.db.plant_posts.insert_one(plant_post)
        flash("added")
        return redirect(url_for("all_plants"))
    maintenance_level = mongo.db.maintenance_level.find().sort("level_name", 1)
    return render_template(
        "add_plant.html", maintenance_level=maintenance_level)


# Update existing plant post
@app.route("/edit_plant/<plant_post_id>", methods=["GET", "POST"])
def edit_plant(plant_post_id):
    if request.method == "POST":
        is_air_purifying = "on" if request.form.get(
            "is_air_purifying") else "off"
        submit = {
            "plant_botanical_name": request.form.get("plant_botanical_name"),
            "plant_nickname": request.form.get("plant_nickname"),
            "plant_description": request.form.get("plant_description"),
            "plant_image_url": request.form.get("plant_image_url"),
            "best_environment": request.form.get("best_environment"),
            "temperature": request.form.get("temperature"),
            "water": request.form.get("water"),
            "feeding": request.form.get("feeding"),
            "is_air_purifying": is_air_purifying,
            "maintenance_level": request.form.get("maintenance_level"),
            "posted_by": session["user"]
        }
        mongo.db.plant_posts.update({"_id": ObjectId(plant_post_id)}, submit)
        return redirect(url_for("all_plants"))
        flash("post updated")

    plant_post = mongo.db.plant_posts.find_one(
        {"_id": ObjectId(plant_post_id)})
    maintenance_level = mongo.db.maintenance_level.find().sort("level_name", 1)
    return render_template(
        "edit_plant.html", plant_post=plant_post,
        maintenance_level=maintenance_level)


# Delete plant post
@app.route("/delete_plant/<plant_post_id>")
def delete_plant(plant_post_id):
    mongo.db.plant_posts.remove({"_id": ObjectId(plant_post_id)})
    flash("Post deleted")
    return redirect(url_for("all_plants"))


# Plant profile
@app.route("/plant_profile/<plant_post_id>")
def plant_profile(plant_post_id):
    plant_post = mongo.db.plant_posts.find_one(
        {"_id": ObjectId(plant_post_id)})
    maintenance_level = mongo.db.maintenance_level.find().sort("level_name", 1)
    return render_template(
        "plant_profile.html", plant_post=plant_post,
        maintenance_level=maintenance_level)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
