import requests

def validateApikey(api_key):
    url = 'https://100105.pythonanywhere.com/api/v1/process-api-key/'
    payload = {
        "api_key" : api_key,
        "api_service_id" : "DOWELL100013"
    }

    response = requests.post(url, json=payload)
    return response.text