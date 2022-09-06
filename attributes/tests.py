from django.test import TestCase
import requests

# Create your tests here.


class AttributeTestCase(TestCase):
    def setUp(self) -> None:
        self.new_common_attribute = {
            "name": "sample 1",
            "code": "sample_code_1"
        }

        self.update_common_attribute = {
            "name": "sample 1",
            "code": "sample_code_12"
        }

        self.new_attribute = {
            "name": "Conveying Modified Source Versions",
            "common_attribute": {
                "_id": "63146d2799c608329b7146ed",
                "eventId": "FB1010000000166228304251473167",
                "name": "sample 2",
                "code": "sample_code_12"
            }
        }
        self.update_attribute = {
            "name": "Conveying Modified Source Versions",
            "common_attribute": {
                "_id": "63146f1699c608329b714706",
                "eventId": "FB1010000000166228353751007912",
                "name": "sample 1",
                "code": "sample_code_1"
            }
        }

        self.client = requests

    def test_get_common_attributes(self):
        res = self.client.get('http://127.0.0.1:8000/api/commonattributes/')
        jsonData = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(jsonData['isSuccess'])

    def _test_create_common_attributes(self):
        res = self.client.post(
            'http://127.0.0.1:8000/api/commonattributes/',
            data=self.new_common_attribute,
            # content_type="application/json"
        )
        jsonData = res.json()

        self.assertEqual(res.status_code, 201)
        self.assertTrue(jsonData['isSuccess'])

    def test_get_common_attribute(self):
        res = self.client.get(
            'http://127.0.0.1:8000/api/commonattributes/FB1010000000166228304251473167/')
        jsonData = res.json()
        data = jsonData['data']

        self.assertEqual(res.status_code, 200)
        self.assertTrue(jsonData['isSuccess'])
        self.assertTrue(data[0]['common_attributes'])

    def test_update_common_attributes(self):
        res = self.client.put(
            'http://127.0.0.1:8000/api/commonattributes/FB1010000000166228304251473167/',
            data=self.update_common_attribute,
            # content_type="application/json"
        )
        jsonData = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(jsonData['isSuccess'])

    def test_get_attributes(self):
        res = self.client.get('http://127.0.0.1:8000/api/attributes/')
        jsonData = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(jsonData['isSuccess'])

    def _test_create_attributes(self):
        res = self.client.post(
            'http://127.0.0.1:8000/api/attributes/',
            data=self.new_attribute,
            # content_type="application/json"
        )
        jsonData = res.json()

        self.assertEqual(res.status_code, 201)
        self.assertTrue(jsonData['isSuccess'])

    def test_get_attribute(self):
        res = self.client.get(
            'http://127.0.0.1:8000/api/attributes/FB1010000000166229342959770951/')
        jsonData = res.json()
        data = jsonData['data']

        self.assertEqual(res.status_code, 200)
        self.assertTrue(jsonData['isSuccess'])
        self.assertTrue(data[0]['attributes'])

    def _test_update_attributes(self):
        res = self.client.put(
            'http://127.0.0.1:8000/api/attributes/FB1010000000166229342959770951/',
            data=self.update_attribute,
        )
        jsonData = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(jsonData['isSuccess'])
