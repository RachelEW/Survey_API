import unittest
from unittest.mock import patch, Mock, PropertyMock
from db import (connect_db, get_all_surveys, add_survey,
                add_survey_response, number_survey_responses, number_available_places,
                survey_builder_assign_id)

class TestSurveyRoutes(unittest.TestCase):
    
    @patch('pymongo.collection.Collection.find_one')
    @patch('Survey_API.db.random.randint')
    def test_assigns_unique_id(self, mock_random, mock_mongo):
        mock_mongo.return_value = None
        mock_random.return_value = 123456
        result = survey_builder_assign_id()
        self.assertEqual(result, 123456)

    @patch('pymongo.collection.Collection.find_one')
    @patch('Survey_API.db.random.randint')
    def test_tries_again_to_assign_unique_id_if_first_id_taken(self, mock_random, mock_mongo):
        mock_mongo.side_effect = [{'survey_name':'test'}, None]
        mock_random.side_effect = [873456, 345678]
        result = survey_builder_assign_id()
        self.assertEqual(result, 345678)