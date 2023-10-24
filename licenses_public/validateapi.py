import requests

def validateApikey(api_key):
    url = "https://100105.pythonanywhere.com/api/v3/process-services/?type=api_service&api_key="+api_key
    # url = 'https://100105.pythonanywhere.com/api/v1/process-api-key/'
    payload = {
        "service_id" : "DOWELL10022"
    }

    response = requests.post(url, json=payload)
    return response.text