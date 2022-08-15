import json
import unittest
from pathlib import Path
import os
import requests
BASE_DIR = Path(__file__).resolve().parent.parent
global_id = ""



class LicensesTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

        # format file path
        # for cross platform compatability
        file_path = os.path.join(
            os.path.join(BASE_DIR, 'fixtures'),
            'data.json'
            )
        
        # load json data payload
        with open(file_path) as file:
            self.fixture = json.load(file)

        self.base_url = "http://127.0.0.1:8000/"

    def create_license(self):
        return requests.request(
            "POST",
            self.base_url+'api/licenses/',
            headers={'Content-Type': 'application/json'},
            data=self.fixture['add_license_data'])

    def test_add_software_license(self):
        res = self.create_license()
        self.assertEqual(res.status_code, 201)

        # get data
        data_json = res.json()
        print(data_json)
        data = data_json["data"]
        licence = data[0]["agreement"]

        self.assertTrue(data_json["isSuccess"])
        self.assertEqual(licence['software_name'], 'APACHE')
        self.assertEqual(licence['license_name'], 'APACHE 2.0')
        global_id = licence['_id']



    def _test_retrieve_license(self):

        # Retrieve license
        res = requests.request(
            "GET",
            f'{self.base_url}api/licenses/{global_id}/',
            headers={"Content-Type": "application/json"})

        # get data
        data_json = res.json()
        data = data_json["data"]
        licence = data[0]["agreement"]

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data_json["isSuccess"])
        self.assertEqual(licence['software_name'], 'APACHE')
        self.assertEqual(licence['license_name'], 'APACHE 2.0')



    def _test_retrieve_all_license(self):
        # Retrieve all license
        res = requests.request(
            "GET",
            f'{self.base_url}api/licenses/{global_id}/',
            headers={"Content-Type: application/json"})

        # get data
        data_json = res.json()
        data = data_json["data"]

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data_json["isSuccess"])
        self.assertTrue(len(data))
    

    def _test_update_license(self):
        # Update license
        res = requests.request(
            "PUT",
            f'{self.base_url}api/licenses/{global_id}',
            headers={"Content-Type": "application/json"},
            data=self.fixture['update_license_data'])

        # get data
        data_json = res.json()
        data = data_json["data"]
        licence = data[0]["agreement"]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(licence['version'], '2.1')
        self.assertEqual(licence['license_name'], 'APACHE 2.1')
        self.assertTrue(len(licence['license_compatible_with_lookup']))




if __name__ == "__main__":
    unittest.main()

