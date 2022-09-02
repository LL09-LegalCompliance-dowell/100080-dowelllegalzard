import requests
import json
from datetime import datetime

# DO NOT CHANGE THE CONSTANTS
# COLLECTIONS
SOFTWARE_AGREEMENT_COLLECTION = "agreement"
SOFTWARE_LICENSE_COLLECTION = "softwarelicenses"
COMMON_ATTRIBUTE_COLLECTION = "common_attributes"
ATTRIBUTE_COLLECTION = "attributes"
LICENSE_TYPE_COLLECTION = "license_types"

# DOCUMENTS
SOFTWARE_AGREEMENT_DOCUMENT_NAME = "agreements"
SOFTWARE_LICENSE_DOCUMENT_NAME = "softwarelicense"
COMMON_ATTRIBUTE_DOCUMENT_NAME = "common_attribute"
ATTRIBUTE_DOCUMENT_NAME = "attribute"
LICENSE_TYPE_DOCUMENT_NAME = "license_type"

# DOCUMENT KEY
SOFTWARE_AGREEMENT_KEY = "agreement"
SOFTWARE_LICENSE_KEY = "softwarelicense"
COMMON_ATTRIBUTE_KEY = "common_attribute"
ATTRIBUTE_MAIN_KEY = "attribute"
LICENSE_MAIN_KEY = "license_type"

# TEAM ID
SOFTWARE_AGREEMENT_TEAM_ID = "10008002"
SOFTWARE_LICENSE_TEAM_ID = "10008001"
# COMMON_ATTRIBUTE_TEAM_ID = ""
# ATTRIBUTE_MAIN_TEAM_ID = ""
# LICENSE_MAIN_TEAM_ID = ""

# FUNCTION ID
SOFTWARE_AGREEMENT_FUNC_ID = "ABCDE"
SOFTWARE_LICENSE_FUNC_ID = "ABCDE"
# COMMON_ATTRIBUTE_FUNC_ID = ""
# ATTRIBUTE_MAIN_FUNC_ID = ""
# LICENSE_MAIN_FUNC_ID = ""

# SERVER
DATABASE = "license"
CLUSTER = "license"

# RECORD LOAD
RECORD_PER_PAGE = 10


def format_id(id):
    return f"ObjectId"+"("+"'{id}'"+")"


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


def save_document(
    collection: str,
    document: str,
    key: str,
    value: dict,
):
    url = "http://100002.pythonanywhere.com/"

    # Build request data or payload
    payload = json.dumps({
        "cluster": CLUSTER,
        "database": DATABASE,
        "collection": collection,
        "document": document,
        "team_member_ID": get_team_id(collection),
        "function_ID": get_function_id(collection),
        "command": "insert",
        "field": {
            "eventId": get_event_id(),
            key: value
        },
        "update_field": {"update_field": "nil"},
        "platform": "bangalore"
    })

    # Setup request headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Send POST request to server
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def update_document(
    collection: str,
    document: str,
    key: str,
    new_value: dict,
    id="",
    license_name=""
):
    url = "http://100002.pythonanywhere.com/"

    # Build request data or payload
    payload = json.dumps({
        "cluster": CLUSTER,
        "database": DATABASE,
        "collection": collection,
        "document": document,
        "team_member_ID": get_team_id(collection),
        "function_ID": get_function_id(collection),
        "command": "update",
        "field": {
            "softwarelicense.license_name": license_name
            # '_id': id
        },
        "update_field": {key: new_value},
        "platform": "bangalore"
    })

    # Setup request headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Send POST request to server
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def fetch_document(
    collection: str,
    document: str,
    fields: dict,
):
    url = "http://100002.pythonanywhere.com/"

    # Build request data or payload
    payload = json.dumps({
        "cluster": CLUSTER,
        "database": DATABASE,
        "collection": collection,
        "document": document,
        "team_member_ID": get_team_id(collection),
        "function_ID": get_function_id(collection),
        "command": "fetch",
        "field": fields,

        "update_field": {"update_field": "nil"},
        "platform": "bangalore"

    })

    # Setup request headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Send POST request to server
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.content)
    return response.json()


def targeted_population(collection, fields, period):

    url = 'http://100032.pythonanywhere.com/api/targeted_population/'
    database_details = {
        'database_name': 'mongodb',
        'collection': collection,
        'database': DATABASE,
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


def get_team_id(collection):
    team_id = ""

    if collection == SOFTWARE_AGREEMENT_COLLECTION:
        team_id = SOFTWARE_AGREEMENT_TEAM_ID
    elif collection == SOFTWARE_LICENSE_COLLECTION:
        team_id = SOFTWARE_LICENSE_TEAM_ID

    return team_id


def get_function_id(collection):
    func_id = ""

    if collection == SOFTWARE_AGREEMENT_COLLECTION:
        func_id = SOFTWARE_AGREEMENT_FUNC_ID
    elif collection == SOFTWARE_LICENSE_COLLECTION:
        func_id = SOFTWARE_LICENSE_FUNC_ID

    return func_id


if __name__ == "__main__":
    pass

    # print(save_document(
    #     collection=SOFTWARE_LICENSE_COLLECTION,
    #     document=SOFTWARE_LICENSE_DOCUMENT_NAME,
    #     key=SOFTWARE_LICENSE_KEY,
    #     value=new_data
    #     ))

    # print(update_document(
    #     collection=SOFTWARE_LICENSE_COLLECTION,
    #     document=SOFTWARE_LICENSE_DOCUMENT_NAME,
    #     key=SOFTWARE_LICENSE_KEY,
    #     new_value=update_data,
    #     id="62f63a4efaaff8a49caf4ba1"
    #     ))

    # print(fetch_document(
    #     collection=SOFTWARE_LICENSE_COLLECTION,
    #     document=SOFTWARE_LICENSE_DOCUMENT_NAME,
    #     fields={"_id": "62f63a4efaaff8a49caf4ba1"}
    #     ))
