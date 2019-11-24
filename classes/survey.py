from survey_api.db import survey_builder_assign_id, add_survey

class SurveyBuilder():

    def __init__(self, survey_name=None, available_places=None, user_id=None):
        self.survey_name = survey_name
        self.available_places = available_places
        self.user_id = user_id

    def build(self):
        self.survey_id = survey_builder_assign_id()
        return Survey(self.survey_id, self.survey_name, self.available_places, self.user_id)


class Survey():

    def __init__(self, survey_id=None, survey_name=None, available_places=None, user_id=None):
        self.survey_id = survey_id
        self.survey_name = survey_name
        self.available_places = available_places
        self.user_id = user_id

    def to_dict(self):
        return {'survey_id': self.survey_id,
                'survey_name': self.survey_name,
                'available_places': self.available_places,
                'user_id': self.user_id,
            }

    def create_survey(self):
        survey_data = self.to_dict()
        result = add_survey(survey_data)
        if result['result'] == 'success':
            return True
        return False
