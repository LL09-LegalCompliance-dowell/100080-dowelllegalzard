from rest_framework import serializers, status
from utils.dowell import (
    fetch_document,
    save_document,
    update_document,

    COMMON_ATTRIBUTE_COLLECTION,
    ATTRIBUTE_COLLECTION,

    COMMON_ATTRIBUTE_DOCUMENT_NAME,
    ATTRIBUTE_DOCUMENT_NAME,

    COMMON_ATTRIBUTE_KEY,
    ATTRIBUTE_MAIN_KEY,

)


class CommonAttributeSerializer(serializers.Serializer):
    """ common_attribute collection contains
        attributes common to all licenses.
        these attributes are created by the admin or the end user
        with unique code 
        eg.
        [
            {
                _id: 9494955eyfhry,
                "name": "Grant of Copyright License.",
                "code": "G_Copyright"
            },
            {
                _id: 50504955eyfhry,
                "name": "Trademark",
                "code": "Trademark"
            }
        ]
    """
    name = serializers.CharField(max_length=150)
    code = serializers.CharField(max_length=50)

    def create(self, validated_data):
        response_json = {}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        # Create common attribute on remote server
        response_json = save_document(
            collection=COMMON_ATTRIBUTE_COLLECTION,
            document=COMMON_ATTRIBUTE_DOCUMENT_NAME,
            key=COMMON_ATTRIBUTE_KEY,
            value=validated_data
        )

        if response_json["isSuccess"]:
            status_code = 201
            # Retrieve attribute from remote server
            response_json = fetch_document(
                collection=COMMON_ATTRIBUTE_COLLECTION,
                document=COMMON_ATTRIBUTE_DOCUMENT_NAME,
                fields={
                    "eventId": response_json["event_id"]
                }
            )
        return response_json, status_code

    def update(self, event_id, validated_data):

        # # Update attribute on remote server
        response_json = update_document(
            collection=COMMON_ATTRIBUTE_COLLECTION,
            document=COMMON_ATTRIBUTE_DOCUMENT_NAME,
            key=COMMON_ATTRIBUTE_KEY,
            new_value=validated_data,
            event_id=event_id
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve common attribute on remote server
            response_json = fetch_document(
                collection=COMMON_ATTRIBUTE_COLLECTION,
                document=COMMON_ATTRIBUTE_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )

        return response_json, status_code


class AttributeSerializer(serializers.Serializer):
    """ attribute collection contains
        all possible licenses attribute.
        these attributes are created and
        pre-configured by the admin or the end user.

        usage: when creating a license the  user will have the option
        to select and add this attribute to the software license

        eg.
        [
            {
                _id: 949495885,
                "name": "Conveying Modified Source Versions",
                "common_attribute": {

                    _id: 50504955eyfhry,
                    "name": "Grant of Copyright License",
                    "code": "G_Copyright"

                    }
            },
            {
                _id: 949495885,
                "name": "Patents.",
                "common_attribute": {

                    _id: 50504955eyfhry,
                    "name": "Trademark",
                    "code": "Trademark"

                    }
            },
        ]
    """
    name = serializers.CharField(max_length=150)
    common_attribute = serializers.JSONField()

    def create(self, validated_data):
        response_json = {}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        # Create attribute on remote server
        response_json = save_document(
            collection=ATTRIBUTE_COLLECTION,
            document=ATTRIBUTE_DOCUMENT_NAME,
            key=ATTRIBUTE_MAIN_KEY,
            value=validated_data
        )

        if response_json["isSuccess"]:
            status_code = 201
            # Retrieve attribute from remote server
            response_json = fetch_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                fields={
                    "eventId": response_json["event_id"]
                }
            )
        return response_json, status_code

    def update(self, event_id, validated_data):

        # # Update attribute on remote server
        response_json = update_document(
            collection=ATTRIBUTE_COLLECTION,
            document=ATTRIBUTE_DOCUMENT_NAME,
            key=ATTRIBUTE_MAIN_KEY,
            new_value=validated_data,
            event_id=event_id
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve attribute from remote server
            response_json = fetch_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )

        return response_json, status_code
