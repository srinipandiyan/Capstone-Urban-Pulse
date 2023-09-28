"""Flask app for Urban Pulse"""

from flask import Flask, render_template, request, flash, redirect, session, g, abort, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
import requests

from forms import UserAddForm, LoginForm, UpdateUserForm
from models import db, connect_db, User

from urban import cities

CURR_USER_KEY = "curr_user"

app = Flask(__name__)
app.app_context().push()

app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///urban_pulse'
#uncomment in production
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# set all to false for production/remove echo
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# Use shell command to turn on debug mode.
# $ export FLASK_DEBUG=1 && flask run
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

##############################################################################
#User signup/login/logout routes

#User is kept track of globally in this route
#The `@app.before_request` is a decorator that runs a function before all incoming requests to the Flask app. 
@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""
    #The g object, short for context globals, is an obj that can keep track of data within the lifetime of a single request.
    #The following code is used to initialize Flask's g object and store the session user.
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route("/")
def root():
    """Render homepage at root directory."""

    return render_template("base.html")


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, re-present form.

    If there already is a user with that username: flash message
    and re-present form.
    """

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data,
            )
            #signup method adds validated user model to session
            db.session.commit()


        except IntegrityError as e:
            flash("Username already taken", 'danger')
            return render_template('user/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('user/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            return redirect('/search')

        flash("Invalid credentials.", 'danger')

    return render_template('user/login.html', form=form)

@app.route('/search')
def homepage():
    """Homepage of Urban Pulse"""
    if g.user:
        #user is authenticated, render the homepage
        return render_template('home.html')
    else:
        #user is not authenticated, redirect to the index
        flash("Invalid credentials.", 'danger')
        return redirect("/")


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()
    flash("User is logged out.", "success")

    return redirect("/")


#User routes

@app.route("/user")
def user_profile():
    """Display user profile"""

    return render_template('user/profile.html')
    
@app.route("/user/edit", methods=["GET", "POST"])
def edit_profile():
    """Display and handle user profile update form"""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/login")
    
    user = g.user
    form = UpdateUserForm(obj=user)

    if form.validate_on_submit():
        if User.authenticate(user.username, form.password.data):
            #if valid authentication, access user model and update with form inputs
            user.username = form.username.data
            user.email = form.email.data

            db.session.commit()
            #redirect to user details page
            flash("User profile updated.", "success")
            return redirect("/user")
        
        else: flash("Please try again. Incorrect password credenitials.", "danger")

    #redisplay form on unsuccessful validation
    return render_template('user/edit.html', form=form) #,user_id=user.id)

#Search routes
def get_ua_id(city):
    """
    Given city from autocomplete suggestion, convert city name to API callable urban area id (ua_id).
    ua_id will have all chars in lowercase, country and punctuation removed, and spaces replaced with hypens (-).

    parameters:
        city (str): the user readable city name and location, for example: "San Francisco Bay Area, United States"

    returns:
        returns ua_id (str)
    """

    #split the city str by comma, retain the city name, replace any spaces with a hypen, and lowercase all chars.
    city_name = city.split(',')
    ua_id = city_name[0].strip().replace(' ', '-').lower()
    return ua_id


def get_city_scores(ua_id):
    """
    Given ua_id, call city scores from Teleport API for urban areas.
    
    parameters: 
        ua_id (str): the urban area id of a city, for example: "san-francisco-bay-area".
            arg must given in lowercase with any spaces replaced with hypens (-).
        
    returns:
       if request == 200, returns a JSON dict object from the API.
            else, returns NONE.
    """
    #API URL route for urban area scores
    url = f"https://api.teleport.org/api/urban_areas/slug%3A{ua_id}/scores/"
    #GET request
    response = requests.get(url)
    
    #verify request was successful with status code 200
    if response.status_code == 200:
        #return parsed json response
        return response.json()
        
    else:
        #handle case where the request was unsuccessful
        print(f"GET request failed: status code {response.status_code}")
        return None
        

@app.route("/search/<string:city>", methods=['GET'])
def search(city):
    """Comparison page for city"""
    ua_id = get_ua_id(city)
    data = get_city_scores(ua_id)
    
    return render_template('city/comparison.html', city=city, data=data)