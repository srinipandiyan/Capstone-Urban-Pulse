"""City model tests."""

# run these tests like:
#
#    python -m unittest test_city_model.py

from app import app
from models import db, City

from sqlalchemy import exc
from unittest import TestCase


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///urban_pulse_test'
db.create_all()

class CityModelTestCase(TestCase):
    """Test city model."""

    def setUp(self):
        """Create test client and add sample city."""
        db.drop_all()
        db.create_all()

        #Create a sample city for testing
        city = City(
            id='sample-city-id',
            name='Sample City, United States',
            scores={'score_1': 1, 'score_2': 2},
            photo='sample_photo_url',
            details={'detail_1': 'value_1', 'detail_2': 'value_2'},
            salaries={'occupation_1': '50000', 'occupation_2': '60000'}
        )

        db.session.add(city)
        db.session.commit()
        self.city = city

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res
    
    def test_create_city(self):
        """Create and add new city."""
        city = City(
            id='new-city-id',
            name='New City, United States',
            scores={'score_3': 3, 'score_4': 4},
            photo='new_photo_url',
            details={'detail_3': 'value_3', 'detail_4': 'value_4'},
            salaries={'occupation_3': '55000', 'occupation_4': '65000'}
        )

        db.session.add(city)
        db.session.commit()

        new_city = City.query.get(city.id)
        self.assertIsNotNone(new_city)
        self.assertEqual(new_city.name, 'New City, United States')
        self.assertEqual(new_city.scores, {'score_3': 3, 'score_4': 4})


    def test_city_attributes(self):
        """Access city attributes."""
        #Access attributes from test city model
        self.assertEqual(self.city.id, 'sample-city-id')
        self.assertEqual(self.city.name, 'Sample City, United States')
        self.assertEqual(self.city.scores, {'score_1': 1, 'score_2': 2})
        self.assertEqual(self.city.photo, 'sample_photo_url')
        self.assertEqual(self.city.details, {'detail_1': 'value_1', 'detail_2': 'value_2'})
        self.assertEqual(self.city.salaries, {'occupation_1': '50000', 'occupation_2': '60000'})
      

    def test_city_create_invalid_data(self):
        """Create a city with invalid data and test for failure"""
        
        #city name contains an invalid datatype: dict.
        invalid_datatype = City(
            id='invalid-city',
            name={'Invalid City, United States'},
            scores={'score_1': 1, 'score_2': 2},
            photo='some-photo-url',
            details={'detail_3': 'value_3', 'detail_4': 'value_4'},
            salaries={'occupation_3': '55000', 'occupation_4': '65000'}
        )

        db.session.add(invalid_datatype)
        
        with self.assertRaises(exc.ProgrammingError) as context:
            db.session.commit()


    def test_city_create_incomplete_data(self):
        """Create a city with incomplete data and test for failure"""
        #id, name, and scores arguments are set to non-nullable
        #city name is passed as None
        incomplete_data = City(
            id='incomplete-city',
            name=None,
            scores={'score_1': 1, 'score_2': 2},
            photo='new_photo_url',
            details={'detail_3': 'value_3', 'detail_4': 'value_4'},
            salaries={'occupation_3': '55000', 'occupation_4': '65000'}
        )
        
        db.session.add(incomplete_data)

        with self.assertRaises(exc.IntegrityError) as context:
            db.session.commit()