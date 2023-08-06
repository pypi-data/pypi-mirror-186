import json, jsonschema, os
from bson.objectid import ObjectId
from datetime import datetime

baseVal = jsonschema.Draft7Validator

def is_datetime(checker, inst):
    return isinstance(inst, datetime)

def is_objectId(checker, inst):
    return isinstance(inst, ObjectId)

TYPE_CHECKER = baseVal.TYPE_CHECKER.redefine_many({
    "datetime": is_datetime,
    "objectId": is_objectId
})


Validator = jsonschema.validators.extend(baseVal, type_checker=TYPE_CHECKER)

def get_validator(schema):
    return Validator(schema=schema)
