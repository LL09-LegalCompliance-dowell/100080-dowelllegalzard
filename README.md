# 100080-dowelllegalzard

## API Reference

### Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:8000/`, which is set as a proxy in the frontend configuration.

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "isSuccess": False,
    "error": 400,
    "message": "bad request"
}
```

The API will return three error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable

### Endpoints

#### GET /api/licenses/

- General:
  - Returns a list of software licenses objects, and success value
- Sample: `curl http://127.0.0.1:8000/api/licenses/` or open link in a browser

```{
    "isSuccess": true,
    "data": [

        {
            "_id": "62f6261530c60549604b8392",
            "eventId": "FB1010000000166029876850946178",
            "agreement": {
                "software_name": "Sample 1",
                "license_name": "LGPLv2.1",
                "version": "2.0",
                "type_of_license": "WEAKLY COPYLEFT",
                "description": "The 2.0 version of the Apache.",
                "disclaimer": "Copyright .",
                "risk_for_choosing_license": "One thing to consider is that you cannot combine Apache",
                "limitation_of_liability": "In no event and under no legal theory.",
                "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "recommendation": "2.0",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [],
                "license_compatibility": [],
                "license_compatible_with_lookup": [
                    "APACHE 2.0"
                ],
                "license_not_compatible_with_lookup": []
            }
        },
        {
            "_id": "62f640b91a2da145efa2e990",
            "eventId": "FB1010000000166030558754942381",
            "agreement": {
                "software_name": "Sample 2",
                "license_name": "GPLv2",
                "version": "2.0",
                "type_of_license": "STRONGLY COPYLEFT",
                "description": "The 2.0 version of the Apache.",
                "disclaimer": "Copyright .",
                "risk_for_choosing_license": "One thing to consider is that you cannot combine Apache",
                "limitation_of_liability": "In no event and under no legal theory.",
                "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "recommendation": "2.0",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [],
                "license_compatibility": [],
                "license_compatible_with_lookup": [
                    "APACHE 2.0"
                ],
                "license_not_compatible_with_lookup": []
            }
        },
        {
            "_id": "62f782a6f8a0224b84f5f280",
            "eventId": "FB1010000000166038799759333038",
            "agreement": {
                "software_name": "APACHE",
                "license_name": "APACHE 2.0",
                "version": "2.0",
                "type_of_license": "PERMISSIVE",
                "description": "The 2.0 version of the Apache License",
                "disclaimer": "Copyright",
                "risk_for_choosing_license": "One thing to consider is that you cannot combine Apache",
                "limitation_of_liability": "In no event and under no legal theory",
                "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "recommendation": "2.0",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [],
                "license_compatibility": [],
                "license_compatible_with_lookup": [],
                "license_not_compatible_with_lookup": []
            }
        }
    ]
}
```

#### POST /api/licenses/

- General:
  - Creates a new software license using the submitted json data, Returns the detail of the created license, success value, and event id.
- `curl http://127.0.0.1:8000/api/licenses/ -X POST -H "Content-Type: application/json" -d ' { "software_name": "Sample 2", "license_name": "GPLv2", "version": "2.0", "type_of_license": "STRONGLY COPYLEFT", "description": "The 2.0 version of the Apache.", "disclaimer": "Copyright .", "risk_for_choosing_license": "One thing to consider is that you cannot combine Apache", "limitation_of_liability": "In no event and under no legal theory.", "license_url": "https://www.apache.org/licenses/LICENSE-2.0", "image_url": "https://www.apache.org/licenses/LICENSE-2.0", "recommendation": "2.0", "released_date": "2022-05-10", "is_active": true, "license_attributes": [], "license_compatibility": [], "license_compatible_with_lookup": [ "APACHE 2.0" ], "license_not_compatible_with_lookup": [] }'`
- You can also open the link `http://127.0.0.1:8000/api/licenses/` in a browser and perform the post operation

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "62f6261530c60549604b8392",
            "eventId": "FB1010000000166029876850946178",
            "agreement": {
                "software_name": "Sample 1",
                "license_name": "LGPLv2.1",
                "version": "2.0",
                "type_of_license": "WEAKLY COPYLEFT",
                "description": "The 2.0 version of the Apache.",
                "disclaimer": "Copyright .",
                "risk_for_choosing_license": "One thing to consider is that you cannot combine Apache",
                "limitation_of_liability": "In no event and under no legal theory.",
                "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "recommendation": "2.0",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [],
                "license_compatibility": [],
                "license_compatible_with_lookup": [
                    "APACHE 2.0"
                ],
                "license_not_compatible_with_lookup": []
            }
        }
    ]
}
```

#### GET /api/licenses/{license_id}/

- General:
  - Returns a list of software licenses objects, and success value
- Sample: `curl http://127.0.0.1:8000/api/licenses/62f6261530c60549604b8392/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "62f6261530c60549604b8392",
            "eventId": "FB1010000000166029876850946178",
            "agreement": {
                "software_name": "Sample 1",
                "license_name": "LGPLv2.1",
                "version": "2.0",
                "type_of_license": "WEAKLY COPYLEFT",
                "description": "The 2.0 version of the Apache.",
                "disclaimer": "Copyright .",
                "risk_for_choosing_license": "One thing to consider is that you cannot combine Apache",
                "limitation_of_liability": "In no event and under no legal theory.",
                "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "recommendation": "2.0",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [],
                "license_compatibility": [],
                "license_compatible_with_lookup": [
                    "APACHE 2.0"
                ],
                "license_not_compatible_with_lookup": []
            }
        }
    ]
}
```

#### PUT /api/licenses/{license_id}/

- General:
  - Fully update the software license of the given ID if it exists. Returns the updated data, success value, to update the frontend.
- `curl http://127.0.0.1:8000/api/licenses/{62f6261530c60549604b8392}/ -X PUT -H "Content-Type: application/json" -d ' { "software_name": "Owner Solt", "license_name": "LGPLv3 or LGPLv3+", "version": "3.0", "type_of_license": "WEAKLY COPYLEFT", "description": "The 2.0 version of the Apache.", "disclaimer": "Copyright .", "risk_for_choosing_license": "One thing to consider is that you cannot combine Apache", "limitation_of_liability": "In no event and under no legal theory.", "license_url": "https://www.apache.org/licenses/LICENSE-2.0", "image_url": "https://www.apache.org/licenses/LICENSE-2.0", "recommendation": "2.0", "released_date": "2022-05-10", "is_active": true, "license_attributes": [], "license_compatibility": [], "license_compatible_with_lookup": [ "APACHE 2.0" ], "license_not_compatible_with_lookup": [] }'`

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "62f6261530c60549604b8392",
            "eventId": "FB1010000000166029876850946178",
            "agreement": {
                "software_name": "Sample 1",
                "license_name": "LGPLv2.1",
                "version": "2.0",
                "type_of_license": "WEAKLY COPYLEFT",
                "description": "The 2.0 version of the Apache.",
                "disclaimer": "Copyright .",
                "risk_for_choosing_license": "One thing to consider is that you cannot combine Apache",
                "limitation_of_liability": "In no event and under no legal theory.",
                "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "recommendation": "2.0",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [],
                "license_compatibility": [],
                "license_compatible_with_lookup": [
                    "APACHE 2.0"
                ],
                "license_not_compatible_with_lookup": []
            }
        }
    ]
}
```
