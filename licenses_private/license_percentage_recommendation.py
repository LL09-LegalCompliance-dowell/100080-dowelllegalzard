PERCENTAGE_FACTOR = {
    "permission": 10,
    "condition": 50,
    "limitation": 20,
    "must include": 10,
    "law": 5,
    "source": 5
}



def calculate_percentage_recommendation(license_1:dict, license_2:dict) -> int:
    """ Calculate percentage recommended between 
        two licenses and return the result 
    """

    permission_percentage = 0
    condition_percentage = 0
    limitation_percentage = 0
    law_percentage = 0
    source_percentage = 0
    must_include_percentage = 0

    if "permissions" in license_1 and "permissions" in license_2:
        permission_percentage = calculate_percentage(license_1['permissions'], license_2['permissions'], "permission")
    if "conditions" in license_1 and "conditions" in license_2:
        condition_percentage = calculate_percentage(license_1['conditions'], license_2['conditions'], "condition")
    if "limitations" in license_1 and "limitations" in license_2:
        limitation_percentage = calculate_percentage(license_1['limitations'], license_2['limitations'], "limitation")

    if "laws" in license_1 and "laws" in license_2:
        # Get factor
        factor = PERCENTAGE_FACTOR["law"]
        if license_1['laws'].lower() == license_2['laws'].lower():
            # if all value are fixed
            law_percentage = factor
        elif license_1['laws'].lower() != license_2['laws'].lower():
            # if one of the value is fixed
            law_percentage = (float(factor) / float(2))

    if "sources" in license_1 and "sources" in license_2:
        source_percentage = calculate_percentage(license_1['sources'], license_2['sources'], "source")
    if "must_includes" in license_1 and "must_includes" in license_2:
        must_include_percentage = calculate_percentage(license_1['must_includes'], license_2['must_includes'], "must include")



    print({
        "permission_percentage": permission_percentage,
        "condition_percentage": condition_percentage,
        "must_include_percentage": must_include_percentage,
        "limitation_percentage": limitation_percentage,
        "law_percentage": law_percentage,
        "source_percentage": source_percentage,
    })


    return int(sum(
        [
        permission_percentage,
        condition_percentage,
        must_include_percentage,
        limitation_percentage,
        law_percentage,
        source_percentage]))


def calculate_percentage(data_1, data_2, type_of_data):
    result = 0

    # Get factor
    factor = PERCENTAGE_FACTOR[type_of_data]

    # format data 
    data_1_formated, data_1_length = format_data(data_1)
    data_2_formated, data_2_length = format_data(data_2)
    

    # Get longest items
    longest_data = data_1_length if data_1_length > data_2_length else data_2_length
    if longest_data:

        # Get score
        score = float(factor) / float(longest_data)


        if data_1_length > data_2_length:
            for key, value in data_1_formated.items():
                # check if item exist
                if key in data_2_formated:
                    # check if value is equal
                    if value['status'] == data_2_formated[key]['status']:
                        # if all value are true or false
                        result += score

                    elif value['status'] != data_2_formated[key]['status']:
                        # if one of the value is true
                        result += (float(score) / float(2))

                
                    result = decrease_result_if_has_condition(
                        result, value['has_other_condition'], data_2_formated[key]['has_other_condition'])

        else:
            for key, value in data_2_formated.items():
                # check if item exist
                if key in data_1_formated:
                    # check if value is equal
                    if value['status'] == data_1_formated[key]['status']:
                        # if all value are true or false
                        result += score
                    elif value['status'] != data_1_formated[key]['status']:
                        # if one of the value is true
                        result += (float(score) / float(2))

                    result = decrease_result_if_has_condition(
                        result, value['has_other_condition'], data_1_formated[key]['has_other_condition'])
                    
    else:
        result += factor


    return result

def decrease_result_if_has_condition(result, has_other_condition_1, has_other_condition_2):

    if has_other_condition_1 and has_other_condition_2:
        result -= 2
    elif has_other_condition_1 or has_other_condition_2:
        result -= 1

    return result


def format_data(data_list)-> dict:
    """ Convert data from list to dict
    and return result
    """
    # 
    formated_data = {}

    for data in data_list:
        if isinstance(data, dict):
            formated_data[data["action"]] = {
                "status": True if data["permission"].lower() == "yes" else False,
                "has_other_condition": data["has_other_condition"] if "has_other_condition" in data else False
            }

        elif isinstance(data, str):
            formated_data[data.lower()] = {"status": True, "has_other_condition": False}

    return formated_data, len(formated_data.keys())






if __name__ == "__main__":

    # TEST
    # Permission Percentage
    permission_1 = [
        
        {"action": "Patent Use", "permission": "Yes", "has_other_condition": True},
        {"action": "Patent Grant", "permission": "Yes"},
        {"action": "trademark Grant", "permission": "Yes"}
    ]
    permission_2 = [
        {"action": "Patent Use", "permission": "Yes", "has_other_condition": True},
        {"action": "Patent Grant", "permission": "No"},
        {"action": "trademark Grant", "permission": "No"}
    ]

    print("permission %: ", calculate_percentage(permission_1, permission_2, "permission"))

    # Condition Percentage
    condition_1 = [
        {"action": "Disclose Source", "permission": "Yes", "has_other_condition": True},
        {"action": "Network Use is for Distribution", "permission": "No"},
        {"action": "Release Under Same License", "permission": "No"},
        {"action": "State changes", "permission": "Yes"},
        {"action": "License and Copyright Notice", "permission": "No"}
    ]
    condition_2 = [
        {"action": "Disclose Source", "permission": "Yes"},
        {"action": "Network Use is for Distribution", "permission": "No"},
        {"action": "Release Under Same License", "permission": "Yes"},
        {"action": "State changes", "permission": "Yes"},
        {"action": "License and Copyright Notice", "permission": "No"}
    ]

    print("condition %: ", calculate_percentage(condition_1, condition_2, "condition"))

    # Limitation Percentage
    limitation_1 = [
        {"action": "liability", "permission": "Yes"},
        {"action": "warranty", "permission": "Yes"},
        {"action": "Trademark use", "permission": "Yes"}
    ]
    limitation_2 = [
        {"action": "liability", "permission": "No"},
        {"action": "warranty", "permission": "Yes"},
        {"action": "Trademark use", "permission": "Yes"}
    ]

    print("limitation %: ", calculate_percentage(limitation_1, limitation_2, "limitation"))

    # Limitation Percentage
    must_include_1 = [
        "License",
        "Copyright notice"
    ]
    must_include_2 = [
        "License",
        "Copyright notice"
    ]


    # Overall percentage calculation
    license_1 = {
        "permissions": permission_1,
        "conditions": condition_1,
        "limitations": limitation_1,
        "must_includes": must_include_1,
        "laws": "Fixed"
    }

    license_2 = {
        "permissions": permission_2,
        "conditions": condition_2,
        "limitations": limitation_2,
        "must_includes": must_include_2,
        "laws": "Fixed"
    }

    print("Recommendation Percentage: ", calculate_percentage_recommendation(license_1, license_2))



