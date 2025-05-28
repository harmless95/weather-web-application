import unittest
from app import app

class TestUsername(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.base_url = "/weather_forecast/"

    def test_city(self):
        city = "moscow"
        url = self.base_url + "/" + city
        response = self.app.get(url)
        respose_text = response.data.decode()
        self.assertIsNotNone(city in respose_text)

