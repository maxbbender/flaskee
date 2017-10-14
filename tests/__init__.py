from flask_testing import TestCase

from ..flaskee import createApp, db


class BaseTest(TestCase):
    db = db

    def create_app(self):
        return createApp()
