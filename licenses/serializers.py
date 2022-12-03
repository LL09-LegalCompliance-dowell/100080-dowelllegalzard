from email.policy import default
from importlib.metadata import requires
from urllib import request
from rest_framework import serializers
import json
from licenses.models import (
    SoftwareLicense,
    SoftwareLicenseAgreement,
    CommonAttribute,
    Attribute,
    LicenseAttribute
)
from utils.dowell import (
    fetch_document,
    save_document,
    update_document,

    SOFTWARE_LICENSE_COLLECTION,
    COMMON_ATTRIBUTE_COLLECTION,
    ATTRIBUTE_COLLECTION,

    SOFTWARE_LICENSE_DOCUMENT_NAME,
    COMMON_ATTRIBUTE_DOCUMENT_NAME,
    ATTRIBUTE_DOCUMENT_NAME,

    SOFTWARE_LICENSE_KEY,
    COMMON_ATTRIBUTE_KEY,
    ATTRIBUTE_MAIN_KEY,

)


class LicenseTypeSerializer(serializers.Serializer):
    """ LicenseType collection contains
        All the types of license
        and their category = name
        eg.
        [
            {
                "name": "WEAKLY COPYLEFT",
                "licenses": [ "LGPLv2.1", "LGPL2.1+"]
            },
            {
                "name": "STRONGLY COPYLEFT",
                "licenses": [ "GPLv2", "GPL2+"]
            }
        ]
    """
    name = serializers.CharField(max_length=150)
    licenses = serializers.ListField()


class SoftwareLicenseSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        software license document
    """
    license_name = serializers.CharField(max_length=100)
    features = serializers.ListField(default=[])
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
    other_links = serializers.ListField(default=[])
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


class LicenseAttributeHelperSerializer(serializers.Serializer):
    """ LicenseAttributeHelper is a helper
        class used to validate and build the dict/JSON object
        for license_attributes property in 
        software_licenses document.

        eg.
        {
           "description": "The 2.0 version of the Apache License, approved by the ASF in 2004.",
           "attribute": {
                        _id: 949495885,
                        "name": "Conveying Modified Source Versions",
                        }   
         }

    """
    description = serializers.CharField(max_length=2000, default="")
    # Mapping LicenseAttribute to
    # constant / common attribute define
    attribute = serializers.JSONField()


class LicenseCompatibilityHelperSerializer(serializers.Serializer):
    """ LicenseCompatibilityHelper is a helper
        class used to validate and build the dict/JSON object
        for license_compatibility property in 
        software_licenses document.

        eg.
        {
           "license": "APACHE 2.0",
           "percentage_of_comaptibility": "80",
           "is_compatible": False,   
         }

    """
    license = serializers.CharField(max_length=150)
    percentage_of_comaptibility = serializers.IntegerField(default=0)
    is_compatible = serializers.BooleanField(default=False)
