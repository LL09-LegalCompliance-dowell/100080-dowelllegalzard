import requests
import json
from datetime import datetime

# DO NOT CHANGE THE CONSTANTS
# COLLECTIONS
SOFTWARE_AGREEMENT_COLLECTION = "agreement"
SOFTWARE_LICENSE_COLLECTION = "agreement"
COMMON_ATTRIBUTE_COLLECTION = "common_attributes"
ATTRIBUTE_COLLECTION = "attributes"
LICENSE_TYPE_COLLECTION = "license_types"

# DOCUMENTS
SOFTWARE_AGREEMENT_DOCUMENT_NAME = "agreements"
SOFTWARE_LICENSE_DOCUMENT_NAME = "agreements"
COMMON_ATTRIBUTE_DOCUMENT_NAME = "common_attribute"
ATTRIBUTE_DOCUMENT_NAME = "attribute"
LICENSE_TYPE_DOCUMENT_NAME = "license_type"

# DOCUMENT KEY
SOFTWARE_AGREEMENT_KEY = "agreement"
SOFTWARE_LICENSE_KEY = "agreement"
COMMON_ATTRIBUTE_KEY = "common_attribute"
ATTRIBUTE_MAIN_KEY = "attribute"
LICENSE_MAIN_KEY = "license_type"

# SERVER
DATABASE = "license"
CLUSTER = "license"



def get_event_id():
    dd=datetime.now()
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
    url="https://100003.pythonanywhere.com/event_creation"

    data={
        "platformcode":"FB" ,
        "citycode":"101",
        "daycode":"0",
        "dbcode":"pfm" ,
        "ip_address":"192.168.0.41",
        "login_id":"lav",
        "session_id":"new",
        "processcode":"1",
        "regional_time":time,
        "dowell_time":time,
        "location":"22446576",
        "objectcode":"1",
        "instancecode":"100051",
        "context":"afdafa ",
        "document_id":"3004",
        "rules":"some rules",
        "status":"work",
        "data_type": "learn",
        "purpose_of_usage": "add",
        "colour":"color value",
        "hashtags":"hash tag alue",
        "mentions":"mentions value",
        "emojis":"emojis",

    }


    r=requests.post(url,json=data)
    return r.text



def save_document(
    collection:str,
    document:str,
    key:str,
    value:dict,
    ):
    url = "http://100002.pythonanywhere.com/"

    # Build request data or payload
    payload = json.dumps({
        "cluster": CLUSTER,
        "database": DATABASE,
        "collection": collection,
        "document": document,
        "team_member_ID": "10008002",
        "function_ID": "ABCDE",
        "command": "insert",
        "field": {
            "eventId" : get_event_id(),
            key : value
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
    collection:str,
    document:str,
    key:str,
    new_value:dict,
    id
    ):
    url = "http://100002.pythonanywhere.com/"

    # Build request data or payload
    payload = json.dumps({
        "cluster": CLUSTER,
        "database": DATABASE,
        "collection": collection,
        "document": document,
        "team_member_ID": "10008002",
        "function_ID": "ABCDE",
        "command": "update",
        "field": {
            '_id': id
            },
        "update_field": {key:new_value}, 
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
    collection:str,
    document:str,
    fields:dict,
    ):
    url = "http://100002.pythonanywhere.com/" 

    # Build request data or payload
    payload = json.dumps({
        "cluster": CLUSTER,
        "database": DATABASE,
        "collection": collection,
        "document": document,
        "team_member_ID": "10008002",
        "function_ID": "ABCDE",
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
    distribution_input={
        'normal': 1,
        'poisson':0,
        'binomial':0,
        'bernoulli':0
    }

    request_data={
        'database_details': database_details,
        'distribution_input': distribution_input,
        'number_of_variable':number_of_variables,
        'stages':stage_input_list,
        'time_input':time_input,
    }

    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=request_data,headers=headers)
    return response.text

new_data = {
    "software_name": "APACHE",
    "license_name": "APACHE 2.0",
    "version": "2.0",
    "type_of_license": "PERMISSIVE",

    "description": "The 2.0 version of the Apache License, approved by the ASF in 2004, All packages produced by the ASF are implicitly licensed under the Apache License, Version 2.0, unless otherwise explicitly stated.",

    "disclaimer": "Copyright [yyyy] [name of copyright owner] Licensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",

    "risk_for_choosing_license": "One thing to consider is that you cannot combine Apache",

    "limitation_of_liability": "In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.",

    "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
    "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
    "recommendation": "2.0",
    "released_date": "2022-05-10",
    "license_attributes": [],
    "license_compatibility": [],
    "license_compatible_with_lookup": [],
    "license_not_compatible_with_lookup": []
}


update_data = {
    "software_name": "APACHE",
    "license_name": "APACHE 2.0",
    "version": "2.0",
    "type_of_license": "PERMISSIVE",

    "description": "The 2.0 version of the Apache License, approved by the ASF in 2004, All packages produced by the ASF are implicitly licensed under the Apache License, Version 2.0, unless otherwise explicitly stated.",

    "disclaimer": "Copyright [yyyy] [name of copyright owner] Licensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",

    "risk_for_choosing_license": "One thing to consider is that you cannot combine Apache",

    "limitation_of_liability": "In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.",

    "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
    "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
    "recommendation": "2.0",
    "released_date": "2022-05-10",
    "license_attributes": [],
    "license_compatibility": [],
    "license_compatible_with_lookup": ["APACHE 2.0"],
    "license_not_compatible_with_lookup": []
}


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
