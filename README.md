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

### Software License

#### GET /api/licenses/

- General:
  - Returns a list of software licenses objects, and success value
- Sample: `curl http://127.0.0.1:8000/api/licenses/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "63047b62b3a9611686cdcd56",
            "eventId": "FB1010000000166123810354118614",
            "softwarelicense": {
                "software_name": "SAMPLE 1",
                "license_name": "LGPLv2.1",
                "version": "2.0",
                "type_of_license": "WEAKLY COPYLEFT",
                "description": "The 2.0 version of the BSD License",
                "disclaimer": "Disclamer copyright",
                "risk_for_choosing_license": "One thing to consider is that you cannot combine LGPLv2.1 with.",
                "limitation_of_liability": "In no event and under no legal",
                "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "recommendation": "2.0",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [
                    "definition",
                    "limitation_of_liability",
                    "disclaimer",
                    "recommendation",
                    "trademark"
                ],
                "license_compatibility": [
                    {
                        "license": "PUBLIC DOMAIN",
                        "percentage_of_comaptibility": "45",
                        "is_compatible": true
                    },
                    {
                        "license": "MIT/XII",
                        "percentage_of_comaptibility": "70",
                        "is_compatible": true
                    },
                    {
                        "license": "BSD",
                        "percentage_of_comaptibility": "60",
                        "is_compatible": true
                    },
                    {
                        "license": "APACHE 2.0",
                        "percentage_of_comaptibility": "90",
                        "is_compatible": true
                    },
                    {
                        "license": "GPLv2",
                        "percentage_of_comaptibility": "80",
                        "is_compatible": false
                    },
                    {
                        "license": "GPL2+",
                        "percentage_of_comaptibility": "95",
                        "is_compatible": false
                    },
                    {
                        "license": "GPLv3 or GPLv3+",
                        "percentage_of_comaptibility": "100",
                        "is_compatible": false
                    }
                ],
                "license_compatible_with_lookup": [
                    "PUBLIC DOMAIN",
                    "MIT/XII",
                    "BSD",
                    "APACHE 2.0"
                ],
                "license_not_compatible_with_lookup": [
                    "GPLv2",
                    "GPL2+",
                    "GPLv3 or GPLv3+"
                ]
            }
        },
        {
            "_id": "63047c5ebecabe8233cdcd4c",
            "eventId": "FB1010000000166123835456631894",
            "softwarelicense": {
                "software_name": "SAMPLE 2",
                "license_name": "BSD",
                "version": "3.0",
                "type_of_license": "PERMISSIVE",
                "description": "The 2.0 version of the BSD License",
                "disclaimer": "Disclamer copyright",
                "risk_for_choosing_license": "One thing to consider is that you cannot combine BSD with.",
                "limitation_of_liability": "In no event and under no legal",
                "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "recommendation": "2.0",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [
                    "definition",
                    "limitation_of_liability",
                    "disclaimer",
                    "recommendation",
                    "trademark",
                    "scope"
                ],
                "license_compatibility": [
                    {
                        "license": "LGPLv2.1",
                        "percentage_of_comaptibility": "45",
                        "is_compatible": true
                    },
                    {
                        "license": "LGPL2.1+",
                        "percentage_of_comaptibility": "70",
                        "is_compatible": true
                    },
                    {
                        "license": "LGPLv3 or LGPLv3+",
                        "percentage_of_comaptibility": "60",
                        "is_compatible": true
                    },
                    {
                        "license": "MPL 1.1",
                        "percentage_of_comaptibility": "90",
                        "is_compatible": true
                    },
                    {
                        "license": "Affero GPL v3",
                        "percentage_of_comaptibility": "80",
                        "is_compatible": false
                    }
                ],
                "license_compatible_with_lookup": [
                    "LGPLv2.1",
                    "LGPL2.1+",
                    "LGPLv3 or LGPLv3+",
                    "MPL 1.1"
                ],
                "license_not_compatible_with_lookup": [
                    "Affero GPL v3"
                ]
            }
        }
    ]
}
```

#### POST /api/licenses/

- General:
  - Creates a new software license using the submitted json data, Returns the detail of the created license, success value, and event id.
- `curl http://127.0.0.1:8000/api/licenses/ -X POST -H "Content-Type: application/json" -d ' { "software_name": "SAMPLE 1", "license_name": "LGPLv2.1", "version": "2.0", "type_of_license": "WEAKLY COPYLEFT", "description": "The 2.0 version of the BSD License", "disclaimer": "Disclamer copyright", "risk_for_choosing_license": "One thing to consider is that you cannot combine LGPLv2.1 with.", "limitation_of_liability": "In no event and under no legal", "license_url": "https://www.apache.org/licenses/LICENSE-2.0", "image_url": "https://www.apache.org/licenses/LICENSE-2.0", "recommendation": "2.0", "released_date": "2022-05-10", "is_active": true, "license_attributes": [ "definition", "limitation_of_liability", "disclaimer", "recommendation", "trademark" ], "license_compatibility": [ { "license": "PUBLIC DOMAIN", "percentage_of_comaptibility": 45, "is_compatible": true }, { "license": "MIT/XII", "percentage_of_comaptibility": 70, "is_compatible": true }, { "license": "BSD", "percentage_of_comaptibility": 60, "is_compatible": true }, { "license": "APACHE 2.0", "percentage_of_comaptibility": 90, "is_compatible": true }, { "license": "GPLv2", "percentage_of_comaptibility": 80, "is_compatible": false }, { "license": "GPL2+", "percentage_of_comaptibility": 95, "is_compatible": false }, { "license": "GPLv3 or GPLv3+", "percentage_of_comaptibility": 100, "is_compatible": false } ], "license_compatible_with_lookup": [ "PUBLIC DOMAIN", "MIT/XII", "BSD", "APACHE 2.0" ], "license_not_compatible_with_lookup": [ "GPLv2", "GPL2+", "GPLv3 or GPLv3+" ] }'`

- You can also open the link `http://127.0.0.1:8000/api/licenses/` in a browser and perform the post operation

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "63047b62b3a9611686cdcd56",
            "eventId": "FB1010000000166123810354118614",
            "softwarelicense": {
                "software_name": "SAMPLE 1",
                "license_name": "LGPLv2.1",
                "version": "2.0",
                "type_of_license": "WEAKLY COPYLEFT",
                "description": "The 2.0 version of the BSD License",
                "disclaimer": "Disclamer copyright",
                "risk_for_choosing_license": "One thing to consider is that you cannot combine LGPLv2.1 with.",
                "limitation_of_liability": "In no event and under no legal",
                "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "recommendation": "2.0",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [
                    "definition",
                    "limitation_of_liability",
                    "disclaimer",
                    "recommendation",
                    "trademark"
                ],
                "license_compatibility": [
                    {
                        "license": "PUBLIC DOMAIN",
                        "percentage_of_comaptibility": "45",
                        "is_compatible": true
                    },
                    {
                        "license": "MIT/XII",
                        "percentage_of_comaptibility": "70",
                        "is_compatible": true
                    },
                    {
                        "license": "BSD",
                        "percentage_of_comaptibility": "60",
                        "is_compatible": true
                    },
                    {
                        "license": "APACHE 2.0",
                        "percentage_of_comaptibility": "90",
                        "is_compatible": true
                    },
                    {
                        "license": "GPLv2",
                        "percentage_of_comaptibility": "80",
                        "is_compatible": false
                    },
                    {
                        "license": "GPL2+",
                        "percentage_of_comaptibility": "95",
                        "is_compatible": false
                    },
                    {
                        "license": "GPLv3 or GPLv3+",
                        "percentage_of_comaptibility": "100",
                        "is_compatible": false
                    }
                ],
                "license_compatible_with_lookup": [
                    "PUBLIC DOMAIN",
                    "MIT/XII",
                    "BSD",
                    "APACHE 2.0"
                ],
                "license_not_compatible_with_lookup": [
                    "GPLv2",
                    "GPL2+",
                    "GPLv3 or GPLv3+"
                ]
            }
        }
    ]
}
```

#### POST /api/licenses/

- General:
  - Check for compatibility between two software license with the submitted json data, return true if compatible else return false.
- `curl http://127.0.0.1:8000/api/licenses/ -X POST -H "Content-Type: application/json" -d ' { "license_event_id_one": "FB1010000000166123835456631894", "license_event_id_two": "FB1010000000166123810354118614", "action_type": "check-compatibility" } '`

- You can also open the link `http://127.0.0.1:8000/api/licenses/` in a browser and perform the post operation

```
{
    "is_compatible": true,
    "percentage_of_comaptibility": 45,
    "disclaimer": "Disclamer copyright",
    "recommendation": "2.0",
    "license_one": "LGPLv2.1",
    "license_two": "BSD"
}
```

#### GET /api/licenses/{event_id}/

- General:
  - Returns a list of software licenses objects, and success value
- Sample: `curl http://127.0.0.1:8000/api/licenses/FB1010000000166123810354118614/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "63047b62b3a9611686cdcd56",
            "eventId": "FB1010000000166123810354118614",
            "softwarelicense": {
                "software_name": "SAMPLE 1",
                "license_name": "LGPLv2.1",
                "version": "2.0",
                "type_of_license": "WEAKLY COPYLEFT",
                "description": "The 2.0 version of the BSD License",
                "disclaimer": "Disclamer copyright",
                "risk_for_choosing_license": "One thing to consider is that you cannot combine LGPLv2.1 with.",
                "limitation_of_liability": "In no event and under no legal",
                "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "recommendation": "2.0",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [
                    "definition",
                    "limitation_of_liability",
                    "disclaimer",
                    "recommendation",
                    "trademark"
                ],
                "license_compatibility": [
                    {
                        "license": "PUBLIC DOMAIN",
                        "percentage_of_comaptibility": "45",
                        "is_compatible": true
                    },
                    {
                        "license": "MIT/XII",
                        "percentage_of_comaptibility": "70",
                        "is_compatible": true
                    },
                    {
                        "license": "BSD",
                        "percentage_of_comaptibility": "60",
                        "is_compatible": true
                    },
                    {
                        "license": "APACHE 2.0",
                        "percentage_of_comaptibility": "90",
                        "is_compatible": true
                    },
                    {
                        "license": "GPLv2",
                        "percentage_of_comaptibility": "80",
                        "is_compatible": false
                    },
                    {
                        "license": "GPL2+",
                        "percentage_of_comaptibility": "95",
                        "is_compatible": false
                    },
                    {
                        "license": "GPLv3 or GPLv3+",
                        "percentage_of_comaptibility": "100",
                        "is_compatible": false
                    }
                ],
                "license_compatible_with_lookup": [
                    "PUBLIC DOMAIN",
                    "MIT/XII",
                    "BSD",
                    "APACHE 2.0"
                ],
                "license_not_compatible_with_lookup": [
                    "GPLv2",
                    "GPL2+",
                    "GPLv3 or GPLv3+"
                ]
            }
        }
    ]
}
```

#### PUT /api/licenses/{event_id}/

- General:
  - Fully update the software license of the given ID if it exists. Returns the updated data, success value, to update the frontend.
- `curl http://127.0.0.1:8000/api/licenses/FB1010000000166123810354118614/ -X PUT -H "Content-Type: application/json" -d ' { "software_name": "SAMPLE 25", "license_name": "LGPLv2.1", "version": "2.0", "type_of_license": "WEAKLY COPYLEFT", "description": "The 2.0 version of the BSD License", "disclaimer": "Disclamer copyright", "risk_for_choosing_license": "One thing to consider is that you cannot combine LGPLv2.1 with.", "limitation_of_liability": "In no event and under no legal", "license_url": "https://www.apache.org/licenses/LICENSE-2.0", "image_url": "https://www.apache.org/licenses/LICENSE-2.0", "recommendation": "2.0", "released_date": "2022-05-10", "is_active": true, "license_attributes": [ "definition", "limitation_of_liability", "disclaimer", "recommendation", "trademark" ], "license_compatibility": [ { "license": "PUBLIC DOMAIN", "percentage_of_comaptibility": 45, "is_compatible": true }, { "license": "MIT/XII", "percentage_of_comaptibility": 70, "is_compatible": true }, { "license": "BSD", "percentage_of_comaptibility": 60, "is_compatible": true }, { "license": "APACHE 2.0", "percentage_of_comaptibility": 90, "is_compatible": true }, { "license": "GPLv2", "percentage_of_comaptibility": 80, "is_compatible": false }, { "license": "GPL2+", "percentage_of_comaptibility": 95, "is_compatible": false }, { "license": "GPLv3 or GPLv3+", "percentage_of_comaptibility": 100, "is_compatible": false } ], "license_compatible_with_lookup": [ "PUBLIC DOMAIN", "MIT/XII", "BSD", "APACHE 2.0" ], "license_not_compatible_with_lookup": [ "GPLv2", "GPL2+", "GPLv3 or GPLv3+" ] }'`

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "63047b62b3a9611686cdcd56",
            "eventId": "FB1010000000166123810354118614",
            "softwarelicense": {
                "software_name": "SAMPLE 25",
                "license_name": "LGPLv2.1",
                "version": "2.0",
                "type_of_license": "WEAKLY COPYLEFT",
                "description": "The 2.0 version of the BSD License",
                "disclaimer": "Disclamer copyright",
                "risk_for_choosing_license": "One thing to consider is that you cannot combine LGPLv2.1 with.",
                "limitation_of_liability": "In no event and under no legal",
                "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "image_url": "https://www.apache.org/licenses/LICENSE-2.0",
                "recommendation": "2.0",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [
                    "definition",
                    "limitation_of_liability",
                    "disclaimer",
                    "recommendation",
                    "trademark"
                ],
                "license_compatibility": [
                    {
                        "license": "PUBLIC DOMAIN",
                        "percentage_of_comaptibility": "45",
                        "is_compatible": true
                    },
                    {
                        "license": "MIT/XII",
                        "percentage_of_comaptibility": "70",
                        "is_compatible": true
                    },
                    {
                        "license": "BSD",
                        "percentage_of_comaptibility": "60",
                        "is_compatible": true
                    },
                    {
                        "license": "APACHE 2.0",
                        "percentage_of_comaptibility": "90",
                        "is_compatible": true
                    },
                    {
                        "license": "GPLv2",
                        "percentage_of_comaptibility": "80",
                        "is_compatible": false
                    },
                    {
                        "license": "GPL2+",
                        "percentage_of_comaptibility": "95",
                        "is_compatible": false
                    },
                    {
                        "license": "GPLv3 or GPLv3+",
                        "percentage_of_comaptibility": "100",
                        "is_compatible": false
                    }
                ],
                "license_compatible_with_lookup": [
                    "PUBLIC DOMAIN",
                    "MIT/XII",
                    "BSD",
                    "APACHE 2.0"
                ],
                "license_not_compatible_with_lookup": [
                    "GPLv2",
                    "GPL2+",
                    "GPLv3 or GPLv3+"
                ]
            }
        }
    ]
}
```

#### GET /api/licenses/?search_term=mit&action_type=search

- General:
  - Search the software license by license. Return query result.
- `curl http://127.0.0.1:8000/api/licenses/?search_term=mit&action_type=search -X GET`

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "630db14a2eb7c2571343a9fb",
            "eventId": "FB1010000000016618417215307426",
            "softwarelicense": {
                "software_name": "MIT",
                "license_name": "MIT",
                "version": "1",
                "type_of_license": "Permissive",
                "description": "nil",
                "disclaimer": "nil",
                "risk_for_choosing_license": "nil",
                "limitation_of_liability": "nil",
                "license_url": "https://sample.com/img.png",
                "image_url": "https://sample.com/img.png",
                "recommendation": "nil",
                "released_date": "2022-05-10",
                "is_active": true,
                "license_attributes": [
                    "Obtain copyright notice",
                    "Right to Use, copy, distribute",
                    "Right to modify",
                    "Right to Publish",
                    "Right to sublicense and sell copies",
                    "Limitations",
                    "No Warranty"
                ],
                "license_compatibility": [],
                "license_compatible_with_lookup": [],
                "license_not_compatible_with_lookup": []
            }
        }
    ]
}
```

### Software Agreement Policy

#### GET /api/agreements/

- General:
  - Returns a list of software agreements objects, and success value
- Sample: `curl http://127.0.0.1:8000/api/agreements/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "63076817b171c30837335384",
            "eventId": "785455899666558884",
            "agreement": {
                "date_of_execution_of_document": "2022-10-20T00:00:00+00:00",
                "party_1_entity_type": "Organization",
                "party_1_full_name": "Dowell Research 1",
                "party_1_postal_address": "P.O.BOX 45, India",
                "party_1_jurisdiction_incorporated": "sample law",
                "party_1_registration_number": "RS5428888",
                "party_1_registrar_office_address": "sample office address",
                "party_1_principal_place_of_business": "India",
                "party_2_entity_type": "Organization",
                "party_2_full_name": "Organization Name",
                "party_2_postal_address": "P.O.BOX 87",
                "party_2_jurisdiction_incorporated": "USA",
                "party_2_registration_number": "459996665",
                "party_2_registrar_office_address": "Some where in USA",
                "party_2_principal_place_of_business": "USA",
                "charges_payable": 245.0,
                "software_document_identification": "My software sample",
                "contract_effective_date": "2022-10-29T00:00:00+00:00",
                "minimum_terms_apply": "2",
                "is_software_form_specified": false,
                "software_form": "yes",
                "is_non_material_defects_count_as_software_defects": true,
                "ways_defect_affect_software": "miss handle",
                "is_set_of_exclusions_included": false,
                "exclusions_apply": "nil",
                "software_specification": "software spic",
                "can_software_specification_be_varied_by_the_parties": false,
                "terms_of_contract_duration": "4",
                "is_inline_copy_right_remove": true,
                "is_term_of_contract_indefinite": false,
                "contract_termination_date": "2023-05-20T00:00:00+00:00",
                "events_that_will_cause_contract_to_be_terminated": "miss handle",
                "number_of_license_to_be_deliver": 5,
                "software_delivery_channel": "Github",
                "software_delivery_period": "4",
                "what_did_licensor_supply_to_the_licensee": "CRM software",
                "purpose_of_supply": "request by licensee",
                "when_should_invoice_be_issued": "After getting requirement from licensee",
                "invoicing_date": "2022-10-20T00:00:00+00:00",
                "period_for_payment_of_invoices": "15 days",
                "effective_date_for_invoice_payment": "2022-10-25T00:00:00+00:00",
                "invoice_payment_method": "via payoner",
                "interest_rate_apply_to_late_payment": 2.5,
                "optional_element_warranty": "nil",
                "is_warranty_relate_to_a_specific_period": true,
                "period_apply_to_warranty": "2 year",
                "scope_of_warranty": "Entire maintenance of software",
                "jurisdictional_coverage_of_warranty": "india law",
                "circumstances_in_which_licensor_may_exercise_its_rights": "when licenee miss handle software",
                "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false,
                "are_there_limitations_on_right_to_modify": false,
                "limitations_on_right_to_modify_specification": "nil",
                "termination_notice_period_apply": true,
                "is_termination_period_expirable": true,
                "relevant_termination_period": "3 month",
                "circumstances_in_which_a_party_may_terminate_for_breach": "un-satisfaction of service",
                "time_frame_for_the_notice_period": "1 month",
                "contact_details_to_sent_contractual_notices_to_the_licensor": "example1@sample.com",
                "contact_details_to_sent_contractual_notices_to_the_licensee": "example2@sample.com",
                "law_governs_document": "law 1",
                "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "india law",
                "will_the_contract_signed_by_party_1_contracting_entity": true,
                "party_1_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/5554image.png",
                "full_name_of_party_1_signatory": "party 1 name",
                "party_1_date_of_signing_contract": "2022-11-02T00:00:00+00:00",
                "full_name_of_party_1_witness": "witness 1 name",
                "party_1_witness_date_of_signing_contract": "2022-11-02T00:00:00+00:00",
                "will_the_contract_signed_by_pary_2_contracting_entity": true,
                "party_2_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/44454image.png",
                "full_name_of_party_2_signatory": "party 2 name",
                "party_2_date_of_signing_contract": "2022-11-05T00:00:00+00:00",
                "full_name_of_party_2_witness": "witness 2 name",
                "party_2_witness_date_of_signing_contract": "2022-11-05T00:00:00+00:00"
            }
        }
    ]
}
```

#### POST /api/agreements/

- General:
  - Creates a new software agreement using the submitted json data, Returns the detail of the created agreement, success value, and event id.
- `curl http://127.0.0.1:8000/api/agreements/ -X POST -H "Content-Type: application/json" -d '{ "date_of_execution_of_document": "2022-10-20T00:00:00+00:00", "party_1_entity_type": "Organization", "party_1_full_name": "Dowell Research 1", "party_1_postal_address": "P.O.BOX 45, India", "party_1_jurisdiction_incorporated": "sample law", "party_1_registration_number": "RS5428888", "party_1_registrar_office_address": "sample office address", "party_1_principal_place_of_business": "India", "party_2_entity_type": "Organization", "party_2_full_name": "Organization Name", "party_2_postal_address": "P.O.BOX 87", "party_2_jurisdiction_incorporated": "USA", "party_2_registration_number": "459996665", "party_2_registrar_office_address": "Some where in USA", "party_2_principal_place_of_business": "USA", "charges_payable": 245.0, "software_document_identification": "My software sample", "contract_effective_date": "2022-10-29T00:00:00+00:00", "minimum_terms_apply": "2", "is_software_form_specified": false, "software_form": "yes", "is_non_material_defects_count_as_software_defects": true, "ways_defect_affect_software": "miss handle", "is_set_of_exclusions_included": false, "exclusions_apply": "nil", "software_specification": "software spic", "can_software_specification_be_varied_by_the_parties": false, "terms_of_contract_duration": "4", "is_inline_copy_right_remove": true, "is_term_of_contract_indefinite": false, "contract_termination_date": "2023-05-20T00:00:00+00:00", "events_that_will_cause_contract_to_be_terminated": "miss handle", "number_of_license_to_be_deliver": 5, "software_delivery_channel": "Github", "software_delivery_period": "4", "what_did_licensor_supply_to_the_licensee": "CRM software", "purpose_of_supply": "request by licensee", "when_should_invoice_be_issued": "After getting requirement from licensee", "invoicing_date": "2022-10-20T00:00:00+00:00", "period_for_payment_of_invoices": "15 days", "effective_date_for_invoice_payment": "2022-10-25T00:00:00+00:00", "invoice_payment_method": "via payoner", "interest_rate_apply_to_late_payment": 2.5, "optional_element_warranty": "nil", "is_warranty_relate_to_a_specific_period": true, "period_apply_to_warranty": "2 year", "scope_of_warranty": "Entire maintenance of software", "jurisdictional_coverage_of_warranty": "india law", "circumstances_in_which_licensor_may_exercise_its_rights": "when licenee miss handle software", "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false, "are_there_limitations_on_right_to_modify": false, "limitations_on_right_to_modify_specification": "nil", "termination_notice_period_apply": true, "is_termination_period_expirable": true, "relevant_termination_period": "3 month", "circumstances_in_which_a_party_may_terminate_for_breach": "un-satisfaction of service", "time_frame_for_the_notice_period": "1 month", "contact_details_to_sent_contractual_notices_to_the_licensor": "example1@sample.com", "contact_details_to_sent_contractual_notices_to_the_licensee": "example2@sample.com", "law_governs_document": "law 1", "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "india law", "will_the_contract_signed_by_party_1_contracting_entity": true, "party_1_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/5554image.png", "full_name_of_party_1_signatory": "party 1 name", "party_1_date_of_signing_contract": "2022-11-02T00:00:00+00:00", "full_name_of_party_1_witness": "witness 1 name", "party_1_witness_date_of_signing_contract": "2022-11-02T00:00:00+00:00", "will_the_contract_signed_by_pary_2_contracting_entity": true, "party_2_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/44454image.png", "full_name_of_party_2_signatory": "party 2 name", "party_2_date_of_signing_contract": "2022-11-05T00:00:00+00:00", "full_name_of_party_2_witness": "witness 2 name", "party_2_witness_date_of_signing_contract": "2022-11-05T00:00:00+00:00" } '`

- You can also open the link `http://127.0.0.1:8000/api/agreements/` in a browser and perform the post operation

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "63076817b171c30837335384",
            "eventId": "785455899666558884",
            "agreement": {
                "date_of_execution_of_document": "2022-10-20T00:00:00+00:00",
                "party_1_entity_type": "Organization",
                "party_1_full_name": "Dowell Research 1",
                "party_1_postal_address": "P.O.BOX 45, India",
                "party_1_jurisdiction_incorporated": "sample law",
                "party_1_registration_number": "RS5428888",
                "party_1_registrar_office_address": "sample office address",
                "party_1_principal_place_of_business": "India",
                "party_2_entity_type": "Organization",
                "party_2_full_name": "Organization Name",
                "party_2_postal_address": "P.O.BOX 87",
                "party_2_jurisdiction_incorporated": "USA",
                "party_2_registration_number": "459996665",
                "party_2_registrar_office_address": "Some where in USA",
                "party_2_principal_place_of_business": "USA",
                "charges_payable": 245.0,
                "software_document_identification": "My software sample",
                "contract_effective_date": "2022-10-29T00:00:00+00:00",
                "minimum_terms_apply": "2",
                "is_software_form_specified": false,
                "software_form": "yes",
                "is_non_material_defects_count_as_software_defects": true,
                "ways_defect_affect_software": "miss handle",
                "is_set_of_exclusions_included": false,
                "exclusions_apply": "nil",
                "software_specification": "software spic",
                "can_software_specification_be_varied_by_the_parties": false,
                "terms_of_contract_duration": "4",
                "is_inline_copy_right_remove": true,
                "is_term_of_contract_indefinite": false,
                "contract_termination_date": "2023-05-20T00:00:00+00:00",
                "events_that_will_cause_contract_to_be_terminated": "miss handle",
                "number_of_license_to_be_deliver": 5,
                "software_delivery_channel": "Github",
                "software_delivery_period": "4",
                "what_did_licensor_supply_to_the_licensee": "CRM software",
                "purpose_of_supply": "request by licensee",
                "when_should_invoice_be_issued": "After getting requirement from licensee",
                "invoicing_date": "2022-10-20T00:00:00+00:00",
                "period_for_payment_of_invoices": "15 days",
                "effective_date_for_invoice_payment": "2022-10-25T00:00:00+00:00",
                "invoice_payment_method": "via payoner",
                "interest_rate_apply_to_late_payment": 2.5,
                "optional_element_warranty": "nil",
                "is_warranty_relate_to_a_specific_period": true,
                "period_apply_to_warranty": "2 year",
                "scope_of_warranty": "Entire maintenance of software",
                "jurisdictional_coverage_of_warranty": "india law",
                "circumstances_in_which_licensor_may_exercise_its_rights": "when licenee miss handle software",
                "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false,
                "are_there_limitations_on_right_to_modify": false,
                "limitations_on_right_to_modify_specification": "nil",
                "termination_notice_period_apply": true,
                "is_termination_period_expirable": true,
                "relevant_termination_period": "3 month",
                "circumstances_in_which_a_party_may_terminate_for_breach": "un-satisfaction of service",
                "time_frame_for_the_notice_period": "1 month",
                "contact_details_to_sent_contractual_notices_to_the_licensor": "example1@sample.com",
                "contact_details_to_sent_contractual_notices_to_the_licensee": "example2@sample.com",
                "law_governs_document": "law 1",
                "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "india law",
                "will_the_contract_signed_by_party_1_contracting_entity": true,
                "party_1_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/5554image.png",
                "full_name_of_party_1_signatory": "party 1 name",
                "party_1_date_of_signing_contract": "2022-11-02T00:00:00+00:00",
                "full_name_of_party_1_witness": "witness 1 name",
                "party_1_witness_date_of_signing_contract": "2022-11-02T00:00:00+00:00",
                "will_the_contract_signed_by_pary_2_contracting_entity": true,
                "party_2_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/44454image.png",
                "full_name_of_party_2_signatory": "party 2 name",
                "party_2_date_of_signing_contract": "2022-11-05T00:00:00+00:00",
                "full_name_of_party_2_witness": "witness 2 name",
                "party_2_witness_date_of_signing_contract": "2022-11-05T00:00:00+00:00"
            }
        }
    ]
}
```

#### GET /api/agreements/{event_id}/

- General:
  - Returns a list of software agreement objects, and success value
- Sample: `curl http://127.0.0.1:8000/api/agreements/785455899666558884/` or open link in a browser

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "63076817b171c30837335384",
            "eventId": "785455899666558884",
            "agreement": {
                "date_of_execution_of_document": "2022-10-20T00:00:00+00:00",
                "party_1_entity_type": "Organization",
                "party_1_full_name": "Dowell Research 1",
                "party_1_postal_address": "P.O.BOX 45, India",
                "party_1_jurisdiction_incorporated": "sample law",
                "party_1_registration_number": "RS5428888",
                "party_1_registrar_office_address": "sample office address",
                "party_1_principal_place_of_business": "India",
                "party_2_entity_type": "Organization",
                "party_2_full_name": "Organization Name",
                "party_2_postal_address": "P.O.BOX 87",
                "party_2_jurisdiction_incorporated": "USA",
                "party_2_registration_number": "459996665",
                "party_2_registrar_office_address": "Some where in USA",
                "party_2_principal_place_of_business": "USA",
                "charges_payable": 245.0,
                "software_document_identification": "My software sample",
                "contract_effective_date": "2022-10-29T00:00:00+00:00",
                "minimum_terms_apply": "2",
                "is_software_form_specified": false,
                "software_form": "yes",
                "is_non_material_defects_count_as_software_defects": true,
                "ways_defect_affect_software": "miss handle",
                "is_set_of_exclusions_included": false,
                "exclusions_apply": "nil",
                "software_specification": "software spic",
                "can_software_specification_be_varied_by_the_parties": false,
                "terms_of_contract_duration": "4",
                "is_inline_copy_right_remove": true,
                "is_term_of_contract_indefinite": false,
                "contract_termination_date": "2023-05-20T00:00:00+00:00",
                "events_that_will_cause_contract_to_be_terminated": "miss handle",
                "number_of_license_to_be_deliver": 5,
                "software_delivery_channel": "Github",
                "software_delivery_period": "4",
                "what_did_licensor_supply_to_the_licensee": "CRM software",
                "purpose_of_supply": "request by licensee",
                "when_should_invoice_be_issued": "After getting requirement from licensee",
                "invoicing_date": "2022-10-20T00:00:00+00:00",
                "period_for_payment_of_invoices": "15 days",
                "effective_date_for_invoice_payment": "2022-10-25T00:00:00+00:00",
                "invoice_payment_method": "via payoner",
                "interest_rate_apply_to_late_payment": 2.5,
                "optional_element_warranty": "nil",
                "is_warranty_relate_to_a_specific_period": true,
                "period_apply_to_warranty": "2 year",
                "scope_of_warranty": "Entire maintenance of software",
                "jurisdictional_coverage_of_warranty": "india law",
                "circumstances_in_which_licensor_may_exercise_its_rights": "when licenee miss handle software",
                "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false,
                "are_there_limitations_on_right_to_modify": false,
                "limitations_on_right_to_modify_specification": "nil",
                "termination_notice_period_apply": true,
                "is_termination_period_expirable": true,
                "relevant_termination_period": "3 month",
                "circumstances_in_which_a_party_may_terminate_for_breach": "un-satisfaction of service",
                "time_frame_for_the_notice_period": "1 month",
                "contact_details_to_sent_contractual_notices_to_the_licensor": "example1@sample.com",
                "contact_details_to_sent_contractual_notices_to_the_licensee": "example2@sample.com",
                "law_governs_document": "law 1",
                "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "india law",
                "will_the_contract_signed_by_party_1_contracting_entity": true,
                "party_1_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/5554image.png",
                "full_name_of_party_1_signatory": "party 1 name",
                "party_1_date_of_signing_contract": "2022-11-02T00:00:00+00:00",
                "full_name_of_party_1_witness": "witness 1 name",
                "party_1_witness_date_of_signing_contract": "2022-11-02T00:00:00+00:00",
                "will_the_contract_signed_by_pary_2_contracting_entity": true,
                "party_2_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/44454image.png",
                "full_name_of_party_2_signatory": "party 2 name",
                "party_2_date_of_signing_contract": "2022-11-05T00:00:00+00:00",
                "full_name_of_party_2_witness": "witness 2 name",
                "party_2_witness_date_of_signing_contract": "2022-11-05T00:00:00+00:00"
            }
        }
    ]
}
```

#### PUT /api/agreements/{event_id}/

- General:
  - Fully update the software agreement of the given ID if it exists. Returns the updated data, success value, to update the frontend.
- `curl http://127.0.0.1:8000/api/agreements/785455899666558884/ -X PUT -H "Content-Type: application/json" -d ' { "date_of_execution_of_document": "2022-10-20T00:00:00+00:00", "party_1_entity_type": "Individual", "party_1_full_name": "Dowell Research 1", "party_1_postal_address": "P.O.BOX 45, India", "party_1_jurisdiction_incorporated": "sample law", "party_1_registration_number": "RS5428888", "party_1_registrar_office_address": "sample office address", "party_1_principal_place_of_business": "India", "party_2_entity_type": "Organization", "party_2_full_name": "Organization Name", "party_2_postal_address": "P.O.BOX 87", "party_2_jurisdiction_incorporated": "USA", "party_2_registration_number": "459996665", "party_2_registrar_office_address": "Some where in USA", "party_2_principal_place_of_business": "USA", "charges_payable": 245.0, "software_document_identification": "My software sample", "contract_effective_date": "2022-10-29T00:00:00+00:00", "minimum_terms_apply": "2", "is_software_form_specified": false, "software_form": "yes", "is_non_material_defects_count_as_software_defects": true, "ways_defect_affect_software": "miss handle", "is_set_of_exclusions_included": false, "exclusions_apply": "nil", "software_specification": "software spic", "can_software_specification_be_varied_by_the_parties": false, "terms_of_contract_duration": "4", "is_inline_copy_right_remove": true, "is_term_of_contract_indefinite": false, "contract_termination_date": "2023-05-20T00:00:00+00:00", "events_that_will_cause_contract_to_be_terminated": "miss handle", "number_of_license_to_be_deliver": 5, "software_delivery_channel": "Github", "software_delivery_period": "4", "what_did_licensor_supply_to_the_licensee": "CRM software", "purpose_of_supply": "request by licensee", "when_should_invoice_be_issued": "After getting requirement from licensee", "invoicing_date": "2022-10-20T00:00:00+00:00", "period_for_payment_of_invoices": "15 days", "effective_date_for_invoice_payment": "2022-10-25T00:00:00+00:00", "invoice_payment_method": "via payoner", "interest_rate_apply_to_late_payment": 2.5, "optional_element_warranty": "nil", "is_warranty_relate_to_a_specific_period": true, "period_apply_to_warranty": "2 year", "scope_of_warranty": "Entire maintenance of software", "jurisdictional_coverage_of_warranty": "india law", "circumstances_in_which_licensor_may_exercise_its_rights": "when licenee miss handle software", "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false, "are_there_limitations_on_right_to_modify": false, "limitations_on_right_to_modify_specification": "nil", "termination_notice_period_apply": true, "is_termination_period_expirable": true, "relevant_termination_period": "3 month", "circumstances_in_which_a_party_may_terminate_for_breach": "un-satisfaction of service", "time_frame_for_the_notice_period": "1 month", "contact_details_to_sent_contractual_notices_to_the_licensor": "example1@sample.com", "contact_details_to_sent_contractual_notices_to_the_licensee": "example2@sample.com", "law_governs_document": "law 1", "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "india law", "will_the_contract_signed_by_party_1_contracting_entity": true, "party_1_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/5554image.png", "full_name_of_party_1_signatory": "party 1 name", "party_1_date_of_signing_contract": "2022-11-02T00:00:00+00:00", "full_name_of_party_1_witness": "witness 1 name", "party_1_witness_date_of_signing_contract": "2022-11-02T00:00:00+00:00", "will_the_contract_signed_by_pary_2_contracting_entity": true, "party_2_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/44454image.png", "full_name_of_party_2_signatory": "party 2 name", "party_2_date_of_signing_contract": "2022-11-05T00:00:00+00:00", "full_name_of_party_2_witness": "witness 2 name", "party_2_witness_date_of_signing_contract": "2022-11-05T00:00:00+00:00" }'`

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "63076817b171c30837335384",
            "eventId": "785455899666558884",
            "agreement": {
                "date_of_execution_of_document": "2022-10-20T00:00:00+00:00",
                "party_1_entity_type": "Individual",
                "party_1_full_name": "Dowell Research 1",
                "party_1_postal_address": "P.O.BOX 45, India",
                "party_1_jurisdiction_incorporated": "sample law",
                "party_1_registration_number": "RS5428888",
                "party_1_registrar_office_address": "sample office address",
                "party_1_principal_place_of_business": "India",
                "party_2_entity_type": "Organization",
                "party_2_full_name": "Organization Name",
                "party_2_postal_address": "P.O.BOX 87",
                "party_2_jurisdiction_incorporated": "USA",
                "party_2_registration_number": "459996665",
                "party_2_registrar_office_address": "Some where in USA",
                "party_2_principal_place_of_business": "USA",
                "charges_payable": 245.0,
                "software_document_identification": "My software sample",
                "contract_effective_date": "2022-10-29T00:00:00+00:00",
                "minimum_terms_apply": "2",
                "is_software_form_specified": false,
                "software_form": "yes",
                "is_non_material_defects_count_as_software_defects": true,
                "ways_defect_affect_software": "miss handle",
                "is_set_of_exclusions_included": false,
                "exclusions_apply": "nil",
                "software_specification": "software spic",
                "can_software_specification_be_varied_by_the_parties": false,
                "terms_of_contract_duration": "4",
                "is_inline_copy_right_remove": true,
                "is_term_of_contract_indefinite": false,
                "contract_termination_date": "2023-05-20T00:00:00+00:00",
                "events_that_will_cause_contract_to_be_terminated": "miss handle",
                "number_of_license_to_be_deliver": 5,
                "software_delivery_channel": "Github",
                "software_delivery_period": "4",
                "what_did_licensor_supply_to_the_licensee": "CRM software",
                "purpose_of_supply": "request by licensee",
                "when_should_invoice_be_issued": "After getting requirement from licensee",
                "invoicing_date": "2022-10-20T00:00:00+00:00",
                "period_for_payment_of_invoices": "15 days",
                "effective_date_for_invoice_payment": "2022-10-25T00:00:00+00:00",
                "invoice_payment_method": "via payoner",
                "interest_rate_apply_to_late_payment": 2.5,
                "optional_element_warranty": "nil",
                "is_warranty_relate_to_a_specific_period": true,
                "period_apply_to_warranty": "2 year",
                "scope_of_warranty": "Entire maintenance of software",
                "jurisdictional_coverage_of_warranty": "india law",
                "circumstances_in_which_licensor_may_exercise_its_rights": "when licenee miss handle software",
                "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false,
                "are_there_limitations_on_right_to_modify": false,
                "limitations_on_right_to_modify_specification": "nil",
                "termination_notice_period_apply": true,
                "is_termination_period_expirable": true,
                "relevant_termination_period": "3 month",
                "circumstances_in_which_a_party_may_terminate_for_breach": "un-satisfaction of service",
                "time_frame_for_the_notice_period": "1 month",
                "contact_details_to_sent_contractual_notices_to_the_licensor": "example1@sample.com",
                "contact_details_to_sent_contractual_notices_to_the_licensee": "example2@sample.com",
                "law_governs_document": "law 1",
                "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "india law",
                "will_the_contract_signed_by_party_1_contracting_entity": true,
                "party_1_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/5554image.png",
                "full_name_of_party_1_signatory": "party 1 name",
                "party_1_date_of_signing_contract": "2022-11-02T00:00:00+00:00",
                "full_name_of_party_1_witness": "witness 1 name",
                "party_1_witness_date_of_signing_contract": "2022-11-02T00:00:00+00:00",
                "will_the_contract_signed_by_pary_2_contracting_entity": true,
                "party_2_signatory_scanned_copy_url": "https://4555.dowell-storage-server.com/44454image.png",
                "full_name_of_party_2_signatory": "party 2 name",
                "party_2_date_of_signing_contract": "2022-11-05T00:00:00+00:00",
                "full_name_of_party_2_witness": "witness 2 name",
                "party_2_witness_date_of_signing_contract": "2022-11-05T00:00:00+00:00"
            }
        }
    ]
}
```

### Attibutes

#### GET /api/commonattributes/

- General:
  - Returns a list of common attribute objects, and success value
- Sample: `curl http://127.0.0.1:8000/api/commonattributes/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "631852cef0ec12a84b24ad90",
            "eventId": "FB1010000000166253844055620553",
            "common_attributes": {
                "name": "Grant of Copyright License",
                "code": "G_Copyright"
            }
        },
        {
            "_id": "631852e9eae6baeed824ae55",
            "eventId": "FB1010000000166253846754137218",
            "common_attributes": {
                "name": "Grant of Patent License",
                "code": "G_Patent"
            }
        }
    ]
}
```

#### GET /api/commonattributes/{event_id}/

- General:
  - Returns a list of common attribute object, and success value
- Sample: `curl http://127.0.0.1:8000/api/commonattributes/FB1010000000166253846754137218/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "631852e9eae6baeed824ae55",
            "eventId": "FB1010000000166253846754137218",
            "common_attributes": {
                "name": "Grant of Patent License",
                "code": "G_Patent"
            }
        }
    ]
}
```

#### POST /api/commonattributes/

- General:
  - Creates a new common attribute using the submitted json data, Returns the detail of the created common attribute, success value, and event id.
- `curl http://127.0.0.1:8000/api/commonattributes/ -X POST -H "Content-Type: application/json" -d '{ "name": "Grant of Copyright License", "code": "G_Copyright" } '`

- You can also open the link `http://127.0.0.1:8000/api/commonattributes/` in a browser and perform the post operation

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "631852e9eae6baeed824ae55",
            "eventId": "FB1010000000166253846754137218",
            "common_attributes": {
                "name": "Grant of Patent License",
                "code": "G_Patent"
            }
        }
    ]
}
```

#### PUT /api/commonattributes/{:event_id}

- General:
  - Creates a new common attribute using the submitted json data, Returns the detail of the created common attribute, success value, and event id.
- `curl http://127.0.0.1:8000/api/commonattributes/FB1010000000166253846754137218/ -X PUT -H "Content-Type: application/json" -d '{ "name": "Grant of Copyright License", "code": "G_Copyright" } '`

- You can also open the link `http://127.0.0.1:8000/api/commonattributes/FB1010000000166253846754137218/` in a browser and perform the put operation

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "631852e9eae6baeed824ae55",
            "eventId": "FB1010000000166253846754137218",
            "common_attributes": {
                "name": "Grant of Copyright License",
                "code": "G_Copyright"
            }
        }
    ]
}
```

#### GET /api/attributes/

- General:
  - Returns a list of attribute objects, and success value
- Sample: `curl http://127.0.0.1:8000/api/attributes/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "631495bb99c608329b714832",
            "eventId": "FB1010000000166229342959770951",
            "attributes": {
                "name": "Conveying Modified Source Versions",
                "common_attribute": {
                    "_id": "63146f1699c608329b714706",
                    "eventId": "FB1010000000166228353751007912",
                    "name": "sample 1",
                    "code": "sample_code_1"
                }
            }
        },
        {
            "_id": "631496c6865bf7cf8a714743",
            "eventId": "FB1010000000166229369651486177",
            "attributes": {
                "name": "Conveying Modified Source Versions",
                "common_attribute": {
                    "_id": "63146d2799c608329b7146ed",
                    "eventId": "FB1010000000166228304251473167",
                    "name": "sample 2",
                    "code": "sample_code_12"
                }
            }
        }
    ]
}
```

#### GET /api/attributes/{event_id}/

- General:
  - Returns a list of attribute object, and success value
- Sample: `curl http://127.0.0.1:8000/api/attributes/FB1010000000166229342959770951/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "631495bb99c608329b714832",
            "eventId": "FB1010000000166229342959770951",
            "attributes": {
                "name": "Conveying Modified Source Versions",
                "common_attribute": {
                    "_id": "63146f1699c608329b714706",
                    "eventId": "FB1010000000166228353751007912",
                    "name": "sample 1",
                    "code": "sample_code_1"
                }
            }
        }
    ]
}
```

#### POST /api/attributes/

- General:
  - Creates a new attribute using the submitted json data, Returns the detail of the created attribute, success value, and event id.
- `curl http://127.0.0.1:8000/api/attributes/ -X POST -H "Content-Type: application/json" -d '{ "name": "Conveying Modified Source Versions", "common_attribute": { "_id": "63146d2799c608329b7146ed", "eventId": "FB1010000000166228304251473167", "name": "sample 2", "code": "sample_code_12" }'`

- You can also open the link `http://127.0.0.1:8000/api/attributes/` in a browser and perform the post operation

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "631496c6865bf7cf8a714743",
            "eventId": "FB1010000000166229369651486177",
            "attributes": {
                "name": "Conveying Modified Source Versions",
                "common_attribute": {
                    "_id": "63146d2799c608329b7146ed",
                    "eventId": "FB1010000000166228304251473167",
                    "name": "sample 2",
                    "code": "sample_code_12"
                }
            }
        }
    ]
}
```

#### PUT /api/attributes/{event_id}/

- General:
  - Creates a new attribute using the submitted json data, Returns the detail of the created attribute, success value, and event id.
- `curl http://127.0.0.1:8000/api/attributes/FB1010000000166229369651486177/ -X PUT -H "Content-Type: application/json" -d '{ "name": "Conveying Modified Source Versions", "common_attribute": { "_id": "63146d2799c608329b7146ed", "eventId": "FB1010000000166228304251473167", "name": "sample 2", "code": "sample_code_12" } }'`

- You can also open the link `http://127.0.0.1:8000/api/attributes/FB1010000000166229369651486177/` in a browser and perform the put operation

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "631496c6865bf7cf8a714743",
            "eventId": "FB1010000000166229369651486177",
            "attributes": {
                "name": "Conveying Modified Source Versions",
                "common_attribute": {
                    "_id": "63146d2799c608329b7146ed",
                    "eventId": "FB1010000000166228304251473167",
                    "name": "sample 2",
                    "code": "sample_code_12"
                }
            }
        }
    ]
}
```

#### GET /api/contacts/

- General:
  - Returns a list of contact us objects, and success value
- Sample: `curl http://127.0.0.1:8000/api/contacts/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
{
            "_id": "6323cbb0002f0020a7730e9e",
            "eventId": "FB1010000000166329028254989355",
            "contacts": {
                "full_name": "sample",
                "email": "sample@sample.com",
                "message": "sample message",
                "search_term": "sample sample-sample@sample.com 000-000-0000"
            }
        }
    ]
}
```

#### GET /api/contacts/{event_id}/

- General:
  - Returns a list of contact us object, and success value
- Sample: `curl http://127.0.0.1:8000/api/contacts/FB1010000000166329028254989355/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "6323cbb0002f0020a7730e9e",
            "eventId": "FB1010000000166329028254989355",
            "contacts": {
                "full_name": "sample",
                "email": "sample@sample.com",
                "message": "sample message",
                "search_term": "sample-sample@sample.com"
            }
        }
    ]
}
```

#### POST /api/contacts/

- General:
  - Creates a new contact us using the submitted json data, Returns the detail of the created contact us, success value, and event id.
- `curl http://127.0.0.1:8000/api/contacts/ -X POST -H "Content-Type: application/json" -d '{ "full_name": "sample", "email": "sample@sample.com", "message": "sample message"}'`

- You can also open the link `http://127.0.0.1:8000/api/contacts/` in a browser and perform the post operation

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "6323cbb0002f0020a7730e9e",
            "eventId": "FB1010000000166329028254989355",
            "contacts": {
                "full_name": "sample",
                "email": "sample@sample.com",
                "message": "sample message",
                "search_term": "sample-sample@sample.com"
            }
        }
    ]
}
```


#### PUT /api/contacts/{event_id}/

- General:
  - Update contact us using the submitted json data, Returns the detail of the updated contact us, success value, and event id.
- `curl http://127.0.0.1:8000/api/contacts/FB1010000000166329028254989355/ -X POST -H "Content-Type: application/json" -d '{ "full_name": "Some Sample", "email": "sample@sample.com", "message": "sample message"}'`

- You can also open the link `http://127.0.0.1:8000/api/contacts/FB1010000000166329028254989355/` in a browser and perform the post operation

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "6323cbb0002f0020a7730e9e",
            "eventId": "FB1010000000166329028254989355",
            "contacts": {
                "full_name": "Some Sample",
                "email": "sample@sample.com",
                "message": "sample message",
                "search_term": "Some Sample-sample@sample.com"
            }
        }
    ]
}
```

#### POST /api/attachments/

- General:
  - Upload a new file into the filesystems using the submitted json data, Returns the detail of the file uploaded and, success value.
- You can also open the link `http://127.0.0.1:8000/api/attachments/` in a browser and perform the post operation

```
{
    "isSuccess": true,
    "file_data": {
        "filename": "img_99347a0b-646d-47ce-82f7-43df2bbf2031.png",
        "actual_filename": "working-hours-06-09-2022.PNG",
        "file_extension": "png"
    }
}
```



### Licenses Comparison API


#### GET /api/comparisons/

- General:
  - Returns a list of license compared objects, and success value
- Sample: `curl http://127.0.0.1:8000/api/comparisons/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "637c621567b305d5f898ed0b",
            "eventId": "FB1010000000166909595159447637",
            "attributes": {
                "attribute_type": "comparisions",
                "identifier": "FB1010000000166184126356826496-FB1010000000016618418385506453,FB1010000000016618418385506453-FB1010000000166184126356826496",
                "license_1_event_id": "FB1010000000166184126356826496",
                "license_2_event_id": "FB1010000000016618418385506453",
                "license_1_logo_url": "https://100080.pythonanywhere.com/media/img/img_585981ab-f2b2-4b35-9ce3-aa4934ee136b.png",
                "license_2_logo_url": "https://100080.pythonanywhere.com/media/img/img_e1f47ce3-de18-491f-ab27-9e73ee0988a0.png",
                "license_1_name": "Apache License<V.2.0>",
                "license_2_name": "Mozilla Public License 2.0",
                "license_1_version": "2.0",
                "license_2_version": "2.0",
                "comparisions": [
                    {
                        "category": "Code Is Protected By Copy Right",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "No"
                        },
                        "_id": "bf973166-f37b-428c-b869-23ad164014eb"
                    },
                    {
                        "category": "Code can be use in close project",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "Yes"
                        },
                        "_id": "822502c9-6129-416b-baf0-0312e5d77236"
                    },
                    {
                        "category": "Code That Uses The Software Can Be Sold Commercially",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "No"
                        },
                        "_id": "8b4db3b8-22a7-4226-a91c-bd7d3301d075"
                    },
                    {
                        "category": "Code That Uses The Software Can Be Sold Commercially",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "No"
                        },
                        "_id": "ca6a97b0-409b-4856-ba22-d1fc55a87956"
                    }
                ]
            }
        }
    ]
}
```

#### GET /api/comparisons/{event_id}/

- General:
  - Returns specific license compared object, and success value
- Sample: `curl http://127.0.0.1:8000/api/comparisons/FB1010000000166909595159447637/` or open link in a browser

```{
    "isSuccess": true,
    "data": [
        {
            "_id": "637c621567b305d5f898ed0b",
            "eventId": "FB1010000000166909595159447637",
            "attributes": {
                "attribute_type": "comparisions",
                "identifier": "FB1010000000166184126356826496-FB1010000000016618418385506453,FB1010000000016618418385506453-FB1010000000166184126356826496",
                "license_1_event_id": "FB1010000000166184126356826496",
                "license_2_event_id": "FB1010000000016618418385506453",
                "license_1_logo_url": "https://100080.pythonanywhere.com/media/img/img_585981ab-f2b2-4b35-9ce3-aa4934ee136b.png",
                "license_2_logo_url": "https://100080.pythonanywhere.com/media/img/img_e1f47ce3-de18-491f-ab27-9e73ee0988a0.png",
                "license_1_name": "Apache License<V.2.0>",
                "license_2_name": "Mozilla Public License 2.0",
                "license_1_version": "2.0",
                "license_2_version": "2.0",
                "comparisions": [
                    {
                        "category": "Code Is Protected By Copy Right",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "No"
                        },
                        "_id": "bf973166-f37b-428c-b869-23ad164014eb"
                    },
                    {
                        "category": "Code can be use in close project",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "Yes"
                        },
                        "_id": "822502c9-6129-416b-baf0-0312e5d77236"
                    },
                    {
                        "category": "Code That Uses The Software Can Be Sold Commercially",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "No"
                        },
                        "_id": "8b4db3b8-22a7-4226-a91c-bd7d3301d075"
                    },
                    {
                        "category": "Code That Uses The Software Can Be Sold Commercially",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "No"
                        },
                        "_id": "ca6a97b0-409b-4856-ba22-d1fc55a87956"
                    }
                ]
            }
        }
    ]
}
```

#### POST /api/comparisons/

- General:
  - Creates a new license compared object using the submitted json data, Returns the detail of the created license compared object, success value, and event id.
- `curl http://127.0.0.1:8000/api/comparisons/ -X POST -H "Content-Type: application/json" -d '{ "license_1_event_id": "FB101000000001661841838550645", "license_2_event_id": "FB10100000001661841263568264"}'`

- You can also open the link `http://127.0.0.1:8000/api/comparisons/` in a browser and perform the post operation

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "637c621567b305d5f898ed0b",
            "eventId": "FB1010000000166909595159447637",
            "attributes": {
                "attribute_type": "comparisions",
                "identifier": "FB1010000000166184126356826496-FB1010000000016618418385506453,FB1010000000016618418385506453-FB1010000000166184126356826496",
                "license_1_event_id": "FB1010000000166184126356826496",
                "license_2_event_id": "FB1010000000016618418385506453",
                "license_1_logo_url": "https://100080.pythonanywhere.com/media/img/img_585981ab-f2b2-4b35-9ce3-aa4934ee136b.png",
                "license_2_logo_url": "https://100080.pythonanywhere.com/media/img/img_e1f47ce3-de18-491f-ab27-9e73ee0988a0.png",
                "license_1_name": "Apache License<V.2.0>",
                "license_2_name": "Mozilla Public License 2.0",
                "license_1_version": "2.0",
                "license_2_version": "2.0",
                "comparisions": []
}
```


### License Category Comparisons

#### GET /api/comparisons/{event_id}/

- General:
  - Returns a list of category comparisons objects, and success value
- Sample: `curl http://127.0.0.1:8000/api/comparisons/FB1010000000166909595159447637/` or open link in a browser

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "637c621567b305d5f898ed0b",
            "eventId": "FB1010000000166909595159447637",
            "attributes": {
                "attribute_type": "comparisions",
                "identifier": "FB1010000000166184126356826496-FB1010000000016618418385506453,FB1010000000016618418385506453-FB1010000000166184126356826496",
                "license_1_event_id": "FB1010000000166184126356826496",
                "license_2_event_id": "FB1010000000016618418385506453",
                "license_1_logo_url": "https://100080.pythonanywhere.com/media/img/img_585981ab-f2b2-4b35-9ce3-aa4934ee136b.png",
                "license_2_logo_url": "https://100080.pythonanywhere.com/media/img/img_e1f47ce3-de18-491f-ab27-9e73ee0988a0.png",
                "license_1_name": "Apache License<V.2.0>",
                "license_2_name": "Mozilla Public License 2.0",
                "license_1_version": "2.0",
                "license_2_version": "2.0",
                "comparisions": [
                    {
                        "category": "Code Is Protected By Copy Right",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "No"
                        },
                        "_id": "bf973166-f37b-428c-b869-23ad164014eb"
                    },
                    {
                        "category": "Code can be use in close project",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "Yes"
                        },
                        "_id": "822502c9-6129-416b-baf0-0312e5d77236"
                    },
                    {
                        "category": "Code That Uses The Software Can Be Sold Commercially",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "No"
                        },
                        "_id": "8b4db3b8-22a7-4226-a91c-bd7d3301d075"
                    },
                    {
                        "category": "Code That Uses The Software Can Be Sold Commercially",
                        "licience_1": {
                            "name": "Apache License<V.2.0>",
                            "comparision_value": "Yes"
                        },
                        "licience_2": {
                            "name": "Mozilla Public License 2.0",
                            "comparision_value": "No"
                        },
                        "_id": "ca6a97b0-409b-4856-ba22-d1fc55a87956"
                    }
                ]
            }
        }
    ]
}
```

#### POST /api/comparisons/{event_id}/

- General:
  - Creates a new license category comparison object using the submitted json data, Returns the detail of the created comparison object, success value, and event id.
- `curl http://127.0.0.1:8000/api/comparisons/FB1010000000166909595159447637/ -X POST -H "Content-Type: application/json" -d '{ "action_type": "add-license-category-comparison",
    "comparision":{
        "category": "Code That Uses The Software Can Be Sold Commercially",
        "licience_1":{
            "name": "Apache License<V.2.0>",
            "comparision_value": "Yes"
        },
        "licience_2":{
            "name": "Mozilla Public License 2.0",
            "comparision_value": "No"
        }
    }
}'`

- You can also open the link `http://127.0.0.1:8000/api/comparisons/FB1010000000166909595159447637/` in a browser and perform the post operation

```
{
    "isSuccess": true,
    "comparison": {
        "category": "Code That Uses The Software Can Be Sold Commercially",
        "licence_1": {
            "name": "Apache License<V.2.0>",
            "comparison_value": "Yes"
        },
        "licence_2": {
            "name": "Mozilla Public License 2.0",
            "comparison_value": "No"
        },
        "_id": "23d48791-07cc-47b5-8470-b59bba76773b"
    }
}
```


#### PUT /api/comparisons/{event_id}/

- General:
  - Update license category comparison object using the submitted json data, Returns the detail of the created comparison object, success value, and event id.
- `curl http://127.0.0.1:8000/api/comparisons/FB1010000000166909595159447637/ -X POST -H "Content-Type: application/json" -d '{
    "action_type": "update-license-category-comparison",
    "comparision_id": "d38b9497-c207-4288-a1f0-31ca8e9a1fad",
    "comparision":{
        "category": "Code Is Protected By Copy Right",
        "licience_1":{
            "name": "Apache License<V.2.0>",
            "comparision_value": "Yes"
        },
        "licience_2":{
            "name": "Mozilla Public License 2.0",
            "comparision_value": "No"
        }
    }
}
'`

- You can also open the link `http://127.0.0.1:8000/api/comparisons/FB1010000000166909595159447637/` in a browser and perform the post operation

```
{
    "isSuccess": true,
    "comparison": {
        "category": "Code Is Protected By Copy Right",
        "licence_1": {
            "name": "Apache License<V.2.0>",
            "comparison_value": "Yes"
        },
        "licence_2": {
            "name": "Mozilla Public License 2.0",
            "comparison_value": "No"
        },
        "_id": "d38b9497-c207-4288-a1f0-31ca8e9a1fad"
    }
}
```
