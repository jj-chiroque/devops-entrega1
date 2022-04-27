import unittest
from application import application
from model.init import instantiate_db
from database.db_connection import db

class TestBase(unittest.TestCase):

    def setUp(self):
        application.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///testing.db"

        with application.app_context():
            db.create_all()

        self.app = application.test_client()

    def tearDown(self):
        with application.app_context():            
            db.session.remove()
            db.drop_all()
        
