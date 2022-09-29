from django.test import TestCase
import requests

# Create your tests here.


class ContactUsTestCase(TestCase):
    def setUp(self) -> None:
        self.create_contact_us_data = {
            "first_name": "sample",
            "last_name": "sample 1",
            "email": "sample@sample.com",
            "phone_number": "000-000-0000",
            "message": "sample message"
        }

        self.client = requests

    def test_get_all_contact_us(self):
        res = self.client.get('http://127.0.0.1:8000/api/contacts/')
        jsonData = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(jsonData['isSuccess'])

    def _test_create_contact_us(self):
        res = self.client.post(
            'http://127.0.0.1:8000/api/contacts/',
            data=self.create_contact_us_data
        )
        jsonData = res.json()

        self.assertEqual(res.status_code, 201)
        self.assertTrue(jsonData['isSuccess'])

    def test_search_contact_us(self):
        res = self.client.get(
            'http://127.0.0.1:8000/api/contacts/?action_type=search&search_term=000-000-0000'
        )
        jsonData = res.json()

        self.assertEqual(res.status_code, 201)
        self.assertTrue(jsonData['isSuccess'])
