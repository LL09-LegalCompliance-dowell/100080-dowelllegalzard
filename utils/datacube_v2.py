import json
import requests

api_key = "1b834e07-c68b-4bf6-96dd-ab7cdc62f07f"
base_url = "https://www.dowelldatacube.uxlivinglab.online/db_api"
# base_url = "https://datacube.uxlivinglab.online/db_api/"
DATABASE_NAME = "legal_licensing"
COLLECTION_NAME = "software_licenses"
LIMIT = 10000


def datacube_data_insertion(api_key, database_name, collection_name, data):
    global base_url
    url = f"{base_url}/api/crud/"
    payload = {
        "api_key": api_key,
        "db_name": database_name,
        "coll_name": collection_name,
        "operation": "insert",
        "data": data,
    }

    print(payload)

    response = requests.post(url, json=payload)
    print(response.text)
    return response.text


def datacube_data_retrieval(api_key, database_name, collection_name, data, limit, offset):
    global base_url
    url = f"{base_url}/api/crud/"
    
    payload = {
        "api_key": api_key,
        "db_name": database_name,
        "coll_name": collection_name,
        "operation": "fetch",
        "filters": data,
        "limit": limit,
        "offset": offset,
    }

    response = requests.post(url, json=payload)
    return response.text


def datacube_data_update(api_key, database_name, collection_name, query, update_data):
    global base_url
    url = f"{base_url}/api/crud/"

    payload = {
        "api_key": api_key,
        "db_name": database_name,
        "coll_name": collection_name,
        "operation": "update",
        "query": query,
        "update_data": update_data,
    }

    response = requests.put(url, json=payload)
    return response.text


def datacube_data_delete(api_key, database_name, collection_name, query):
    global base_url
    url = f"{base_url}/api/crud/"

    payload = {
        "api_key": api_key,
        "db_name": database_name,
        "coll_name": collection_name,
        "operation": "delete",
        "query": query
    }
    response = requests.delete(url, json=payload)
    return response.text


def datacube_create_collection(api_key, database_name, collection_name):
    global base_url
    url = f"{base_url}/api/add_collection/"
    
    payload = {
        "api_key": api_key,
        "db_name": database_name,
        "coll_names": collection_name,
    }

    response = requests.post(url, json=payload)
    return response.text


def datacube_collection_retrieval(api_key, database_name):
    global base_url
    url = f"{base_url}/api/list_collections/"
    
    payload = {
        "api_key": api_key,
        "db_name": database_name,
    }
    response = requests.get(url, json=payload)
    return response.text


def datacube_create_database(
        api_key, database_name,
        num_collections,
		coll_names,
        num_documents,
		field_labels,
        num_fields
        ):
    global base_url
    url = f"{base_url}/api/create_database/"
    
    payload = {
        "api_key": api_key,
        "db_name": database_name,
        "num_collections": num_collections,
        "coll_names": coll_names,
        "num_documents": num_documents,
		"num_fields": num_fields,
		"field_labels": field_labels
    }
    response = requests.get(url, json=payload)
    return response.text