from flask import Flask, request, jsonify
from survey_api.db import connect_db, get_all_surveys, add_survey

from survey_api.classes.survey import Survey
from survey_api.classes.survey_response import SurveyResponse

app = Flask(__name__)
# app.config.from_object(Config)
app.config['SECRET_KEY'] = 'development'
app.config['MONGO_URI'] = connect_db()


@app.route('/survey_api/surveys', methods=['GET'])
def all_surveys():
    results = get_all_surveys()
    if isInstance(results, list):
        return jsonify({'status': 'ok', 'data': results}), 200
    return jsonify({'status': 'ok', 'data':'No surveys in database'}), 200

@app.route('/survey_api/surveys', methods=['POST'])
def create_survey():
    return jsonify({}), 200

@app.route('/survey_api/survey_responses', methods=['POST'])
def create_survey_response():
    return jsonify({}), 200


if __name__ == "__main__":
    app.run(debug=True)