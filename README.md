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
- `curl http://127.0.0.1:8000/api/licenses/ -X POST -H "Content-Type: application/json" -d ' {
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
    ],

    
    "permissions": [
        "Commercial Use",
        "Distribute",
        "Distribution",
        "Modify",
        "Modification",
        "Patent Use",
        "Private Use",
        "Place Warranty",
        "Sublicense",
        "Use Patent Claims"
    ],
    "conditions": [
        "License and Copyright notice",
        "State Changes",
        "Include Original",
        "Disclose Source",
        "Include Copyright",
        "Include License",
        "Include Notice",
        "Give Credit"
    ],
    "limitations": [
        "Liability",
        "Use Trademark",
        "Warranty",
        "Sublicense",
        "Hold Liable"
    ],
    "references": [
        {
            "action": "Distribution of the code to third parties",
            "permission": "Yes"
        },
        {
            "action": "Modification of the code by a licensee",
            "permission": "Yes"
        },
        {
            "action": "May be used privately (e.g. internal use by a corporation)",
            "permission": "Yes"
        }

    ]
}'`

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
    "is_compatible": false,
    "license_comparison": {
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
        "comparisons": [
            {
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
        ],
        "percentage_of_compatibility": 78,
        "recommendation": "power",
        "disclaimer": "power"
    }
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



#### DELETE /api/licenses/{event_id}/
- `curl http://127.0.0.1:8000/api/licenses/FB1010000000167015140150633419/ -X DELETE -H "Content-Type: application/json"`

```
{
    "event_id": "FB1010000000167015140150633419",
    "isSuccess": true
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
                            "agreement_compliance_type": "software-license-policy",
                            "organization_id": "ROD345OS443345OS443OSS",
                            "date_of_execution_of_document": "2025-10-20",
                            "party_1_entity_type": "Individual",
                            "party_1_full_name": "Party 1 Name 1",
                            "party_1_postal_address": "P.O.BOX 45, India",
                            "party_1_jurisdiction_incorporated": "sample law",
                            "party_1_registration_number": "RS5428888",
                            "party_1_registrar_office_address_1": "sample office address",
                            "party_1_registrar_office_address_2": "",
                            "party_1_registrar_office_address_3": "",
                            "party_1_principal_place_of_business": "India",
                            "party_2_entity_type": "Organization",
                            "party_2_full_name": "Party 2 Name",
                            "party_2_postal_address": "P.O.BOX 45, USA",
                            "party_2_jurisdiction_incorporated": "USA",
                            "party_2_registration_number": "RS5428845888",
                            "party_2_registrar_office_address_1": "sample office address",
                            "party_2_registrar_office_address_2": "badu street",
                            "party_2_registrar_office_address_3": "",
                            "party_2_principal_place_of_business": "USA",
                            "charges_payable": 3000.15,
                            "software_document_identification": "software",
                            "contract_effective_date": "2023-02-20",
                            "minimum_terms_apply": 45,
                            "minimum_terms_apply_unit": "Days",
                            "is_software_form_specified": true,
                            "software_form": "software spic",
                            "is_non_material_defects_count_as_software_defects": false,
                            "ways_defect_affect_software": "example",
                            "is_set_of_exclusions_included": false,
                            "exclusions_apply": "",
                            "software_specification": "87 linux",
                            "can_software_specification_be_varied_by_the_parties": true,
                            "terms_of_contract_duration": 50,
                            "terms_of_contract_duration_unit": "Months",
                            "is_inline_copy_right_remove": false,
                            "is_term_of_contract_indefinite": false,
                            "contract_termination_date": "2022-10-20",
                            "events_that_will_cause_contract_to_be_terminated": "Nil",
                            "number_of_license_to_be_deliver": 4,
                            "number_of_license_to_be_deliver_unit": "pcs",
                            "software_delivery_channel": "Email",
                            "within_what_period_must_software_be_delivered": 12,
                            "within_what_period_must_software_be_delivered_unit": "Days",
                            "what_did_licensor_supply_to_the_licensee": "software",
                            "purpose_by_reference_to_which_sub_licensing_is_permitted": "Use For",
                            "when_should_invoice_be_issued": "Nil",
                            "invoicing_date": "2022-10-20",
                            "period_for_payment_of_invoices": 85,
                            "period_for_payment_of_invoices_unit": "Days",
                            "effective_date_for_invoice_payment": "2022-10-20",
                            "invoice_payment_method": "Nil",
                            "interest_rate_apply_to_late_payment": 2450.55,
                            "optional_element": "",
                            "is_warranty_relate_to_a_specific_period": true,
                            "scope_of_warranty": "Nil",
                            "jurisdictional_coverage_of_warranty": "Nil",
                            "period_apply_to_warranty": 3,
                            "period_apply_to_warranty_unit": "Months",
                            "circumstances_in_which_licensor_may_exercise_its_rights": "Nil",
                            "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false,
                            "are_there_limitations_on_right_to_modify": false,
                            "limitations_on_right_to_modify_specification": "Nil",
                            "termination_notice_period_apply": 3,
                            "termination_notice_period_apply_unit": "Months",
                            "is_termination_period_expirable": false,
                            "relevant_termination_period": 0,
                            "relevant_termination_period_unit": "Days",
                            "relevant_termination_period_date": "2022-10-20",
                            "circumstances_in_which_a_party_may_terminate_for_breach": "Nil",
                            "time_frame_for_the_notice_period": 0,
                            "time_frame_for_the_notice_period_unit": "Months",
                            "sent_contractual_notices_to_the_licensor_name": "Nil",
                            "sent_contractual_notices_to_the_licensor_address_1": "Nil",
                            "sent_contractual_notices_to_the_licensor_address_2": "Nil",
                            "sent_contractual_notices_to_the_licensor_address_3": "Nil",
                            "sent_contractual_notices_to_the_licensor_contact_details": "Nil",
                            "sent_contractual_notices_to_the_licensee_name": "Nil",
                            "sent_contractual_notices_to_the_licensee_address_1": "Nil",
                            "sent_contractual_notices_to_the_licensee_address_2": "Nil",
                            "sent_contractual_notices_to_the_licensee_address_3": "Nil",
                            "sent_contractual_notices_to_the_licensee_contact_details": "Nil",
                            "law_governs_document": "Nil",
                            "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "Nil",
                            "which_entity_will_sign_contract_on_behalf_of_party_1": "Contractor",
                            "party_1_signatory_scanned_copy_detail": {
                                "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                                "actual_filename": "AFL.png",
                                "file_extension": "png",
                                "url": "https://100080.pythonanywhere.com/media/img/img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png"
                            },
                            "full_name_of_party_1_signatory": "party 1 name",
                            "party_1_date_of_signing_contract": "2022-11-02",
                            "full_name_of_the_person_sign_on_behalf_of_party_1": "witness 1 name",
                            "date_contract_was_sign_on_behalf_of_party_1": "2022-11-02",
                            "which_entity_will_sign_contract_on_behalf_of_party_2": "Contractor",
                            "party_2_signatory_scanned_copy_detail": {
                                "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                                "actual_filename": "AFL.png",
                                "file_extension": "png",
                                "url": "https://100080.pythonanywhere.com/media/img/img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png"
                            },
                            "full_name_of_party_2_signatory": "party 2 name",
                            "party_2_date_of_signing_contract": "2022-11-05",
                            "full_name_of_the_person_sign_on_behalf_of_party_2": "witness 2 name",
                            "date_contract_was_sign_on_behalf_of_party_2": "2022-11-05"

                        }

        }
    ]
}
```

#### POST /api/agreements/

- General:
  - Creates a new software agreement using the submitted json data, Returns the detail of the created agreement, success value, and event id.
- `curl http://127.0.0.1:8000/api/agreements/ -X POST -H "Content-Type: application/json" -d '{
                "agreement_compliance_type": "software-license-policy",
                "date_of_execution_of_document": "2025-10-20",
                "party_1_entity_type": "Individual",
                "party_1_full_name": "Party 1 Name 1",
                "party_1_postal_address": "P.O.BOX 45, India",
                "party_1_jurisdiction_incorporated": "sample law",
                "party_1_registration_number": "RS5428888",
                "party_1_registrar_office_address_1": "sample office address",
                "party_1_registrar_office_address_2": "",
                "party_1_registrar_office_address_3": "",
                "party_1_principal_place_of_business": "India",
                "party_2_entity_type": "Organization",
                "party_2_full_name": "Party 2 Name",
                "party_2_postal_address": "P.O.BOX 45, USA",
                "party_2_jurisdiction_incorporated": "USA",
                "party_2_registration_number": "RS5428845888",
                "party_2_registrar_office_address_1": "sample office address",
                "party_2_registrar_office_address_2": "badu street",
                "party_2_registrar_office_address_3": "",
                "party_2_principal_place_of_business": "USA",
                "charges_payable": 3000.15,
                "software_document_identification": "software",
                "contract_effective_date": "2023-02-20",
                "minimum_terms_apply": 45,
                "minimum_terms_apply_unit": "Days",
                "is_software_form_specified": true,
                "software_form": "software spic",
                "is_non_material_defects_count_as_software_defects": false,
                "ways_defect_affect_software": "example",
                "is_set_of_exclusions_included": false,
                "exclusions_apply": "",
                "software_specification": "87 linux",
                "can_software_specification_be_varied_by_the_parties": true,
                "terms_of_contract_duration": 50,
                "terms_of_contract_duration_unit": "Months",
                "is_inline_copy_right_remove": false,
                "is_term_of_contract_indefinite": false,
                "contract_termination_date": "2022-10-20",
                "events_that_will_cause_contract_to_be_terminated": "Nil",
                "number_of_license_to_be_deliver": 4,
                "number_of_license_to_be_deliver_unit": "pcs",
                "software_delivery_channel": "Email",
                "within_what_period_must_software_be_delivered": 12,
                "within_what_period_must_software_be_delivered_unit": "Days",
                "what_did_licensor_supply_to_the_licensee": "software",
                "purpose_by_reference_to_which_sub_licensing_is_permitted": "Use For",
                "when_should_invoice_be_issued": "Nil",
                "invoicing_date": "2022-10-20",
                "period_for_payment_of_invoices": 85,
                "period_for_payment_of_invoices_unit": "Days",
                "effective_date_for_invoice_payment": "2022-10-20",
                "invoice_payment_method": "Nil",
                "interest_rate_apply_to_late_payment": 2450.55,
                "optional_element": "",
                "is_warranty_relate_to_a_specific_period": true,
                "scope_of_warranty": "Nil",
                "jurisdictional_coverage_of_warranty": "Nil",
                "period_apply_to_warranty": 3,
                "period_apply_to_warranty_unit": "Months",
                "circumstances_in_which_licensor_may_exercise_its_rights": "Nil",
                "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false,
                "are_there_limitations_on_right_to_modify": false,
                "limitations_on_right_to_modify_specification": "Nil",
                "termination_notice_period_apply": 3,
                "termination_notice_period_apply_unit": "Months",
                "is_termination_period_expirable": false,
                "relevant_termination_period": 0,
                "relevant_termination_period_unit": "Days",
                "relevant_termination_period_date": "2022-10-20",
                "circumstances_in_which_a_party_may_terminate_for_breach": "Nil",
                "time_frame_for_the_notice_period": 0,
                "time_frame_for_the_notice_period_unit": "Months",
                "sent_contractual_notices_to_the_licensor_name": "Nil",
                "sent_contractual_notices_to_the_licensor_address_1": "Nil",
                "sent_contractual_notices_to_the_licensor_address_2": "Nil",
                "sent_contractual_notices_to_the_licensor_address_3": "Nil",
                "sent_contractual_notices_to_the_licensor_contact_details": "Nil",
                "sent_contractual_notices_to_the_licensee_name": "Nil",
                "sent_contractual_notices_to_the_licensee_address_1": "Nil",
                "sent_contractual_notices_to_the_licensee_address_2": "Nil",
                "sent_contractual_notices_to_the_licensee_address_3": "Nil",
                "sent_contractual_notices_to_the_licensee_contact_details": "Nil",
                "law_governs_document": "Nil",
                "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "Nil",
                "which_entity_will_sign_contract_on_behalf_of_party_1": "Contractor",
                "party_1_signatory_scanned_copy_detail": {
                    "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                    "actual_filename": "AFL.png",
                    "file_extension": "png",
                    "url": "https://100080.pythonanywhere.com/media/img/img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png"
                },
                "full_name_of_party_1_signatory": "party 1 name",
                "party_1_date_of_signing_contract": "2022-11-02",
                "full_name_of_the_person_sign_on_behalf_of_party_1": "witness 1 name",
                "date_contract_was_sign_on_behalf_of_party_1": "2022-11-02",
                "which_entity_will_sign_contract_on_behalf_of_party_2": "Contractor",
                "party_2_signatory_scanned_copy_detail": {
                    "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                    "actual_filename": "AFL.png",
                    "file_extension": "png",
                    "url": "https://100080.pythonanywhere.com/media/img/img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png"
                },
                "full_name_of_party_2_signatory": "party 2 name",
                "party_2_date_of_signing_contract": "2022-11-05",
                "full_name_of_the_person_sign_on_behalf_of_party_2": "witness 2 name",
                "date_contract_was_sign_on_behalf_of_party_2": "2022-11-05"

            }


'`

- You can also open the link `http://127.0.0.1:8000/api/agreements/` in a browser and perform the post operation

## Request body

### Software Agreement
```
{
            "agreement_compliance_type": "software-license-policy",
            "organization_id": "ROD345OS443345OS443OSS",
            "date_of_execution_of_document": "2025-10-20",
            "party_1_entity_type": "Individual",
            "party_1_full_name": "Party 1 Name 1",
            "party_1_postal_address": "P.O.BOX 45, India",
            "party_1_jurisdiction_incorporated": "sample law",
            "party_1_registration_number": "RS5428888",
            "party_1_registrar_office_address_1": "sample office address",
            "party_1_registrar_office_address_2": "",
            "party_1_registrar_office_address_3": "",
            "party_1_principal_place_of_business": "India",
            "party_2_entity_type": "Organization",
            "party_2_full_name": "Party 2 Name",
            "party_2_postal_address": "P.O.BOX 45, USA",
            "party_2_jurisdiction_incorporated": "USA",
            "party_2_registration_number": "RS5428845888",
            "party_2_registrar_office_address_1": "sample office address",
            "party_2_registrar_office_address_2": "badu street",
            "party_2_registrar_office_address_3": "",
            "party_2_principal_place_of_business": "USA",
            "charges_payable": 3000.15,
            "software_document_identification": "software",
            "contract_effective_date": "2023-02-20",
            "minimum_terms_apply": 45,
            "minimum_terms_apply_unit": "Days",
            "is_software_form_specified": true,
            "software_form": "software spic",
            "is_non_material_defects_count_as_software_defects": false,
            "ways_defect_affect_software": "example",
            "is_set_of_exclusions_included": false,
            "exclusions_apply": "",
            "software_specification": "87 linux",
            "can_software_specification_be_varied_by_the_parties": true,
            "terms_of_contract_duration": 50,
            "terms_of_contract_duration_unit": "Months",
            "is_inline_copy_right_remove": false,
            "is_term_of_contract_indefinite": false,
            "contract_termination_date": "2022-10-20",
            "events_that_will_cause_contract_to_be_terminated": "Nil",
            "number_of_license_to_be_deliver": 4,
            "number_of_license_to_be_deliver_unit": "pcs",
            "software_delivery_channel": "Email",
            "within_what_period_must_software_be_delivered": 12,
            "within_what_period_must_software_be_delivered_unit": "Days",
            "what_did_licensor_supply_to_the_licensee": "software",
            "purpose_by_reference_to_which_sub_licensing_is_permitted": "Use For",
            "when_should_invoice_be_issued": "Nil",
            "invoicing_date": "2022-10-20",
            "period_for_payment_of_invoices": 85,
            "period_for_payment_of_invoices_unit": "Days",
            "effective_date_for_invoice_payment": "2022-10-20",
            "invoice_payment_method": "Nil",
            "interest_rate_apply_to_late_payment": 2450.55,
            "optional_element": "",
            "is_warranty_relate_to_a_specific_period": true,
            "scope_of_warranty": "Nil",
            "jurisdictional_coverage_of_warranty": "Nil",
            "period_apply_to_warranty": 3,
            "period_apply_to_warranty_unit": "Months",
            "circumstances_in_which_licensor_may_exercise_its_rights": "Nil",
            "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false,
            "are_there_limitations_on_right_to_modify": false,
            "limitations_on_right_to_modify_specification": "Nil",
            "termination_notice_period_apply": 3,
            "termination_notice_period_apply_unit": "Months",
            "is_termination_period_expirable": false,
            "relevant_termination_period": 0,
            "relevant_termination_period_unit": "Days",
            "relevant_termination_period_date": "2022-10-20",
            "circumstances_in_which_a_party_may_terminate_for_breach": "Nil",
            "time_frame_for_the_notice_period": 0,
            "time_frame_for_the_notice_period_unit": "Months",
            "sent_contractual_notices_to_the_licensor_name": "Nil",
            "sent_contractual_notices_to_the_licensor_address_1": "Nil",
            "sent_contractual_notices_to_the_licensor_address_2": "Nil",
            "sent_contractual_notices_to_the_licensor_address_3": "Nil",
            "sent_contractual_notices_to_the_licensor_contact_details": "Nil",
            "sent_contractual_notices_to_the_licensee_name": "Nil",
            "sent_contractual_notices_to_the_licensee_address_1": "Nil",
            "sent_contractual_notices_to_the_licensee_address_2": "Nil",
            "sent_contractual_notices_to_the_licensee_address_3": "Nil",
            "sent_contractual_notices_to_the_licensee_contact_details": "Nil",
            "law_governs_document": "Nil",
            "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "Nil",
            "which_entity_will_sign_contract_on_behalf_of_party_1": "Contractor",
            "party_1_signatory_scanned_copy_detail": {
                "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                "file_extension": "png",
            },
            "full_name_of_party_1_signatory": "party 1 name",
            "party_1_date_of_signing_contract": "2022-11-02",
            "full_name_of_the_person_sign_on_behalf_of_party_1": "witness 1 name",
            "date_contract_was_sign_on_behalf_of_party_1": "2022-11-02",
            "which_entity_will_sign_contract_on_behalf_of_party_2": "Contractor",
            "party_2_signatory_scanned_copy_detail": {
                "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                "file_extension": "png",
            },
            "full_name_of_party_2_signatory": "party 2 name",
            "party_2_date_of_signing_contract": "2022-11-05",
            "full_name_of_the_person_sign_on_behalf_of_party_2": "witness 2 name",
            "date_contract_was_sign_on_behalf_of_party_2": "2022-11-05"

}



```

### EULA
```
 {
                "agreement_compliance_type": "eula",
                "organization_id": "ROD345OS443345OS443OSS",
                "date_of_execution_of_document": "2025-10-20",
                "party_details_full_name": "Individual and Company",
                "party_details_company_name": "Dowell Research 1",
                "party_details_address_line_1": "P.O.BOX 45, India",
                "party_details_address_line_2": "sample law",
                "party_details_address_line_3": "RS5428888",
                "party_details_country": "India",
                "party_details_state": "India",
                "party_details_zipcode": "RT455",
                "party_details_phone": "+255459996665",
                "party_details_email": "sample@email.com",
                "company_details_nature_of_company": "Individual",
                "software_product": "Sample 2",
                "software_product_license_name": "Sample Mix",
                "software_product_license_name_uc": "",
                "liability_remedy_amount": 2542.45,
                "state_law_applies": "India",
                "jurisdiction_city": "Mobai",
                "jurisdiction_state": "India",
                "date_of_commencement": "2025-10-20",
                "is_maintenance_or_support_available_for_app": true,
                "will_it_state_number_of_maintenance_and_schedules": true,
                "at_which_point_will_users_be_bound_by_terms": "When They Download",
                "will_users_be_able_to_install_app_on_multiple_device": false,
                "violations_that_enable_app_provider_to_cancel_agreement": "When change software spic"
            }
```

### MOU
```
{
    "agreement_compliance_type": "mou",
    "organization_id": "ROD345OS443345OS443OSS",
    "date_of_execution_of_document": "2025-10-20",
    "party_1_entity_type": "Organization",
    "party_1_full_name": "Software Own",
    "party_1_address_line_1": "P.O.BOX 45, India",
    "party_1_address_line_2": "sample law",
    "party_1_address_line_3": "RS5428888",
    "party_1_zipcode": "Mobai",
    "party_1_state": "India",
    "party_1_country": "India",
    "party_1_period_mentioned": 50,
    "party_1_period_mentioned_unit": "Days",
    "party_2_entity_type": "Individual",
    "party_2_full_name": "sample",
    "party_2_address_line_1": "Individual",
    "party_2_address_line_2": "Sample 2",
    "party_2_address_line_3": "Sample Mix",
    "party_2_zipcode": "+254",
    "party_2_state": "India",
    "party_2_country": "India",
    "party_2_period_mentioned": 45,
    "party_2_period_mentioned_unit": "Months",
    "what_will_be_the_purpose_of_this_mou": "India",
    "what_is_the_objective_of_this_mou": "contract",
    "date_of_commencement": "2025-10-20",
    "date_of_termination": "2025-10-20",
    "period_for_notice_in_case_of_cancellation_or_amendment": 50,
    "period_for_notice_in_case_of_cancellation_or_amendment_unit": "Days",
    "state_of_laws_use_as_governing_laws": "India",
    "state_of_laws_for_governing_laws_in_case_of_reimbursement": "India",
    "number_of_parties_enter_this_mou": 5,
    "mou_include_confidentiality": true,
    "mou_retrict_working_with_competitors": false,
    "period_mou_retrict_working_with_competitors": 50,
    "period_mou_retrict_working_with_competitors_unit": "Days",
    "date_for_legally_binding_definitive_agreement": "2025-10-20",
    "should_the_parties_agree_to_refrain_from_negotiating_with_third_parties": false,
    "will_mou_agreement_be_terminated_in_case_of_force_majeure": true,
    "any_other_contracts_entered_between_parties_together_with_this_mou": true,

    "project_name": "",
    "project_detail": ""
}
```

### Website Terms Of Use
```
{
    "agreement_compliance_type": "website-terms-of-use",
    "organization_id": "ROD345OS443345OS443OSS",
    "terms_last_updated": "2025-10-20",
    "full_name_of_the_party": "Website Owner",
    "website_url": "www.website.come",
    "email_id": "example@website.com",
    "email_id_for_acquiring_written_permission": "example1@website.com",
    "liability_limit_amount": 5240.00,
    "liability_limit_amount_currency": "USD",
    "liability_must_not_exceed_amount": 6000,
    "liability_must_not_exceed_amount_currency": "USD",
    "email_id_for_requesting_access_or_correction_of_personal_info": "example3@website.com"
}
```

### Website Privacy Policy
```
{
    "agreement_compliance_type": "website-privacy-policy",
    "organization_id": "ROD345OS443345OS443OSS",
    "last_updated": "2025-10-20",
    "company_name": "SamPle",
    "company_address": "sample street",
    "registration_number": "7845587457",
    "country": "India",
    "website_name": "SamPle",
    "website_url": "www.sample.com",
    "website_contact_page_url": "www.sample.com/contact",
    "website_contact_email": "info@sample.com"
}
```

### Website Security Policy
```
{
    "agreement_compliance_type": "website-security-policy",
    "organization_id": "ROD345OS443345OS443OSS",
    "last_updated": "2025-10-20",
    "company_name": "SamPle",
    "website_name": "SamPle",
    "jurisdiction": "India",
    "website_url": "www.sample.com",
    "website_contact_email": "info@sample.com"
}
```


### Non Compete Agreement
```
 {
    "agreement_compliance_type": "non-compete-agreement",
    "organization_id": "ROD345OS443345OS443OSS",
    "date_of_execution_of_document": "2025-10-20",
    "party_full_name": "Individual and Company",
    "company_name": "Dowell Research 1",
    "company_address_line_1": "P.O.BOX 45, India",
    "company_address_line_2": "sample law",
    "company_address_line_3": "RS5428888",
    "company_zipcode": "India",
    "type_of_company": "India",
    "restricted_area": "RT455",
    "date_of_termination": "2025-10-20",
    "duration_for_solicit": 54,
    "duration_for_solicit_unit": "Days",
    "governing_laws_country": "Sample 2",
    "will_there_be_a_litigation_matter_in_case_of_dispute": false,
    "which_state_should_abide_litigation_matter": "",
    "will_electronic_notices_be_allowed": "yes",
    "name_of_witnesses": "Seth",
    "signature_of_witnesses_detail": {
                "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                "file_extension": "png",
            },

    "company_nature_of_work": "",
    "employee_job_title": ""

}

```


### Cookies policy
```
{
    "agreement_compliance_type": "cookie-policy",
    "organization_id": "ROD345OS443345OS443OSS",
    "date_of_execution_of_document": "2025-10-20",
    "party_full_name": "Individual and Company",
    "will_the_cookie_store_personal_information": true,
    "type_of_personal_information_store_by_cookies": ["Email", "Phone"],
    "other_type_of_personal_information_store_by_cookies": "Nil",
    "does_your_website_or_app_use_essential_cookies": true,
    "does_your_website_or_app_use_any_perfomance_and_functionality_cookies": false,
    "does_your_website_or_app_use_marketing_cookies": true,
    "does_your_website_or_app_use_analytic_and_customization_cookies": true,
    "does_your_website_or_app_use_social_media_cookies": true,
    "does_your_website_or_app_use_third_party_cookies": true,
    "personal_information_store_by_third_party_cookies": ["Email", "Phone", "IP Address"],
    "does_your_website_or_app_show_ads": true,
    "website_uses_other_technologies_to_perform_other_functions_achieved_via_cookie": true,
    "which_medium_can_website_users_raise_question_regarding_cookies": {
        "email": "email@example.com",
        "website": "www.example.com"
    },
    "provide_situations_where_cookies_may_be_collected_without_consent_of_users": "",
    "name_of_third_party_cookies": "bitmake",
    "owner_of_third_party_cookies": "Sample 2"

}
```

### App Disclaimer
```
{
    "agreement_compliance_type": "app-disclaimer",
    "organization_id": "ROD345OS443345OS443OSS",
    "last_update": "2025-10-20",
    "app_name": "App"
}
```


### Return and Refund
```

{
    "agreement_compliance_type": "return-and-refund",
    "organization_id": "ROD345OS443345OS443OSS",
    "date": "2025-10-20",
    "website_or_app_name": "App 2",
    "company_info": "App 2",
    "website_url": "app.com",
    "cancellation_right_of_order": 50,
    "cancellation_right_of_order_unit": "Months",
    "reimbursement_of_cancellation_money": 2500.01,
    "reimbursement_of_cancellation_money_currency": "USD",
    "website_contact_email": "example@email.com"

}
```

### Non Disclosure Agreement
```
{
    "agreement_compliance_type": "nda",
    "organization_id": "ROD345OS443345OS443OSS",
    "party_1_full_name": "Party 1 Name 2",
    "party_1_address_line_1": "India Street",
    "party_1_address_line_2": "",
    "party_1_address_line_3": "",
    "party_1_country": "India",
    "party_1_city": "Mbadu",
    "party_1_state": "Mbadu",
    "party_1_zipcode": "4545",
    "party_2_full_name": "Party 1 Name",
    "party_2_address_line_1": "India Street",
    "party_2_address_line_2": "",
    "party_2_address_line_3": "",
    "party_2_country": "India",
    "party_2_city": "Mbadu",
    "party_2_state": "Mbadu",
    "party_2_zipcode": "4545",
    "what_shall_be_the_of_term_this_agrement": 0,
    "what_shall_be_the_of_term_this_agrement_unit": "Months",
    "what_shall_be_the_governing_this_law_this_agrement": "India Law",
    "date_of_execution_of_document": "2025-10-20",
    "number_of_witness": 2,
    "witnesses": [
        {
            "full_name": "Witness 1",
            "address_line_1": "Witness 1 Street",
            "address_line_2": "",
            "address_line_3": ""
        },
        {
            "full_name": "Witness 2",
            "address_line_1": "Witness 2 Street",
            "address_line_2": "",
            "address_line_3": ""
        },
        {
            "full_name": "Witness 3",
            "address_line_1": "Witness 3 Street",
            "address_line_2": "",
            "address_line_3": ""
        }
    ],
    "will_the_obligations_of_confidentiality_subsist_after_expiry": true,
    "what_will_be_the_date_for_termination_of_this_nda": "2025-10-20",
    "will_the_party_be_allow_to_enter_into_similar_arragements_with_other_party": true,
    "the_period_a_party_is_entitle_to_enter_into_similar_arragement_with_other_party": 5,
    "the_period_a_party_is_entitle_to_enter_into_similar_arragement_with_other_party_unit": "Months",
    "how_will_the_agreement_be_terminated": "Notice",
    "other_medium_agreement_can_be_terminated": ""
}
```


### App Privacy Policy
```
{
    "agreement_compliance_type": "app-privacy-policy",
    "organization_id": "ROD345OS443345OS443OSS",
    "last_update": "2025-10-20",
    "company_name": "Sample Ltd",
    "app_name": "App 1",
    "app_url": "http://app.com/app",
    "website_contact_page_url": "http://website.com/contact",
    "website_contact_email": "app@website.com"
}
```

### Discliamer For Website
```
{
    "agreement_compliance_type": "discliamer-for-website",
    "organization_id": "ROD345OS443345OS443OSS",
    "last_update": "2025-10-20",
    "effective_date": "2025-10-20",
    "jurisdiction": "India Law",
    "company_name": "Sample",
    "website_name": "Sample website",
    "website_url": "http://app.com/app",
    "website_contact_email": "app@website.com"
}
```


### Employment Contract
```
{
    "agreement_compliance_type": "employment-contract",
    "organization_id": "ROD345OS443345OS443OSS",
    "company_name": "company 1",
    "company_address_line_1": "India Mubai street",
    "company_address_line_2": "",
    "company_address_line_3": "",
    "employee_full_name": "employee 1",
    "type_of_business_the_company_engaged": "Information Technology",
    "start_date": "2025-10-20",
    "company_state": "Mubai",
    "company_country": "India",
    "duties_of_employee": "Work with developers to design algorithms and flowcharts. \nProduce clean, efficient code based on specifications.",
    "time_frame_of_the_compensation": "Days",
    "amount": 120.0,
    "amount_currency": "USD",
    "full_name_of_company_signatory": "company name",
    "company_signatory_scanned_copy_detail": {
                "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                "file_extension": "png",
            },
    "company_signatory_date": "2025-10-20",
    "full_name_of_employee_signatory": "",
    "employee_signatory_scanned_copy_detail": {},
    "employee_signatory_date": null,
    "jurisdiction": "India law",
    "employee_state": "Mubai",
    "employee_country": "India"


}
```


### Terms and Conditions
```
{
    "agreement_compliance_type": "terms-and-conditions",
    "organization_id": "ROD345OS443345OS443OSS",
    "last_update": "2025-10-20",
    "country_name": "India",
    "company_name": "Company Name Test",
    "website_or_app_name": "websiteexample",
    "website_url": "http://websiteexample.com/",
    "support_email": "access@example.com"

}
```

### Statement Of Work
```
{
    "agreement_compliance_type": "statement-of-work",
    "organization_id": "ROD345OS443345OS443OSS",
    "client_full_name": "Client Name",
    "jurisdiction": "India Law",
    "project_name": "Project",
    "effective_date": "2025-10-20",
    "freelancers_full_name": "Lancer",
    "freelancer_access": [
        "Client’s web hosting account (AWS)",
        "Client’s project management tool (Jira)"
    ],
    "what_is_the_goal_of_this_project": "nil",
    "deliverables_expected_in_this_scope_of_work": [
        "coding",
        "managing"
    ],
    "mode_of_communication_between_the_parties": "nil",
    "when_will_the_freelancer_share_his_status_on_deliverables": "2025-03-20T14:30:43",
    "when_will_the_progress_meetings_occur": "2025-03-20T14:30:43",
    "what_is_the_minimum_time_required_to_complete_this_project": 25,
    "what_is_the_minimum_time_required_to_complete_this_project_unit": "Days",
    "what_is_value_in_respect_to_time_required": 542.0,
    "what_is_value_in_respect_to_time_required_currency": "USD",
    "what_is_the_billing_rate": 250.0,
    "what_is_the_billing_rate_currency": "USD",
    "what_is_the_charges_for_rush_work": 560.0,
    "what_is_the_charges_for_rush_work_currency": "USD",
    "whom_should_the_invoices_be_submitted_to": "flash",
    "whom_should_the_invoices_be_submitted_to_department_name": "nil",
    "when_should_the_invoices_be_submitted": "2025-10-20",
    "when_will_the_invoices_be_payable_by_after_receipt": "2025-10-20"

}
```


### GDPR Privacy Policy
```
{
    "agreement_compliance_type": "gdpr-privacy-policy",
    "organization_id": "ROD345OS443345OS443OSS",
    "location": "india 1",
    "jurisdictional_laws": "India law",
    "privacy_policy_will_be_used_for": "Mobile App",
    "would_you_like_to_create_a_premium_privacy_policy": "Yes, I would like to create a premium privacy policy.",
    "do_you_operate_your_app_under_a_company_name": "No",
    "company_name": "",
    "does_your_company_have_a_short_or_trade_name": "No.",
    "short_or_trade_name_of_your_company": "",
    "can_users_sign_up_and_create_account_in_your_app": "Yes, users can sign up for an account.",
    "can_users_sign_up_using_social_media_and_other_third_party_service": "Yes, users can sign up using third-party services.",
    "can_users_view_and_change_their_personal_information": "Yes, users have full access to their personal information.",
    "can_users_delete_their_account_and_personal_information": "Yes, users can delete their accounts and personal information at any time.",
    "how_can_users_delete_their_account_and_personal_information": "They can log in to their account settings page to delete it.",
    "can_users_publish_anything_in_your_app": "Yes, users can submit and publish their own content.",
    "can_users_share_content_available_in_your_app": "Yes, content can be shared on social networks.",
    "can_users_interact_with_each_other_in_your_app": "Yes, users can interact with each other (via comments, messages, etc).",
    "when_users_interact_can_they_see_other_users_personally_identifiable_information": "Yes, personally identifiable information may be displayed.",
    "does_your_target_audience_include_resident_of_california_usa": "Yes, our target audience or users may include residents of California (required for the CCPA compliance).",
    "does_your_target_audience_include_resident_of_european_union": "Yes, our target audience or users may include residents in the European Union (required for the GDPR compliance).",
    "does_your_target_audience_include_those_under_the_age_of_18": "Yes, our target audience or users may include those under the age of 18.",
    "does_your_target_audience_include_those_under_the_age_of_13": "",
    "do_you_collect_any_information_from_children": "",
    "will_information_submitted_by_children_be_publicly_available": "",
    "is_there_an_option_to_keep_submitted_information_private": "",
    "items_apply_to_children_using_the_app": [],
    "do_you_currently_sell_or_plan_on_selling_products_or_services_in_your_app": "Yes, we sell products or services or plan to sell in the future.",
    "do_you_offer_products_or_services_provided_by_third_party_companies": "Yes, we offer products or services provided by third-party companies.",
    "do_you_have_security_measures_in_place_to_protect_sensitive_payment_information": "Yes, we’ve taken all the necessary measures to keep sensitive payment information secure.",
    "do_you_store_any_sensitive_payment_information": "Yes, we may store payment information for future purchases or recurring billing (such as credit card numbers or tokens).",
    "do_you_perform_credit_checks_on_your_customers_members_of_their_household": "Yes, we may perform credit checks.",
    "do_you_use_third_party_analytics_or_tracking_tools": "Yes, we use third-party analytics tools.",
    "do_you_anonymize_users_personal_information": "Yes, user’s personal information is anonymized to prevent analytics tools from linking it to an individual person.",
    "do_you_have_affiliate_links_in_your_app": "Yes, there may be affiliate links.",
    "do_you_display_ads_in_your_app": "Yes, there may be ads displayed.",
    "do_you_collect_users_data_for_remarketing": "Yes, we may do targeted advertising to users based on collected data.",
    "do_you_send_email_newsletters_to_users": "Yes, users can opt to receive email newsletters from us.",
    "do_you_send_push_notifications_to_your_users": "Yes, users can opt to receive push notifications from us.",
    "do_you_use_third_party_provider_to_send_push_notification": "Yes, we use a third-party provider to send push notifications.",
    "what_kind_of_information_do_you_collect_from_your_users": [
        "Account details (such as user name, unique user ID, password, etc)",
        "Contact information (such as email address, phone number, etc)"
    ],
    "will_you_be_requesting_access_to_the_geolocation_of_your_users": "Yes, we may request access to geolocation.",
    "will_you_be_requesting_access_to_various_features_on_yours_users_device": "Yes, we may request access to certain features.",
    "do_you_collect_any_derivative_data_from_your_users": "Yes, we may collect derivative data of our users.",
    "do_you_collect_users_personal_information_from_third_party_source": "Yes, we may collect personal information from third parties.",
    "what_will_you_do_with_the_information_you_collect": [
        "Create and manage user accounts",
        "Fulfill and manage orders"
    ],
    "do_you_combine_different_bits_of_personal_information": "Yes, we combine different bits of personal information to create consumer profiles.",
    "will_you_disclose_personal_information_to_business_affiliates": "Yes, we may disclose personal information to business affiliates.",
    "will_you_disclose_personal_information_to_third_parties": "Yes, we may disclose personal information to third parties.",
    "what_are_the_categories_of_third_parties_you_may_disclose_personal_information_to": [
        "Advertising networks",
        "Affiliate programs"
    ],
    "will_the_information_disclosed_to_third_parties_contain_any_personally_identifiable_details": "Yes, some personally identifiable information may be disclosed.",
    "will_you_disclose_personal_information_in_the_event_of_a_business_sale_or_merger": "Yes, we will disclose personal information with the purchaser.",
    "will_you_disclose_personal_information_to_law_enforcement_agencies_upon_lawful_requests": "Yes, we’ll disclose personal information upon lawful request.",
    "how_long_will_you_store_your_users_personal_information": "As long as necessary to comply with the regulations.",
    "what_is_the_maximum_time_you_will_store_users_personal_information": 10,
    "is_the_person_or_company_responsible_for_the_protection_of_personal_information": "Yes, a different person or company is responsible for it.",
    "what_is_your_dpos_name": "",
    "how_can_users_contact_your_dpo": [],
    "what_is_your_dpos_email_address": "",
    "do_you_have_security_measures_in_place_to_project_personal_information": "Yes, we’ve taken all the necessary measures to keep personal information secure.",
    "what_kind_of_responsive_action_will_you_take_if_you_have_a_data_breach": [
        "Post notifications in the mobile app.",
        "Notify users via email."
    ],
    "how_can_users_contact_you_regarding_this_policy": [
        "Contact form",
        "Email address"

    ],
    "what_is_the_url_of_your_contact_form": "",
    "what_is_your_email_address": "",
    "what_is_your_business_address": "",
    "how_will_you_notify_users_of_the_updates_to_this_policy": [
        "Update the modification date at the bottom of the privacy policy page.",
        "Post notifications in the mobile app."
    ],
    "last_update": "2023-05-02",

    "website_or_app_name": "Dowell GDPR",
    "website_or_app_url": "http://app.com",
    "website_or_app_contact_page_url": "http://app.com/contact",
    "website_or_app_contact_email": "example@app.com"



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
                            "agreement_compliance_type": "software-license-policy",
                            "date_of_execution_of_document": "2025-10-20",
                            "party_1_entity_type": "Individual",
                            "party_1_full_name": "Party 1 Name 1",
                            "party_1_postal_address": "P.O.BOX 45, India",
                            "party_1_jurisdiction_incorporated": "sample law",
                            "party_1_registration_number": "RS5428888",
                            "party_1_registrar_office_address_1": "sample office address",
                            "party_1_registrar_office_address_2": "",
                            "party_1_registrar_office_address_3": "",
                            "party_1_principal_place_of_business": "India",
                            "party_2_entity_type": "Organization",
                            "party_2_full_name": "Party 2 Name",
                            "party_2_postal_address": "P.O.BOX 45, USA",
                            "party_2_jurisdiction_incorporated": "USA",
                            "party_2_registration_number": "RS5428845888",
                            "party_2_registrar_office_address_1": "sample office address",
                            "party_2_registrar_office_address_2": "badu street",
                            "party_2_registrar_office_address_3": "",
                            "party_2_principal_place_of_business": "USA",
                            "charges_payable": 3000.15,
                            "software_document_identification": "software",
                            "contract_effective_date": "2023-02-20",
                            "minimum_terms_apply": 45,
                            "minimum_terms_apply_unit": "Days",
                            "is_software_form_specified": true,
                            "software_form": "software spic",
                            "is_non_material_defects_count_as_software_defects": false,
                            "ways_defect_affect_software": "example",
                            "is_set_of_exclusions_included": false,
                            "exclusions_apply": "",
                            "software_specification": "87 linux",
                            "can_software_specification_be_varied_by_the_parties": true,
                            "terms_of_contract_duration": 50,
                            "terms_of_contract_duration_unit": "Months",
                            "is_inline_copy_right_remove": false,
                            "is_term_of_contract_indefinite": false,
                            "contract_termination_date": "2022-10-20",
                            "events_that_will_cause_contract_to_be_terminated": "Nil",
                            "number_of_license_to_be_deliver": 4,
                            "number_of_license_to_be_deliver_unit": "pcs",
                            "software_delivery_channel": "Email",
                            "within_what_period_must_software_be_delivered": 12,
                            "within_what_period_must_software_be_delivered_unit": "Days",
                            "what_did_licensor_supply_to_the_licensee": "software",
                            "purpose_by_reference_to_which_sub_licensing_is_permitted": "Use For",
                            "when_should_invoice_be_issued": "Nil",
                            "invoicing_date": "2022-10-20",
                            "period_for_payment_of_invoices": 85,
                            "period_for_payment_of_invoices_unit": "Days",
                            "effective_date_for_invoice_payment": "2022-10-20",
                            "invoice_payment_method": "Nil",
                            "interest_rate_apply_to_late_payment": 2450.55,
                            "optional_element": "",
                            "is_warranty_relate_to_a_specific_period": true,
                            "scope_of_warranty": "Nil",
                            "jurisdictional_coverage_of_warranty": "Nil",
                            "period_apply_to_warranty": 3,
                            "period_apply_to_warranty_unit": "Months",
                            "circumstances_in_which_licensor_may_exercise_its_rights": "Nil",
                            "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false,
                            "are_there_limitations_on_right_to_modify": false,
                            "limitations_on_right_to_modify_specification": "Nil",
                            "termination_notice_period_apply": 3,
                            "termination_notice_period_apply_unit": "Months",
                            "is_termination_period_expirable": false,
                            "relevant_termination_period": 0,
                            "relevant_termination_period_unit": "Days",
                            "relevant_termination_period_date": "2022-10-20",
                            "circumstances_in_which_a_party_may_terminate_for_breach": "Nil",
                            "time_frame_for_the_notice_period": 0,
                            "time_frame_for_the_notice_period_unit": "Months",
                            "sent_contractual_notices_to_the_licensor_name": "Nil",
                            "sent_contractual_notices_to_the_licensor_address_1": "Nil",
                            "sent_contractual_notices_to_the_licensor_address_2": "Nil",
                            "sent_contractual_notices_to_the_licensor_address_3": "Nil",
                            "sent_contractual_notices_to_the_licensor_contact_details": "Nil",
                            "sent_contractual_notices_to_the_licensee_name": "Nil",
                            "sent_contractual_notices_to_the_licensee_address_1": "Nil",
                            "sent_contractual_notices_to_the_licensee_address_2": "Nil",
                            "sent_contractual_notices_to_the_licensee_address_3": "Nil",
                            "sent_contractual_notices_to_the_licensee_contact_details": "Nil",
                            "law_governs_document": "Nil",
                            "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "Nil",
                            "which_entity_will_sign_contract_on_behalf_of_party_1": "Contractor",
                            "party_1_signatory_scanned_copy_detail": {
                                "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                                "actual_filename": "AFL.png",
                                "file_extension": "png",
                                "url": "https://100080.pythonanywhere.com/media/img/img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png"
                            },
                            "full_name_of_party_1_signatory": "party 1 name",
                            "party_1_date_of_signing_contract": "2022-11-02",
                            "full_name_of_the_person_sign_on_behalf_of_party_1": "witness 1 name",
                            "date_contract_was_sign_on_behalf_of_party_1": "2022-11-02",
                            "which_entity_will_sign_contract_on_behalf_of_party_2": "Contractor",
                            "party_2_signatory_scanned_copy_detail": {
                                "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                                "actual_filename": "AFL.png",
                                "file_extension": "png",
                                "url": "https://100080.pythonanywhere.com/media/img/img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png"
                            },
                            "full_name_of_party_2_signatory": "party 2 name",
                            "party_2_date_of_signing_contract": "2022-11-05",
                            "full_name_of_the_person_sign_on_behalf_of_party_2": "witness 2 name",
                            "date_contract_was_sign_on_behalf_of_party_2": "2022-11-05"

                        }



        }
    ]
}
```

#### PUT /api/agreements/{event_id}/

- General:
  - Fully update the software agreement of the given ID if it exists. Returns the updated data, success value, to update the frontend.
- `curl http://127.0.0.1:8000/api/agreements/785455899666558884/ -X PUT -H "Content-Type: application/json" -d ' {
    "agreement_compliance_type": "software-license-policy",
                    "date_of_execution_of_document": "2025-10-20",
                    "party_1_entity_type": "Individual",
                    "party_1_full_name": "Party 1 Name 1",
                    "party_1_postal_address": "P.O.BOX 45, India",
                    "party_1_jurisdiction_incorporated": "sample law",
                    "party_1_registration_number": "RS5428888",
                    "party_1_registrar_office_address_1": "sample office address",
                    "party_1_registrar_office_address_2": "",
                    "party_1_registrar_office_address_3": "",
                    "party_1_principal_place_of_business": "India",
                    "party_2_entity_type": "Organization",
                    "party_2_full_name": "Party 2 Name",
                    "party_2_postal_address": "P.O.BOX 45, USA",
                    "party_2_jurisdiction_incorporated": "USA",
                    "party_2_registration_number": "RS5428845888",
                    "party_2_registrar_office_address_1": "sample office address",
                    "party_2_registrar_office_address_2": "badu street",
                    "party_2_registrar_office_address_3": "",
                    "party_2_principal_place_of_business": "USA",
                    "charges_payable": 3000.15,
                    "software_document_identification": "software",
                    "contract_effective_date": "2023-02-20",
                    "minimum_terms_apply": 45,
                    "minimum_terms_apply_unit": "Days",
                    "is_software_form_specified": true,
                    "software_form": "software spic",
                    "is_non_material_defects_count_as_software_defects": false,
                    "ways_defect_affect_software": "example",
                    "is_set_of_exclusions_included": false,
                    "exclusions_apply": "",
                    "software_specification": "87 linux",
                    "can_software_specification_be_varied_by_the_parties": true,
                    "terms_of_contract_duration": 50,
                    "terms_of_contract_duration_unit": "Months",
                    "is_inline_copy_right_remove": false,
                    "is_term_of_contract_indefinite": false,
                    "contract_termination_date": "2022-10-20",
                    "events_that_will_cause_contract_to_be_terminated": "Nil",
                    "number_of_license_to_be_deliver": 4,
                    "number_of_license_to_be_deliver_unit": "pcs",
                    "software_delivery_channel": "Email",
                    "within_what_period_must_software_be_delivered": 12,
                    "within_what_period_must_software_be_delivered_unit": "Days",
                    "what_did_licensor_supply_to_the_licensee": "software",
                    "purpose_by_reference_to_which_sub_licensing_is_permitted": "Use For",
                    "when_should_invoice_be_issued": "Nil",
                    "invoicing_date": "2022-10-20",
                    "period_for_payment_of_invoices": 85,
                    "period_for_payment_of_invoices_unit": "Days",
                    "effective_date_for_invoice_payment": "2022-10-20",
                    "invoice_payment_method": "Nil",
                    "interest_rate_apply_to_late_payment": 2450.55,
                    "optional_element": "",
                    "is_warranty_relate_to_a_specific_period": true,
                    "scope_of_warranty": "Nil",
                    "jurisdictional_coverage_of_warranty": "Nil",
                    "period_apply_to_warranty": 3,
                    "period_apply_to_warranty_unit": "Months",
                    "circumstances_in_which_licensor_may_exercise_its_rights": "Nil",
                    "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false,
                    "are_there_limitations_on_right_to_modify": false,
                    "limitations_on_right_to_modify_specification": "Nil",
                    "termination_notice_period_apply": 3,
                    "termination_notice_period_apply_unit": "Months",
                    "is_termination_period_expirable": false,
                    "relevant_termination_period": 0,
                    "relevant_termination_period_unit": "Days",
                    "relevant_termination_period_date": "2022-10-20",
                    "circumstances_in_which_a_party_may_terminate_for_breach": "Nil",
                    "time_frame_for_the_notice_period": 0,
                    "time_frame_for_the_notice_period_unit": "Months",
                    "sent_contractual_notices_to_the_licensor_name": "Nil",
                    "sent_contractual_notices_to_the_licensor_address_1": "Nil",
                    "sent_contractual_notices_to_the_licensor_address_2": "Nil",
                    "sent_contractual_notices_to_the_licensor_address_3": "Nil",
                    "sent_contractual_notices_to_the_licensor_contact_details": "Nil",
                    "sent_contractual_notices_to_the_licensee_name": "Nil",
                    "sent_contractual_notices_to_the_licensee_address_1": "Nil",
                    "sent_contractual_notices_to_the_licensee_address_2": "Nil",
                    "sent_contractual_notices_to_the_licensee_address_3": "Nil",
                    "sent_contractual_notices_to_the_licensee_contact_details": "Nil",
                    "law_governs_document": "Nil",
                    "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "Nil",
                    "which_entity_will_sign_contract_on_behalf_of_party_1": "Contractor",
                    "party_1_signatory_scanned_copy_detail": {
                        "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                        "actual_filename": "AFL.png",
                        "file_extension": "png",
                        "url": "https://100080.pythonanywhere.com/media/img/img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png"
                    },
                    "full_name_of_party_1_signatory": "party 1 name",
                    "party_1_date_of_signing_contract": "2022-11-02",
                    "full_name_of_the_person_sign_on_behalf_of_party_1": "witness 1 name",
                    "date_contract_was_sign_on_behalf_of_party_1": "2022-11-02",
                    "which_entity_will_sign_contract_on_behalf_of_party_2": "Contractor",
                    "party_2_signatory_scanned_copy_detail": {
                        "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                        "actual_filename": "AFL.png",
                        "file_extension": "png",
                        "url": "https://100080.pythonanywhere.com/media/img/img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png"
                    },
                    "full_name_of_party_2_signatory": "party 2 name",
                    "party_2_date_of_signing_contract": "2022-11-05",
                    "full_name_of_the_person_sign_on_behalf_of_party_2": "witness 2 name",
                    "date_contract_was_sign_on_behalf_of_party_2": "2022-11-05"

                }'`

```
{
    "isSuccess": true,
    "data": [
        {
            "_id": "63076817b171c30837335384",
            "eventId": "785455899666558884",
            "agreement": {
                    "agreement_compliance_type": "software-license-policy",
                    "date_of_execution_of_document": "2025-10-20",
                    "party_1_entity_type": "Individual",
                    "party_1_full_name": "Party 1 Name 1",
                    "party_1_postal_address": "P.O.BOX 45, India",
                    "party_1_jurisdiction_incorporated": "sample law",
                    "party_1_registration_number": "RS5428888",
                    "party_1_registrar_office_address_1": "sample office address",
                    "party_1_registrar_office_address_2": "",
                    "party_1_registrar_office_address_3": "",
                    "party_1_principal_place_of_business": "India",
                    "party_2_entity_type": "Organization",
                    "party_2_full_name": "Party 2 Name",
                    "party_2_postal_address": "P.O.BOX 45, USA",
                    "party_2_jurisdiction_incorporated": "USA",
                    "party_2_registration_number": "RS5428845888",
                    "party_2_registrar_office_address_1": "sample office address",
                    "party_2_registrar_office_address_2": "badu street",
                    "party_2_registrar_office_address_3": "",
                    "party_2_principal_place_of_business": "USA",
                    "charges_payable": 3000.15,
                    "software_document_identification": "software",
                    "contract_effective_date": "2023-02-20",
                    "minimum_terms_apply": 45,
                    "minimum_terms_apply_unit": "Days",
                    "is_software_form_specified": true,
                    "software_form": "software spic",
                    "is_non_material_defects_count_as_software_defects": false,
                    "ways_defect_affect_software": "example",
                    "is_set_of_exclusions_included": false,
                    "exclusions_apply": "",
                    "software_specification": "87 linux",
                    "can_software_specification_be_varied_by_the_parties": true,
                    "terms_of_contract_duration": 50,
                    "terms_of_contract_duration_unit": "Months",
                    "is_inline_copy_right_remove": false,
                    "is_term_of_contract_indefinite": false,
                    "contract_termination_date": "2022-10-20",
                    "events_that_will_cause_contract_to_be_terminated": "Nil",
                    "number_of_license_to_be_deliver": 4,
                    "number_of_license_to_be_deliver_unit": "pcs",
                    "software_delivery_channel": "Email",
                    "within_what_period_must_software_be_delivered": 12,
                    "within_what_period_must_software_be_delivered_unit": "Days",
                    "what_did_licensor_supply_to_the_licensee": "software",
                    "purpose_by_reference_to_which_sub_licensing_is_permitted": "Use For",
                    "when_should_invoice_be_issued": "Nil",
                    "invoicing_date": "2022-10-20",
                    "period_for_payment_of_invoices": 85,
                    "period_for_payment_of_invoices_unit": "Days",
                    "effective_date_for_invoice_payment": "2022-10-20",
                    "invoice_payment_method": "Nil",
                    "interest_rate_apply_to_late_payment": 2450.55,
                    "optional_element": "",
                    "is_warranty_relate_to_a_specific_period": true,
                    "scope_of_warranty": "Nil",
                    "jurisdictional_coverage_of_warranty": "Nil",
                    "period_apply_to_warranty": 3,
                    "period_apply_to_warranty_unit": "Months",
                    "circumstances_in_which_licensor_may_exercise_its_rights": "Nil",
                    "should_there_be_an_express_requirement_for_licensor_to_act_reasonably": false,
                    "are_there_limitations_on_right_to_modify": false,
                    "limitations_on_right_to_modify_specification": "Nil",
                    "termination_notice_period_apply": 3,
                    "termination_notice_period_apply_unit": "Months",
                    "is_termination_period_expirable": false,
                    "relevant_termination_period": 0,
                    "relevant_termination_period_unit": "Days",
                    "relevant_termination_period_date": "2022-10-20",
                    "circumstances_in_which_a_party_may_terminate_for_breach": "Nil",
                    "time_frame_for_the_notice_period": 0,
                    "time_frame_for_the_notice_period_unit": "Months",
                    "sent_contractual_notices_to_the_licensor_name": "Nil",
                    "sent_contractual_notices_to_the_licensor_address_1": "Nil",
                    "sent_contractual_notices_to_the_licensor_address_2": "Nil",
                    "sent_contractual_notices_to_the_licensor_address_3": "Nil",
                    "sent_contractual_notices_to_the_licensor_contact_details": "Nil",
                    "sent_contractual_notices_to_the_licensee_name": "Nil",
                    "sent_contractual_notices_to_the_licensee_address_1": "Nil",
                    "sent_contractual_notices_to_the_licensee_address_2": "Nil",
                    "sent_contractual_notices_to_the_licensee_address_3": "Nil",
                    "sent_contractual_notices_to_the_licensee_contact_details": "Nil",
                    "law_governs_document": "Nil",
                    "court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document": "Nil",
                    "which_entity_will_sign_contract_on_behalf_of_party_1": "Contractor",
                    "party_1_signatory_scanned_copy_detail": {
                        "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                        "actual_filename": "AFL.png",
                        "file_extension": "png",
                        "url": "https://100080.pythonanywhere.com/media/img/img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png"
                    },
                    "full_name_of_party_1_signatory": "party 1 name",
                    "party_1_date_of_signing_contract": "2022-11-02",
                    "full_name_of_the_person_sign_on_behalf_of_party_1": "witness 1 name",
                    "date_contract_was_sign_on_behalf_of_party_1": "2022-11-02",
                    "which_entity_will_sign_contract_on_behalf_of_party_2": "Contractor",
                    "party_2_signatory_scanned_copy_detail": {
                        "filename": "img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png",
                        "actual_filename": "AFL.png",
                        "file_extension": "png",
                        "url": "https://100080.pythonanywhere.com/media/img/img_47dbffd8-50c1-4f5c-af54-819db6d902ab.png"
                    },
                    "full_name_of_party_2_signatory": "party 2 name",
                    "party_2_date_of_signing_contract": "2022-11-05",
                    "full_name_of_the_person_sign_on_behalf_of_party_2": "witness 2 name",
                    "date_contract_was_sign_on_behalf_of_party_2": "2022-11-05"

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


#### DELETE /api/comparisons/{event_id}/

- `curl http://127.0.0.1:8000/api/comparisons/FB1010000000166909595159447637/ -X DELETE -H "Content-Type: application/json`


```
{
    "isSuccess": true,
    "event_id": "FB1010000000166909595159447637"
}
```




### Agreement Compliance Sample

-   https://100080.pythonanywhere.com/media/doc/cookies-policy.pdf
-   https://100080.pythonanywhere.com/media/doc/discliamer-for-app.pdf
-   https://100080.pythonanywhere.com/media/doc/discliamer-for-website.pdf
-   https://100080.pythonanywhere.com/media/doc/employment-contract.pdf
-   https://100080.pythonanywhere.com/media/doc/end-user-licensing-agreement.pdf
-   https://100080.pythonanywhere.com/media/doc/gdpr-privacy-policy.pdf
-   https://100080.pythonanywhere.com/media/doc/memorandum-of-understanding.pdf
-   https://100080.pythonanywhere.com/media/doc/non-compete-agreement.pdf
-   https://100080.pythonanywhere.com/media/doc/non-disclosure-agreement.pdf
-   https://100080.pythonanywhere.com/media/doc/app-privacy-policy.pdf
-   https://100080.pythonanywhere.com/media/doc/website-privacy-policy.pdf
-   https://100080.pythonanywhere.com/media/doc/return-refund-policy.pdf
-   https://100080.pythonanywhere.com/media/doc/software-license-agreement.pdf
-   https://100080.pythonanywhere.com/media/doc/statement-of-work.pdf
-   https://100080.pythonanywhere.com/media/doc/terms-and-conditions.pdf
-   https://100080.pythonanywhere.com/media/doc/terms-of-use-licensing-app.pdf
-   https://100080.pythonanywhere.com/media/doc/website-security-policy.pdf
-   https://100080.pythonanywhere.com/media/doc/website-terms-of-use.pdf


