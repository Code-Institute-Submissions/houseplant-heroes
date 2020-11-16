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

    Creates list of plant_posts in MongoDb named 'all_plants'
    Sorts list by Id(highest to lowest) and limits results to 10.

    Returns: 
        renders template for home.html with all_plants
        list insterted and displayed.

    """
    all_plants = list(mongo.db.plant_posts.find().sort("_id", -1).limit(10))
    return render_template("home.html", all_plants=all_plants)


# Read and display all posts in all_plants.html
@app.route("/all_plants")
def all_plants():
    """all_plants:

    Creates list of plant_posts in MongoDb named 'all_plants'
    Sorts list alphabetically.

    Returns: 
    renders template for all_plants.html with all_plants list insterted
    and displayed.

    """
    all_plants = list(
        mongo.db.plant_posts.find().sort("plant_nickname", 1))
    return render_template("all_plants.html", all_plants=all_plants)


# Search all plants
@app.route("/search_all_plants", methods=["GET", "POST"])
def search_all_plants():
    """search_all_plants:
    Allows users to search the plant_posts MongoDb using text.

    Retrieves search text posted by user and
    compares to text within plant_posts MongoDb.
    Creates a list of matching results named 'all_plants'.

    If matching results are found,
    return renders the template for all_plants.html
    with all_plants list insterted and displayed to the user.

    Else if no results are found,

    Returns:
    redirects users
    to the url for all_plants and a flash message is displayed
    to the user that explains that there are no matching
    results but they can browse all plants displayed below.

    """

    if request.method == "POST":
        search = request.form.get("search")
        all_plants = list(mongo.db.plant_posts.find(
            {"$text": {"$search": search}}))
        # check for search result matches
        if all_plants:
            return render_template("all_plants.html", all_plants=all_plants)
        else:
            flash("No results. Please try again or browse all plants below.")
            return redirect(url_for("all_plants"))


# Register username and password in join.html
@app.route("/join", methods=["GET", "POST"])
def join():
    """
    Function to allow user to create a username, password and profile.

    Return renders template for join.html.

    User posts a desired username which is retrieve from the form.
    An if/else ladder is first, used to check
    whether that username already exists in the user MongoDb.
    If a match is found, a message is flashed to the user username
    already exist and return redirects user back
    to the url for join so they are able to try again.

    Both the password and confirmed password are
    retrieved from the form, the an if statement checks that they match.
    When all if conditions are satisfied, the username and
    password are retrieved and a password is generated using
    werkzeug security generate_password_hash.
    These are then inserted in to the user MongoDb and a session cookie
    is created for the user from the inputted username.
    Return redirects user to their profile page based on session cookie.

    If the passwords don't match, a flash message is displayed
    and return redirects back to join.html.

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
            join = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
            }
            mongo.db.users.insert_one(join)
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
    """
    Function to allow users to access their profile
    providing their username and password is correct.

    Return renders template for login.html.

    User posts username which is retrieve from the form.
    An if/else ladder is first, used to check username is in the user MongoDb.

    If it does, the check_password_hash from werkzeug security is used to
    check that the inputted password is correct.
    If it is, a session cookie is created from a session cookie
    is created for the user from the inputted username
    and return redirects to their profile page.

    If they do not match, a flash message is displayed
    and return redirects back to login.

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

    return render_template("login.html")


# User profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Function to displays users profile page.

    Parameters:
        username: Generated by finding a username in users
        Mongodb that matches the session cookie to be passed in to url.

    Plant_posts in MongoDb is searched for posted_by the session user
    and a list, my_plants, is created.

    An if statement checks that there is a session user,
    if there is, return renders a template for profile.html with
    username = username and my_plants = my_plants
    to be displayed.

    If there is no session user, return redirects to login.

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
    """
    Function to allow users to logout of their profile.

    Removes user from session cookie,
    return redirects to login page and flashes message.

    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Create a new plant post
@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    """
    Function to allow users to add a new plant_post to the MongoDb.

    Finds maintenece_level in MongoDb.
    Return renders template for add_plant.html with
    maitenance_level = maintenance level

    Retrieve air_purfiying from form.
    When user posts form, retrieve all information and save as 'plant_post'.
    Insert plant_post in to plant_posts MongoDb.
    Flash message of thanks and return redirects to
    users profile page.

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
            "posted_datetime": datetime.utcnow(),
            "posted_datetime_string": datetime.utcnow().strftime(
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
    """
    Function to allow users to update a plant_post in the MongoDb.
    Uses bson ObjectId to render Mongodb documents by their unique id.

    Parameters:
        plant_post_id: Unique post id to be to be passed in to url.

    Finds maintenece_level in MongoDb.
    Return renders template for edit_plant.html with plant_post=plant_post
    and maitenance_level = maintenance level.

    Retrieve specific plant post from plant_posts using _id to convert,
    'plant_post_id' in to bson data type, that will be passed in to url.
    When user posts form, retrieve all information and save as 'submit'.
    Update specified plant_post with new information and flash message.
    Return redirects back to the plants profile.

    """
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
            "water": request.form.get("water"),
            "humidity": request.form.get("humidity"),
            "feeding": request.form.get("feeding"),
            "is_air_purifying": is_air_purifying,
            "maintenance_level": request.form.get("maintenance_level"),
            "posted_by": session["user"],
            "lastest_post_date": datetime.utcnow().strftime(
                'on %d-%m-%y at %H:%M')
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
    """
    Function to render the profile page for a
    specific plant and display comments related to that plant.
    Uses bson ObjectId to render Mongodb documents by their unique id.

    Parameters:
        plant_post_id: Unique post id to be to be passed in to url.

    Retrieve specific plant post from plant_posts using _id to convert
    "plant_post_id" in to bson data type, that will be passed in to url.
    Creates list, 'comments' from comments in
    Mongdb with a matching plant_post_id.
    Finds maintenece_level in MongoDb. Return renders template
    for plant_profile.html with plant_post=plant_post,
    maintenance_level=maintenance_level, comments=comments.

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
    """
    Function to allow user to delete a plant_post in the mongoDb.
    Uses bson ObjectId to render Mongodb documents by their unique id.

    Parameters:
        plant_post_id: Unique post id to be to be passed in to url.

    Remove specific plant post from plant_posts
    using _id to convert "plant_post_id"
    in to bson data type, that will be passed in to url.
    Return redirects to url for all_plants and flash message.

    """
    mongo.db.plant_posts.remove({"_id": ObjectId(plant_post_id)})
    # mongo.db.comments.remove({"plant_post_id": {
    #     "_id": ObjectId(plant_post_id)}})
    flash("Your post has been deleted")
    return redirect(url_for("all_plants"))


# Insert comment
@ app.route(
    "/<plant_post_id>/comments", methods=["GET", "POST"])
def insert_comment(plant_post_id):
    """
    Function to allow users to add a comment
    regarding a specific plant to the MongDb.
    Uses bson ObjectId to render Mongodb documents by their unique id.

    Parameters:
        plant_post_id: Unique post id to be to be passed in to url.

    When user posts form, retrieve all information and save as 'comment'.
    Insert comment in to comments MongoDb.
    Flash message of thanks and return redirects to
    url for the plant_profile with newly created comment displayed.

    """
    if request.method == "POST":
        comment = {
            "plant_post_id": request.form.get("plant_post_id"),
            "posted_at": datetime.utcnow().strftime(
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
    """
    Function to allow users to delete a comment
    regarding a specific plant from the MongDb.
    Uses bson ObjectId to render Mongodb documents by their unique id.

    Parameters:
        plant_post_id: Unique post id to be to be passed in to url.
        comment_id: Unique comment id to be to be passed in to url.

    Remove specific comment from comments using _id to convert
    "comment_id" in to bson data type, that will be passed in to url.
    Return redirects to url for plant_post and flash message.


    """
    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    flash("Your comment has been deleted")
    return redirect(url_for(
        "plant_profile", plant_post_id=plant_post_id, comment_id=comment_id))


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
