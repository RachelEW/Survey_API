import unittest
from unittest.mock import patch
from run import app

class TestSurveyRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_route_returns_list_of_surveys_when_surveys_in_database(self):
        result = self.app.get('survey_api/v1/surveys')
        print(result.data)
        self.assertEquals(result.status_code, 200)
