import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, jsonify)
from datetime import datetime
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# Instance of Flask
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Home
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# Read and display all posts in all_plants.html
@app.route("/all_plants")
def all_plants():
    all_plants = mongo.db.plant_posts.find().sort("plant_botanical_name", 1)
    return render_template("all_plants.html", all_plants=all_plants)


# Search all plants
@app.route("/search_all_plants", methods=["GET", "POST"])
def search_all_plants():
    if request.method == "POST":
        search = request.form.get("search")
        all_plants = list(mongo.db.plant_posts.find(
            {"$text": {"$search": search}}))
        # check for search result matches
        if all_plants:
            flash("Results for...")
            return render_template("all_plants.html", all_plants=all_plants)
        else:
            flash("No results found, try again or browse all plants below")
            return redirect(url_for("all_plants"))


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
                    request.form.get("password")),
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
    # find plant posted by sesssion user
    my_plants = mongo.db.plant_posts.find({"posted_by": session["user"]})

    if session["user"]:
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
            "plant_nickname": request.form.get("plant_nickname"),
            "plant_botanical_name": request.form.get("plant_botanical_name"),
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
        flash("You're our hero <3. You're post has been added, thank you!")
        return redirect(url_for("all_plants"))
    maintenance_level = mongo.db.maintenance_level.find().sort("level_name", 1)
    return render_template(
        "add_plant.html", maintenance_level=maintenance_level)


# Edit/Update existing plant post
@app.route("/edit_plant/<plant_post_id>", methods=["GET", "POST"])
def edit_plant(plant_post_id):
    plant_post = mongo.db.plant_posts.find_one(
        {"_id": ObjectId(plant_post_id)})
    if request.method == "POST":
        is_air_purifying = "on" if request.form.get(
            "is_air_purifying") else "off"
        submit = {
            "plant_nickname": request.form.get("plant_nickname"),
            "plant_botanical_name": request.form.get("plant_botanical_name"),
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
        return redirect(url_for('plant_profile', plant_post_id=plant_post_id))
        flash("post updated")

    maintenance_level = mongo.db.maintenance_level.find().sort("level_name", 1)
    return render_template(
        "edit_plant.html", plant_post=plant_post,
        maintenance_level=maintenance_level)


# Delete plant post
@ app.route("/delete_plant/<plant_post_id>")
def delete_plant(plant_post_id):
    mongo.db.plant_posts.remove({"_id": ObjectId(plant_post_id)})
    flash("Post deleted")
    return redirect(url_for("all_plants"))


# Plant profile
@ app.route("/plant_profile/<plant_post_id>")
def plant_profile(plant_post_id):
    plant_post = mongo.db.plant_posts.find_one(
        {"_id": ObjectId(plant_post_id)})
    # Find comments for plant post
    comments = list((mongo.db.comments.find(
        {"plant_post_id": plant_post_id}).sort("posted_at", -1)))
    maintenance_level = mongo.db.maintenance_level.find().sort("level_name", 1)
    return render_template(
        "plant_profile.html", plant_post=plant_post,
        maintenance_level=maintenance_level, comments=comments)


# Insert comment
@ app.route(
    "/plant_profile/<plant_post_id>/comments", methods=["GET", "POST"])
def insert_comment(plant_post_id):
    if request.method == "POST":
        submit={
            "plant_post_id": request.form.get("plant_post_id"),
            "posted_at": datetime.utcnow(),
            "posted_by": session["user"],
            "comment_body": request.form.get("comment_body"),
        }
        mongo.db.comments.insert_one(submit)
        flash("inserted")
        return redirect(url_for(
            "plant_profile", plant_post_id=plant_post_id))


# Edit/Update comment
@ app.route(
    "/<plant_post_id>/edit_comment/<comment_id>", methods=["GET", "POST"])
def edit_comment(comment_id, plant_post_id):
    if request.method == "POST":
        submit={
            "plant_post_id": request.form.get("plant_post_id"),
            "posted_at": datetime.utcnow(),
            "posted_by": session["user"],
            "comment_body": request.form.get("comment_body"),
        }
        mongo.db.comments.update({"_id": ObjectId(comment_id)}, submit)
        flash("Comment edited")
        return redirect(url_for("plant_profile", plant_post_id=plant_post_id))
    comment=mongo.db.comments.find_one(
        {"_id": ObjectId(comment_id)})
    plant_post=mongo.db.plant_posts.find_one(
        {"_id": ObjectId(plant_post_id)})
    return render_template(
        "edit_comment.html", comment=comment, plant_post=plant_post)


# Delete comment
@ app.route("/<plant_post_id>/delete_comment/<comment_id>")
def delete_comment(comment_id, plant_post_id):
    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    flash("Comment deleted")
    return redirect(url_for("plant_profile", plant_post_id=plant_post_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
