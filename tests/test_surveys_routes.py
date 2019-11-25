import unittest
from unittest.mock import patch, Mock, PropertyMock
from run import app

class TestSurveyRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.new_survey_data = {
            'survey_name': 'Opinions about lemons',
            'available_places': 30,
            'user_id': 5438
        }
        self.survey_response_success = {
            'survey_id': 654321,
            'user_id': 8756,
        }
        self.survey_response_fail = {
            'survey_id': 390373,
            'user_id': 8756,
        }
        self.all_surveys = [{"survey_name" : "Test Survey", "survey_id" : "098430", "available_places" : 23, "user_id" : "3214" },
                            {"survey_id" : "820616", "survey_name" : "Thoughts on Dogs", "available_places" : 15, "user_id" : "5438"},
                            { "survey_id" : "292284", "survey_name" : "Opinions about Trees", "available_places" : 30, "user_id" : "2483"}]

    @patch('Survey_API.run.get_all_surveys')
    def test_route_returns_list_of_surveys_when_surveys_in_database(self, mock_all):
        mock_all.return_value = self.all_surveys
        result = self.app.get('/surveys')
        self.assertEquals(result.status_code, 200)

    @patch('Survey_API.run.SurveyBuilder.build')
    @patch('Survey_API.run.Survey.create_survey')
    @patch('Survey_API.run.Survey')
    def test_route_creates_new_survey_and_adds_it_to_the_database(self, mock_survey, mock_create, mock_build):
        mock_build.return_value = Mock()
        mock_create.return_value = True
        mock_survey = Mock()
        mock_id = PropertyMock(return_value='123456')
        type(mock_survey).survey_id = mock_id
        result = self.app.post('/surveys', json=self.new_survey_data)
        self.assertEquals(result.status_code, 200)

    @patch('Survey_API.run.SurveyResponse.create_survey_response')
    def test_route_checks_available_places_for_survey_response_and_creates_new_response_if_places_available(self, mock_create):
        mock_create.return_value = True
        result = self.app.post('/survey_responses', json=self.survey_response_fail)
        print('response result', result.data)
        self.assertEquals(result.status_code, 200)


    # def test_again_route_creates_new_survey_and_adds_it_to_the_database(self):
    #     result = self.app.post('/surveys', json=self.new_survey_data)
    #     print('second result', result.data)
    #     self.assertEquals(result.status_code, 200)

    # def test_again_route_returns_list_of_surveys_when_surveys_in_database(self):
    #     result = self.app.get('/surveys')
    #     print('all results: ', result.data)
    #     self.assertEquals(result.status_code, 200)