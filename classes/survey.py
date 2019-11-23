import random

class SurveyBuilder():

    def __init__(self, survey_name=None, available_places=None, user_id=None):
        self.survey_name = survey_name
        self.available_places = available_places
        self.user_id = user_id

    def builder_dict():
        return {'survey_name': self.survey_name,
                'available_places': self.available_places,
                'user_id': self.user_id
                }
    
    def generate_unique_id():
        survey_id = random.randint(1, 999999)

    def check_duplicate():
        pass



class Survey():

    def __init__(self, survey_id=None, survey_name=None, available_places=None, user_id=None):
        survey_id = self.survey_id