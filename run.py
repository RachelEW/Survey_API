from flask import Flask, request
from survey_api.db import connect_db, get_all_surveys, add_survey, number_survey_responses, number_available_places
import json

from survey_api.classes.survey import SurveyBuilder, Survey
from survey_api.classes.survey_response import SurveyResponse

app = Flask(__name__)
# app.config.from_object(Config)
app.config['SECRET_KEY'] = 'development'
app.config['MONGO_URI'] = connect_db()


@app.route('/survey_api/v1/surveys', methods=['GET'])
def all_surveys():
    results = get_all_surveys()
    if isinstance(results, list):
        return json.dumps({'status': 'ok', 'data': results}), 200
    return json.dumps({'status': 'ok', 'data':'No surveys in database'}), 200

@app.route('/survey_api/v1/surveys', methods=['POST'])
def create_survey():
    survey_data = request.json
    new_survey_builder = SurveyBuilder(survey_name=survey_data['survey_name'], available_places=survey_data['available_places'], user_id=survey_data['user_id'])
    new_survey_builder.create_unique_id()
    new_survey = new_survey.build()
    return json.dumps({}), 200

@app.route('/survey_api/v1/survey_responses', methods=['POST'])
def create_survey_response():
    return json.dumps({}), 200


if __name__ == "__main__":
    app.run(debug=True)