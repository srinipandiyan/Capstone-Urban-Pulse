"""Flask app for Urban Pulse"""

from flask import Flask, render_template, request, flash, redirect, session, g, abort, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import UserAddForm, LoginForm
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
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
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
            return render_template('home.html')

        flash("Invalid credentials.", 'danger')

    return render_template('user/login.html', form=form)


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

#Search routes

## @app.route("/search", methods=['GET', 'POST'])
#def autocomplete():
   # """Suggest cities for search functionality and get selected city for comparison"""
    #if request.method == "GET":
    #    return render_template("home.html", cities=cities)

@app.route("/search/<string:city_id>", methods=['GET'])
def search(city_id):
    """Comparison page for city"""
    return render_template('city/comparison.html', city_id=city_id)