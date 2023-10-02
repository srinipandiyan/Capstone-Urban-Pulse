"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py

from app import app
from models import db, User

from sqlalchemy import exc
from unittest import TestCase


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///urban_pulse_test'
db.create_all()

class UserModelTestCase(TestCase):
    """Test user model."""

    def setUp(self):
        """Create test client and add sample user."""
        db.drop_all()
        db.create_all()

        user1 = User.signup(username="test1", email="test1@email.org", password="randompassword")
        uid_1 = 24
        user1.id = uid_1

        user2 = User.signup(username="test2", email="test2@email.com", password="a_string")
        uid_2 = 12345
        user2.id = uid_2

        db.session.commit()

        user1 = User.query.get(uid_1)
        user2 = User.query.get(uid_2)

        self.user1 = user1
        self.uid_1 = uid_1

        self.user2 = user2
        self.uid_2 = uid_2

        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res
    
    def test_user_model(self):
        """User object instantiation"""

        u = User(
            username="testuser",
            email="test@test.com",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        #User object when instantiated should not contain favorited_cities nor a base_city
        self.assertEqual(len(u.favorited_cities), 0)
        self.assertEqual(u.base_city, None)

    def test_signup(self):
        """User signup method is able to successfully create a new user given valid credentials"""

        valid_u = User.signup(username="testuser", 
                             email="test@test.com", 
                             password="password"
        )

        uid = 4321
        valid_u.id = uid
        db.session.commit()

        u_test = User.query.get(uid)
        self.assertIsNotNone(u_test)
        self.assertEqual(u_test.username, "testuser")
        self.assertEqual(u_test.email, "test@test.com")
        self.assertTrue(u_test.password.startswith("$2b$"))

    def test_signup_fail(self):
        """User signup method is unable to create a new user given invalid credentials"""

        invalid_u = User.signup(username=None, email="test@test.com", password="password")
        uid = 5432
        invalid_u.id = uid

        with self.assertRaises(exc.IntegrityError) as context:
            db.session.commit()

    def test_authenticate(self):
        """User authenticate method successfully returns a user given valid username and password credentials"""

        u = User.authenticate(self.user1.username, "randompassword")
        self.assertIsNotNone(u)
        self.assertEqual(u.id, self.uid_1)

    def test_authenticate_fail(self):
        """User authenticate method does not return a user given invalid username and password credentials"""

        self.assertFalse(User.authenticate(self.user1.username, "wrongpassword"))
        self.assertFalse(User.authenticate("nonexistentuser", "randompassword"))
