import requests

"""DoWell Product Experienced Service"""
def experience_database_services(email, occurrences):
    url = "https://100105.pythonanywhere.com/api/v3/experience_database_services/?type=experienced_service_user_details"
    payload = {
        "email":email,
        "product_number":"UXLIVINGLAB003",
        "occurrences":occurrences
    }
    response = requests.post(url, json=payload)
    response_json = response.json()
    if not response_json['success']:
        print('Register User Here: ')
        register_url = "https://100105.pythonanywhere.com/api/v3/experience_database_services/?type=register_user"
        register_payload = {
            "email":email,
            "product_number":"UXLIVINGLAB003",
        }
        register_response = requests.post(register_url, json=register_payload)
        register_response_json = register_response.json()
        print(register_response_json)
        return register_response.text
    else:
        return response.text


def save_experienced_product_data(product_name,email,experienced_data):
    url = "https://100105.pythonanywhere.com/api/v3/experience_database_services/?type=experienced_user_details"
    payload = {
        "product_name": product_name,
        "email": email,
        "experienced_data": experienced_data
    }
    response = requests.post(url, json=payload)
    # print("this is ok ",response.status_code)
    # print("this is ok ",response.text)
    return response.text


def update_user_usage(email, occurrences):
    url = f"https://100105.pythonanywhere.com//api/v3/experience_database_services/?type=update_user_usage&product_number=UXLIVINGLAB003&email={email}&occurrences={occurrences}"
    response = requests.get(url)
    # print("this is ok ",response.status_code)
    # print("this is ok ",response.text)
   
    return response.text