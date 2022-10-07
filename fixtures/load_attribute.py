import csv
from dowell import (
    fetch_document,
    save_document,

    COMMON_ATTRIBUTE_COLLECTION,
    ATTRIBUTE_COLLECTION,
    COMMON_ATTRIBUTE_KEY,
    ATTRIBUTE_MAIN_KEY,

    COMMON_ATTRIBUTE_DOCUMENT_NAME,
    ATTRIBUTE_DOCUMENT_NAME,
    RECORD_PER_PAGE
)
from common_attribute import common_attributes


def add_common_attributes():

    print(common_attributes)
    for data in common_attributes:
        save_document(
            collection=COMMON_ATTRIBUTE_COLLECTION,
            document=COMMON_ATTRIBUTE_DOCUMENT_NAME,
            key=COMMON_ATTRIBUTE_KEY,
            value=data
        )


def add_attribute():

    with open("D:\\workhub\\freelancing\\100080-dowelllegalzard\\fixtures\\license-attribution.csv", "r") as file:
        reader = csv.DictReader(file)
        attribute_code = ""
        attributes = ""
        attribute_id = ""

        for data in reader:
            attribute_code = data['Attribute_Code']
            attributes = data['Attributes']
            attribute_id = data['Attribute_ID']

            # Get common attribute
            res_data = fetch_document(
                collection=COMMON_ATTRIBUTE_COLLECTION,
                document=COMMON_ATTRIBUTE_DOCUMENT_NAME,
                fields={"common_attributes.code": attribute_code}
            )

            # Save attribute
            common_attribute = {}
            if res_data['data']:
                common_attribute_obj = res_data['data'][0]
                common_attribute = common_attribute_obj['common_attributes']

            new_attribute = {
                "name": attributes,
                "attribute_id": attribute_id,
                "common_attribute": {
                    "_id": common_attribute_obj['_id'] if common_attribute else "Nil",
                    "eventId": common_attribute_obj['eventId'] if common_attribute else "Nil",
                    "name": common_attribute['name'] if common_attribute else "Nil",
                    "code": common_attribute['code'] if common_attribute else "Nil"
                }
            }
            print(new_attribute)

            save_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                key=ATTRIBUTE_MAIN_KEY,
                value=new_attribute
            )


if __name__ == "__main__":
    # add_common_attributes()
    add_attribute()
