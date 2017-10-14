

from . import BaseTest


class TestUser(BaseTest):
    def setUp(self):
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def testTrue(self):
        self.assertTrue(True)
