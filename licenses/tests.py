import json
from pathlib import Path
import os
from django.test import TestCase
import requests

BASE_DIR = Path(__file__).resolve().parent.parent


class LicensesTestCase():

    def setUp(self) -> None:
        # format file path
        file_path = os.path.join(
            os.path.join(BASE_DIR, 'fixtures'),
            'data.json'
        )

        # load json data payload
        with open(file_path) as file:
            self.fixture = json.load(file)

        # initialize web client object
        self.client = requests

    def test_add_software_license(self):
        # Create license
        res = self.client.post(
            'http://127.0.0.1:8000/api/licenses/',
            self.fixture['add_license_data'],
            # content_type="application/json"
        )
        res = self.add_new_software_license()
        self.assertEqual(res.status_code, 201)

        json_data = res.json()
        data = json_data['data']
        softwarelicense = data[0]["softwarelicense"]

        self.assertEqual(softwarelicense['software_name'], 'APACHE')
        self.assertEqual(softwarelicense['license_name'], 'APACHE 2.0')

    def test_retrieve_license(self):
        # Retrieve license
        res = self.client.get(
            f'http://127.0.0.1:8000/api/licenses/{json_data["_id"]}/')
        self.assertEqual(res.status_code, 200)

        json_data = res.json()
        data = json_data['data']
        softwarelicense = data[0]["softwarelicense"]

        self.assertEqual(softwarelicense['software_name'], 'APACHE')
        self.assertEqual(softwarelicense['license_name'], 'APACHE 2.0')

    def test_retrieve_all_license(self):
        # Retrieve all license
        res = self.client.get(f'http://127.0.0.1:8000/api/licenses/')

        json_data = res.json()
        data = json_data['data']

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data))

    def test_update_license(self):
        # Update license
        res = self.client.put(
            f'http://127.0.0.1:8000/api/licenses/{json_data["_id"]}/',
            self.fixture['update_license_data'],
            # content_type='application/json'
        )

        self.assertEqual(res.status_code, 200)
        json_data = res.json()
        data = json_data['data']

        softwarelicense = data[0]["softwarelicense"]
        self.assertEqual(softwarelicense['version'], '2.1')
        self.assertEqual(softwarelicense['license_name'], 'APACHE 2.1')
