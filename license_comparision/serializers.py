from datetime import datetime
from rest_framework import serializers
import json
from utils.dowell import (
    fetch_document,
    save_document,
    update_document,

    ATTRIBUTE_COLLECTION,
    ATTRIBUTE_DOCUMENT_NAME,
    ATTRIBUTE_MAIN_KEY

)

class ComparisionSerializer(serializers.Serializer):
    """ Retrieve, and  create and update
        license comparision
    """

    attribute_type = serializers.CharField(max_length=200)
    indentifier = serializers.CharField(max_length=1000)
    license_1_event_id = serializers.CharField(max_length=255)
    license_2_event_id = serializers.CharField(max_length=255)
    license_1_logo_url = serializers.URLField()
    license_2_logo_url = serializers.URLField()
    license_1_name = serializers.CharField(max_length=150)
    license_2_name = serializers.CharField(max_length=150)
    license_1_version = serializers.CharField(max_length=50)
    license_2_version = serializers.CharField(max_length=50)
    comparisions = serializers.ListField()


    def create(self, validated_data):
        """
        Create and return comparision.
        """


        # Create comparision
        response_json = save_document(
            collection=ATTRIBUTE_COLLECTION,
            document=ATTRIBUTE_DOCUMENT_NAME,
            key=ATTRIBUTE_MAIN_KEY,
            value=validated_data
        )

        if response_json["isSuccess"]:
            status_code = 201
            # Retrieve comparision
            response_json = fetch_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                fields={"eventId": response_json["event_id"]}
            )



        return response_json, status_code

    def update(self, event_id, validated_data):
        """
        Update and return comparision.
        """
        status_code = 500
        response_json = {}



        # Update comparision
        response_json = update_document(
            collection=ATTRIBUTE_COLLECTION,
            document=ATTRIBUTE_DOCUMENT_NAME,
            key=ATTRIBUTE_MAIN_KEY,
            new_value=validated_data,
            event_id=event_id
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve comparision
            response_json = fetch_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )



        return response_json, status_code

