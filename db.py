import random
import pymongo
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, PyMongoError

def connect_db():
    try:
        MONGO_URI = 'mongodb://localhost:27017/survey_api'
        client = MongoClient(MONGO_URI)
        db = client.survey_api
        return db
    except ServerSelectionTimeoutError as exc:
        return {'data':'could not connect to database, server timed out'}
    except PyMongoError as err:
        message = f'could not connect to database, pymongo error occured {err}'
        return {'data': message}

def get_all_surveys():
    db = connect_db()
    all_surveys = list(db.surveys.find({}, {'_id': 0}))
    return all_surveys

def add_survey(survey_data):
    db = connect_db()
    response = db.surveys.insert_one(survey_data)
    if response['acknowledged']:
        return {'result':'success'}
    return {'result': 'fail'}

def add_survey_response(response_data):
    db = connect_db()
    response = db.survey_responses.insert_one(response_data)
    if response['acknowledged']:
        return {'result':'success'}
    return {'result': 'fail'}

def number_survey_responses(survey_id):
    db = connect_db()
    number_responses = db.survey_responses.count_documents({'survey_id': survey_id})
    return number_responses

def number_available_places(survey_id):
    db = connect_db()
    number_avail_places = db.survey_responses.find({'survey_id': survey_id}, {'available_places': 1})
    return number_avail_places

def survey_builder_assign_id(survey_builder_dict):
    db = connect_db()
    survey_id = random.randint(1, 999999)
    unique = False
    while not unique:
        matching_docs = db.surveys.count_documents({'survey_id': survey_id})
        if matching_docs != 0:
            unique = True
    return survey_id