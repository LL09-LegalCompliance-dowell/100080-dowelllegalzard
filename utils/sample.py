import requests
import json
from datetime import datetime


def get_event_id():
    dd = datetime.now()
    time = dd.strftime("%d:%m:%Y,%H:%M:%S")
    url = "https://100003.pythonanywhere.com/event_creation"

    data = {
        "platformcode": "FB",
        "citycode": "101",
        "daycode": "0",
        "dbcode": "pfm",
        "ip_address": "192.168.0.41",
        "login_id": "lav",
        "session_id": "new",
        "processcode": "1",
        "regional_time": time,
        "dowell_time": time,
        "location": "22446576",
        "objectcode": "1",
        "instancecode": "100051",
        "context": "afdafa ",
        "document_id": "3004",
        "rules": "some rules",
        "status": "work",
        "data_type": "learn",
        "purpose_of_usage": "add",
        "colour": "color value",
        "hashtags": "hash tag alue",
        "mentions": "mentions value",
        "emojis": "emojis",

    }

    r = requests.post(url, json=data)
    return r.text


def save_licenses():  # license
    url = "http://uxlivinglab.pythonanywhere.com"
    agreement = {
        "name": "Worlako vs George",
        "title": "License agreement",
        "test": "This is just a test agreement"
    }
    # searchstring="ObjectId"+"("+"'"+"6139bd4969b0c91866e40551"+"'"+")"
    payload = json.dumps({
        "cluster": "license",
        "database": "license",
        "collection": "agreement",
        "document": "agreements",
        "team_member_ID": "10008002",
        "function_ID": "ABCDE",
        "command": "insert",
        "field": {
            "eventId": get_event_id(),
            "agreement": agreement
        },
        "update_field": {
            "order_nos": 21
        },
        "platform": "bangalore"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.json())


save_licenses()


def targeted_population(database, collection, fields, period):
    url = 'http://100032.pythonanywhere.com/api/targeted_population/'
    database_details = {
        'database_name': 'mongodb',
        'collection': collection,
        'database': database,
        'fields': fields
    }
    # number of variables for sampling rule
    number_of_variables = -1

    """
        period can be 'custom' or 'last_1_day' or 'last_30_days' or 'last_90_days' or 'last_180_days' or 'last_1_year' or 'life_time'
        if custom is given then need to specify start_point and end_point
        for others datatpe 'm_or_A_selction' can be 'maximum_point' or 'population_average'
        the the value of that selection in 'm_or_A_value'
        error is the error allowed in percentage
    """
    time_input = {
        'column_name': 'Date',
        'split': 'week',
        'period': period,
        'start_point': '2021/01/08',
        'end_point': '2021/01/25',
    }

    stage_input_list = [
    ]

    # distribution input
    distribution_input = {
        'normal': 1,
        'poisson': 0,
        'binomial': 0,
        'bernoulli': 0
    }

    request_data = {
        'database_details': database_details,
        'distribution_input': distribution_input,
        'number_of_variable': number_of_variables,
        'stages': stage_input_list,
        'time_input': time_input,
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=request_data, headers=headers)
    return response.text

# response = targeted_population('license','agreement',  ['full_name'], 'life_time')
# print(response)
