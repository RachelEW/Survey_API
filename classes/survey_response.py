from Survey_API.db import number_available_places, number_survey_responses, add_survey_response

class SurveyResponse():

    def __init__(self, survey_id=None, user_id=None, created_at=None):
        self.survey_id = survey_id
        self.user_id = user_id
        self.created_at = created_at

    def to_dict(self):
        return {'survey_id': self.survey_id,
                'user_id': self.user_id,
                'created_at': self.created_at
            }

    def create_survey_response(self):
        avail_places = number_available_places(self.survey_id)
        no_responses = number_survey_responses(self.survey_id)
        remaining_places = avail_places - no_responses
        if remaining_places > 0:
            response_data = self.to_dict()
            add_survey_response(response_data)
            return {'status': 'success'}
        else:
            message = f'No available places for survey {self.survey_id}'
            return {'status': 'fail', 'error':message}
