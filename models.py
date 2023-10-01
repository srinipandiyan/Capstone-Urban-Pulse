"""SQLAlchemy models for Urban Pulse"""

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    base_city_id = db.Column(db.String(255), db.ForeignKey('cities.id'), nullable=True)
    occupation = db.Column(db.Text, nullable=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    base_city = db.relationship("City", backref="user_id", uselist=False)
    favorited_cities = db.relationship("FavoritedCity", backref="user")

    @classmethod
    def signup(cls, username, email, password):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False

class City(db.Model):
    """City model for Teleport cities"""
    __tablename__ = 'cities'

    id = db.Column(db.String(255), primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    scores = db.Column(db.JSON, nullable=False)
    #images = db.Column(db.Text, nullable=True)
    #details = db.Column(db.JSON, nullable=True)
    #salary = db.Column(db.JSON, nullable=True)
    
    user = db.relationship("User", backref="city")

class FavoritedCity(db.Model):
    """User favorited model of Teleport Cities"""
    __tablename__ = 'favorite_cities'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    city_id = db.Column(db.String(255), db.ForeignKey('cities.id'), nullable=False)

    def __repr__(self):
        return f'<Favorited Cities: id={self.id}, user_id={self.user_id}, city_id={self.city_id}>'

def connect_db(app):
    """Connect this database to provided Flask app."""
    
    db.app = app
    db.init_app(app)