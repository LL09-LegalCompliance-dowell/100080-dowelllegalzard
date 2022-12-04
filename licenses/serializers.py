from rest_framework import serializers

from utils.dowell import (
    fetch_document,
    save_document,
    update_document,

    SOFTWARE_LICENSE_COLLECTION,
    SOFTWARE_LICENSE_DOCUMENT_NAME,
    SOFTWARE_LICENSE_KEY,

)


class SoftwareLicenseSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        software license document
    """
    license_name = serializers.CharField(max_length=100)
    license_tags = serializers.ListField(default=[])
    version = serializers.CharField(max_length=15)
    type_of_license = serializers.CharField(max_length=150)
    short_description = serializers.CharField(
        max_length=500, default="", allow_blank=True, required=False)
    description = serializers.CharField(
        max_length=10000, default="", allow_blank=True, required=False)
    disclaimer = serializers.CharField(max_length=10000, default="", allow_blank=True, required=False)
    risk_for_choosing_license = serializers.CharField(max_length=2000, allow_blank=True, required=False)
    limitation_of_liability = serializers.CharField(max_length=2000, allow_blank=True, required=False)
    license_url = serializers.URLField(max_length=255)
    logo_detail = serializers.DictField()
    recommendation = serializers.CharField(max_length=2000, default="", allow_blank=True, required=False)
    is_active = serializers.BooleanField(default=True)
    license_attributes = serializers.DictField()
    license_compatible_with_lookup = serializers.ListField(default=[])
    license_not_compatible_with_lookup = serializers.ListField(default=[])


    def to_representation(self, document: dict, id):

        if "_id" not in document:
            document['_id'] = id
        return document

    def create(self, validated_data):
        """
        Create and return new software license.
        """
        status_code = 500
        response_json = {}


        # Create license on remote server
        response_json = save_document(
            collection=SOFTWARE_LICENSE_COLLECTION,
            document=SOFTWARE_LICENSE_DOCUMENT_NAME,
            key=SOFTWARE_LICENSE_KEY,
            value=validated_data
        )

        if response_json["isSuccess"]:
            status_code = 201
            # Retrieve license on remote server
            response_json = fetch_document(
                collection=SOFTWARE_LICENSE_COLLECTION,
                document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields={
                    "eventId": response_json["event_id"]
                }
            )

        return response_json, status_code

    def update(self, event_id, validated_data):
        """
        Update and return software license.
        """
        status_code = 500
        response_json = {}


        # # Update license on remote server
        response_json = update_document(
            collection=SOFTWARE_LICENSE_COLLECTION,
            document=SOFTWARE_LICENSE_DOCUMENT_NAME,
            key=SOFTWARE_LICENSE_KEY,
            new_value=validated_data,
            event_id=event_id
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve license on remote server
            response_json = fetch_document(
                collection=SOFTWARE_LICENSE_COLLECTION,
                document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )

        return response_json, status_code