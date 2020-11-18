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
    """home:

    Creates list of all plant_posts in database sorted
    by newest first and renders on to home.html template

    Returns:
    home.html with all plants list insterted displayed.

    """
    all_plants = list(mongo.db.plant_posts.find().sort("_id", -1).limit(10))
    return render_template("home.html", all_plants=all_plants)


# Read and display all posts in all_plants.html
@app.route("/all_plants")
def all_plants():
    """all_plants:

    Creates list of all plant_posts in database sorted
    by newest first and renders on to all_plants.html

    Returns:
    all_plants.html with all plants list and displayed.

    """
    all_plants = list(mongo.db.plant_posts.find().sort("_id", -1))
    return render_template("all_plants.html", all_plants=all_plants)


# Search all plants
@app.route("/search_all_plants", methods=["GET", "POST"])
def search_all_plants():
    """search_all_plants:

    Allows user to search the plant_posts database using text.

    If matching results are found, returns:
    all_plants.html with matching plants displayed.

    Else, returns:
    all_plants to display all plant_posts in database.

    """

    if request.method == "POST":
        search = request.form.get("search")
        matching_plants = list(mongo.db.plant_posts.find(
            {"$text": {"$search": search}}))
        # check for search result matches
        if matching_plants:
            return render_template(
                "all_plants.html", matching_plants=matching_plants)
        else:
            flash("No results. Please try again or browse all plants below.")
            return redirect(url_for("all_plants"))


# Register username and password in join.html
@app.route("/join", methods=["GET", "POST"])
def join():
    """join:

    Allows user to create a username and password.

    Returns:
    join.html template

    On post to back-end:
        An if statement is used to check whether the inputted
        username already exists in the users database.

        If username does exist returns:
      join to refresh the page with flash message

        An if/else ladder is used to check that password and
        confirmed password match, then insert the user in the users database

        If statisfied, returns:
      user's profile and adds username to session

        Else returns:
      join to refresh the page with flash message

    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already in use, please try another")
            return redirect(url_for("join"))

        # check that the first password matched the "confirm password"
        confirm_password = request.form.get("confirm_password")
        password = request.form.get("password")

        if confirm_password == password:
            join_insert = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
            }
            mongo.db.users.insert_one(join_insert)
            # put the new user into session cookie
            session["user"] = request.form.get("username").lower()
            return redirect(url_for("profile", username=session["user"]))
        else:
            flash("Passwords don't match, please try again")
            return redirect(url_for("join"))
    return render_template("join.html")


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    """ login:

    Allows user to access their profile
    providing their username and password is correct.

    Returns:
    login.html template

    On post to back-end:
        An if statement is used to check whether the inputted
        username already exists in the users database.
        If it does, the check_password_hash from werkzeug security is used
        to check that the inputted password is correct.

        If correct, a session cookie is created create from username
        and returns:
      Profile with username inserted

        If they do not match returns:
      login to refresh the page with flash message

    """

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
                flash("Incorrect username and/or password please try again.")
                return redirect(url_for("login"))
        # return flash if username doesn't exist in database
        else:
            flash("Incorrect username and/or password please try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


# User profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """profile:

    Displays user's profile page.

    Args:
    1.  username: username from session cookie

    If no <username> inserted. Returns:
    redirect user to login

    Creates list of plants posted by session user.

    Checks that a session user is present.

    Returns:
    profile.html template with username and list displayed.

    """

    # get session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # find plant posted by sesssion user
    my_plants = list(mongo.db.plant_posts.find({"posted_by": session["user"]}))

    if session["user"]:
        return render_template(
            "profile.html", username=username, my_plants=my_plants)

    return redirect(url_for("login"))


# Logout function
@app.route("/logout")
def logout():
    """logout:

    Allows user to logout of their profile.

    Removes user from session cookie.

    Returns:
    Login page and flashes message.

    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Create a new plant post
@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    """add_plants:

    Allows user to add a new plant_post to the plant_posts database.

    Returns:
    add_plant.html template

    On post to back-end:
        Inserts plant_post based on user input.

        Returns:
        User's profile page.

    """
    is_air_purifying = True if request.form.get("is_air_purifying") else False
    if request.method == "POST":
        plant_post = {
            "plant_nickname": request.form.get("plant_nickname"),
            "plant_botanical_name": request.form.get("plant_botanical_name"),
            "plant_description": request.form.get("plant_description"),
            "plant_image_url": request.form.get("plant_image_url"),
            "best_environment": request.form.get("best_environment"),
            "water": request.form.get("water"),
            "humidity": request.form.get("humidity"),
            "feeding": request.form.get("feeding"),
            "is_air_purifying": is_air_purifying,
            "maintenance_level": request.form.get("maintenance_level"),
            "posted_by": session["user"],
            "post_date": datetime.utcnow(),
            "post_date_string": datetime.utcnow().strftime(
                'on: %d-%m-%y at: %H:%M')
        }
        mongo.db.plant_posts.insert_one(plant_post)
        flash("You're our hero <3. View your newly add plant below.")
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return redirect(url_for(
            "profile", username=username))

    maintenance_level = mongo.db.maintenance_level.find()
    return render_template(
        "add_plant.html", maintenance_level=maintenance_level)


# Edit/Update existing plant post
@app.route("/edit_plant/<plant_post_id>", methods=["GET", "POST"])
def edit_plant(plant_post_id):
    """edit_plant:

    Allows user to update a plant_post in the MongoDb.

    Arguments:
    1.  plant_post_id: Unique post id

    Returns:
    edit_plant.html template

    On post to back-end:
        Updates specified plant_post in plant_posts database

        Returns:
        plant_profile template

    """
    plant_post = mongo.db.plant_posts.find_one(
        {"_id": ObjectId(plant_post_id)})
    if request.method == "POST":
        is_air_purifying = True if request.form.get(
            "is_air_purifying") else False
        submit = {
            "plant_nickname": request.form.get("plant_nickname"),
            "plant_botanical_name": request.form.get("plant_botanical_name"),
            "plant_description": request.form.get("plant_description"),
            "plant_image_url": request.form.get("plant_image_url"),
            "best_environment": request.form.get("best_environment"),
            "water": request.form.get("water"),
            "humidity": request.form.get("humidity"),
            "feeding": request.form.get("feeding"),
            "is_air_purifying": is_air_purifying,
            "maintenance_level": request.form.get("maintenance_level"),
            "posted_by": session["user"],
            "post_date": datetime.utcnow(),
            "post_date_string": datetime.utcnow().strftime(
                'on: %d-%m-%y at: %H:%M')
        }
        mongo.db.plant_posts.update({"_id": ObjectId(plant_post_id)}, submit)
        flash("You have updated your post.")
        return redirect(url_for('plant_profile', plant_post_id=plant_post_id))

    maintenance_level = mongo.db.maintenance_level.find()
    return render_template(
        "edit_plant.html", plant_post=plant_post,
        maintenance_level=maintenance_level)


# Plant profile
@ app.route("/plant_profile/<plant_post_id>")
def plant_profile(plant_post_id):
    """plant_profile:

    Profile page for a specific plant with related comments.

    Arguments:
    1.  plant_post_id: Unique post id

    Finds specific plant.
    Creates list of related comments from comments database.

    Returns:
    plant_profile.html template

    """
    plant_post = mongo.db.plant_posts.find_one(
        {"_id": ObjectId(plant_post_id)})
    # Find comments for plant post
    comments = list((mongo.db.comments.find(
        {"plant_post_id": plant_post_id})))
    maintenance_level = mongo.db.maintenance_level.find()
    return render_template(
        "plant_profile.html", plant_post=plant_post,
        maintenance_level=maintenance_level, comments=comments)


# Delete plant post
@ app.route("/delete_plant/<plant_post_id>")
def delete_plant(plant_post_id):
    """delete_plant:

    Allows user to delete a plant_post in the mongoDb.

    Arguments:
    1.  plant_post_id: Unique post id

    Remove specific plant_post from plant_posts database.

    Returns:
    all_plants page

    """
    mongo.db.comments.remove({"plant_post_id": plant_post_id})
    mongo.db.plant_posts.remove({"_id": ObjectId(plant_post_id)})
    flash("Your post has been deleted")
    return redirect(url_for("all_plants"))


# Insert comment
@ app.route(
    "/<plant_post_id>/comments", methods=["GET", "POST"])
def insert_comment(plant_post_id):
    """insert_comment:

    Allows user to add a comment to a plant_profile page.

    Parameters:
        plant_post_id: Unique post id to be to be passed in to url.

    On post to back-end:
        Insert comment in to comments database.

        Returns:
        plant_profile page

    """
    if request.method == "POST":
        comment = {
            "plant_post_id": request.form.get("plant_post_id"),
            "posted_at": datetime.utcnow(),
            "posted_at_string": datetime.utcnow().strftime(
                '%H:%M:%S, %d-%m-%y'),
            "posted_by": session["user"],
            "comment_body": request.form.get("comment_body"),
        }
        mongo.db.comments.insert_one(comment)
        flash("Thanks for your comment!")
        return redirect(url_for(
            "plant_profile", plant_post_id=plant_post_id))


# Delete comment
@ app.route(
    "/<plant_post_id>/delete_comment/<comment_id>")
def delete_comment(plant_post_id, comment_id):
    """delete_comment

    Allows user to delete a specific comment regarding a specific plant.

    Arguments:
    1.  plant_post_id: Unique post id
    2   comment_id: Unique comment id

    Removes specific comment from comments database.

    Returns:
    plant_profile page

    """
    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    flash("Your comment has been deleted")
    return redirect(url_for(
        "plant_profile", plant_post_id=plant_post_id, comment_id=comment_id))


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    """page_not_found:

    Custom 404 error page

    Arguments:
    1.  e: Positional argument

    Returns:
    404.html template

    """
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
