import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia"
        # self.database_path = "postgres://{}/{}".format('localhost:5000', self.database_name)
        self.database_path = "postgresql://postgres:postgres@localhost:5000/trivia"
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    """
    Test for get_all_categories: Tests for the status code, if success is true, if categories is returned and the length of the returned categories
    """
    def test_get_all_categories(self):

        # Make the request and process the response
        response = self.client().get('/categories')
        data = json.loads(response.data)

        # Make the assertions based on the response data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertEqual(len(data['categories']), 6)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()