from dowell import (
    fetch_document,
    save_document,

    COMMON_ATTRIBUTE_COLLECTION,
    ATTRIBUTE_COLLECTION,
    COMMON_ATTRIBUTE_KEY,

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


if __name__ == "__main__":
    add_common_attributes()
