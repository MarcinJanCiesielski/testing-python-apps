from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self) -> None:
        app.testing = True # Flask knows tha this is a test
        self.app = app.test_client
