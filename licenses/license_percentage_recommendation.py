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


    permission_percentage = calculate_percentage(license_1['permissions'], license_2['permissions'], "permission")
    condition_percentage = calculate_percentage(license_1['conditions'], license_2['conditions'], "condition")
    limitation_percentage = calculate_percentage(license_1['limitations'], license_2['limitations'], "limitation")
    # law_percentage = calculate_percentage(license_1['laws'], license_2['laws'], "law")
    # source_percentage = calculate_percentage(license_1['sources'], license_2['sources'], "source")
    # must_include_percentage = calculate_percentage(license_1['must_includes'], license_2['must_includes'], "must include")


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


    data_1_length = len(data_1)
    data_2_length = len(data_2)

    # format data 
    data_1_formated = format_data(data_1)
    data_2_formated = format_data(data_2)
    

    # Get longest items
    longest_data = data_1_length if data_1_length > data_2_length else data_2_length

    # Get score
    score = float(factor) / float(longest_data)


    if data_1_length > data_2_length:
        for key, value in data_1_formated.items():
            # check if item exist
            if key in data_2_formated:
                # check if value is equal
                if value == data_2_formated[key]:
                    result += score
                else:
                    result += (float(score) / float(2))
            
    
    else:
        for key, value in data_2_formated.items():
            # check if item exist
            if key in data_1_formated:
                # check if value is equal
                if value == data_1_formated[key]:
                    result += score
                else:
                    result += (float(score) / float(2))


    return result


def format_data(data_list)-> dict:
    """ Convert data from list to dict
    and return result
    """
    formated_data = {}

    for data in data_list:
        if isinstance(data, dict):

            key:str = list(data.keys())[0]
            formated_data[key.lower()] = data[key]

        elif isinstance(data, str):
            formated_data[data.lower()] = True

    return formated_data






if __name__ == "__main__":

    # TEST
    # Permission Percentage
    permission_1 = [
        
        {"Patent Use": True},
        {"Patent Grant": True},
        {"trademark Grant": True}
    ]
    permission_2 = [
        {"Patent Use": True},
        {"Patent Grant": False},
        {"trademark Grant": False}
    ]

    print("permission %: ", calculate_percentage(permission_1, permission_2, "permission"))

    # Condition Percentage
    condition_1 = [
        {"Disclose Source": True},
        {"Network Use is for Distribution": True},
        {"Release Under Same License": True},
        {"State changes": True},
        {"License and Copyright Notice": True}
    ]
    condition_2 = [
        {"Disclose Source": True},
        {"Network Use is for Distribution": False},
        {"Release Under Same License": True},
        {"State changes": True},
        {"License and Copyright Notice": True}
    ]

    print("condition %: ", calculate_percentage(condition_1, condition_2, "condition"))

    # Limitation Percentage
    limitation_1 = [
        "No liability",
        "No warranty",
        "No Trademark use"
    ]
    limitation_2 = [
        "No liability",
        "No warranty",
        "No Trademark use"
    ]

    print("limitation %: ", calculate_percentage(limitation_1, limitation_2, "limitation"))


    # Overall percentage calculation
    license_1 = {
        "permissions": permission_1,
        "conditions": condition_1,
        "limitations": limitation_1
    }

    license_2 = {
        "permissions": permission_2,
        "conditions": condition_2,
        "limitations": limitation_2
    }

    print("Recommendation Percentage: ", calculate_percentage_recommendation(license_1, license_2))



