from survey_api.db import number_available_places, number_survey_responses

class SurveyResponse():

    def __init__(self, survey_id=None, user_id=None):
        self.survey_id = survey_id
        self.user_id = user_id

    def to_dict(self):
        return {'survey_id': self.survey_id,
                'user_id': self.user_id
            }

    def add_survey_response(self):
        avail_places = number_available_places(self.survey_id)
        no_responses = number_survey_responses(self.survey_id)
        remaining_places = avail_places - no_responses
        if remaining_places > 0:
            self.create_survey_response
            return {'response': 'success'}
        else:
            message = f'No available places for survey {self.survey_id}'
            return {'reponse': 'fail', 'error':message}


    def create_survey_response(self):
        result = add_survey()
        if result['result'] == 'success':
            return True
        return False