from flask import Flask, request
from Survey_API.db import connect_db, get_all_surveys, add_survey, number_survey_responses, number_available_places

import json
from datetime import datetime

from Survey_API.classes.survey import SurveyBuilder, Survey
from Survey_API.classes.survey_response import SurveyResponse

app = Flask(__name__)
# app.config.from_object(Config)
app.config['SECRET_KEY'] = 'development'
app.config['MONGO_URI'] = connect_db()


@app.route('/surveys', methods=['GET'])
def all_surveys():
    results = get_all_surveys()
    if isinstance(results, list):
        return json.dumps({'status': 'ok', 'data': results}), 200
    return json.dumps({'status': 'ok', 'data':'No surveys in database'}), 200

@app.route('/surveys', methods=['POST'])
def create_survey():
    survey_data = request.json
    survey_build = SurveyBuilder(survey_name=survey_data['survey_name'], available_places=survey_data['available_places'], user_id=survey_data['user_id'])
    new_survey = survey_build.build()
    result = new_survey.create_survey()
    if result:
        message = f'Survey successfully created with survey ID {new_survey.survey_id}'
        return json.dumps({'status': 'ok', 'data': message}), 200
    return json.dumps({'status': 'fail', 'data': 'could not create new survey'}), 400

@app.route('/survey_responses', methods=['POST'])
def create_survey_response():
    survey_resp_data = request.json
    timestamp = datetime.utcnow()
    new_survey_response = SurveyResponse(survey_id=survey_resp_data['survey_id'], user_id=survey_resp_data['user_id'], created_at=timestamp)
    result = new_survey_response.create_survey_response()
    if result['status'] == 'ok':
        return json.dumps({'status': 'ok', 'data': 'survey response created'}), 200
    return json.dumps({'status': 'fail', 'error':'Could not create survey response, maximum number of participants exceeded'}), 400


if __name__ == "__main__":
    app.run(debug=True)