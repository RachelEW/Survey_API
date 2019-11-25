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
        message = f'could not connect to database, server timed out, exception raised {exc}'
        return {'data': message}
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
    if response.insertedId is not None:
        return {'result':'success'}
    return {'result': 'fail'}

def add_survey_response(response_data):
    db = connect_db()
    response = db.survey_responses.insert_one(response_data)
    if response.insertedId is not None:
        return {'result':'success'}
    return {'result': 'fail'}

def number_survey_responses(survey_id):
    db = connect_db()
    number_responses = db.survey_responses.count_documents({'survey_id': survey_id})
    return number_responses

def number_available_places(survey_id):
    db = connect_db()
    avail_places_dict = db.surveys.find({'survey_id': survey_id}, {'available_places': 1, '_id': 0})
    number_avail_places = avail_places_dict['available_places']
    return number_avail_places

def survey_builder_assign_id():
    db = connect_db()
    unique = False
    while not unique:
        survey_id = random.randint(1, 999999)
        matching_doc = db.surveys.find_one({'survey_id': survey_id})
        if matching_doc == None:
            unique = True
    return survey_id