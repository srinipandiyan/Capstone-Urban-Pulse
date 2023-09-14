"""Flask app for Urban Pulse"""

from flask import Flask, render_template, request, flash, redirect, session, g, abort
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push()

from models import db, connect_db

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.

app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///urban_pulse'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
# Use shell command to turn on debug mode.
# $ export FLASK_DEBUG=1 && flask run
toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def root():
    """Render homepage at root directory."""

    return render_template("base.html")