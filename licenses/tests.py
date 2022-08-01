import json
from django.test import TestCase, Client
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent



class LicensesTest(TestCase):

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

        # initialize web client object
        self.client = Client()


    def add_new_software_license(self):
        # Create license
        return self.client.post(
            '/api/licenses/',
            self.fixture['add_license_data'],
            content_type="application/json"
            )

    

    def test_add_software_license(self):
        # Create license
        response = self.add_new_software_license()
        self.assertEqual(response.status_code, 201)

        json_data = response.json()["license"]
        self.assertEqual(json_data['software_name'], 'GNU GPL v 2.0')



    def test_retrieve_license(self):
        # Create license
        response = self.add_new_software_license()
        self.assertEqual(response.status_code, 201)
        json_data = response.json()["license"]

        # Retrieve license
        response = self.client.get(f'/api/licenses/{json_data["license_id"]}/')
        self.assertEqual(response.status_code, 200)

        json_data = response.json()["license"]
        self.assertEqual(json_data['software_name'], 'GNU GPL v 2.0')



    def test_retrieve_all_license(self):
        # Create license
        response = self.add_new_software_license()
        self.assertEqual(response.status_code, 201)

        # Retrieve all license
        response = self.client.get(f'/api/licenses/')

        json_data_list = response.json()["licenses"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_data_list), 1)
    

    def test_update_license(self):
        # Create license
        response = self.add_new_software_license()
        self.assertEqual(response.status_code, 201)
        json_data = response.json()["license"]

        # Update license
        response = self.client.put(
            f'/api/licenses/{json_data["license_id"]}/',
            self.fixture['update_license_data'],
            content_type='application/json'
            )

        self.assertEqual(response.status_code, 200)
        json_data = response.json()["license"]
        self.assertEqual(json_data['software_name'], 'GNU GPL v 2.2')


    def test_delete_license(self):
        # Create license
        response = self.add_new_software_license()
        self.assertEqual(response.status_code, 201)
        json_data = response.json()["license"]

        # Delete license
        response = self.client.delete(
            f'/api/licenses/{json_data["license_id"]}/'
            )

        self.assertEqual(response.status_code, 204)

