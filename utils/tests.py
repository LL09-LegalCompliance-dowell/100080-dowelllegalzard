import requests


def search_license(search_term):
    response = requests.get(f'https://100080.pythonanywhere.com/api/licenses/?search_term={search_term}&action_type=search')
    license_data = response.json()['data'][0]
    print("Event ID", license_data['eventId'])
    return license_data['eventId']


def check_compatibility(event1, event2):
    api_url = "https://100080.pythonanywhere.com/api/licenses/"
    json_payload = {
    "action_type": "check-compatibility",
    "license_event_id_one": event1,
    "license_event_id_two": event2,
    }
    response = requests.post(api_url, json=json_payload)
    is_compatible = response.json()['is_compatible']
    percentage_of_compatibility = response.json()['percentage_of_compatibility']
    print("is_compatible: ", is_compatible)
    print("percentage_of_compatibility: ", percentage_of_compatibility)
    return is_compatible

#search_license('mit')
# check_compatibility('FB1010000000168019792755266733', 'FB1010000000167644773552170851')

def test_bot():
    package_license_ids = {'BSD-3-Clause', 'BSD-2-Clause'}
    spdx_request = requests.get("https://spdx.org/licenses/licenses.json")
    repo_license_event_id = search_license('MIT')
    #  initialize issues
    incompatible_licenses = ""
    truth = False
    # run comparison with package licenses
    for license_id in package_license_ids:
        try:
            # get license
            license_event_id = search_license(license_id)
            compatibility = check_compatibility(repo_license_event_id, license_event_id)
            # skip compatible licenses
            if compatibility:
                print("Is compatible")
                continue
            # log incompatible licenses
            incompatible_licenses += f"{license_name}\n"
        except Exception as e:
            print(e)
            pass
test_bot()