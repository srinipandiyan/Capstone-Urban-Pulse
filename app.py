"""Flask app for Urban Pulse"""

from flask import Flask, render_template, request, flash, redirect, session, g, abort
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push()

from models import db, connect_db

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

@app.route("/")
def root():
    """Render homepage at root directory."""

    return render_template("base.html")

#User routes


@app.route("/user")
def user_profile():
    """Display user profile"""