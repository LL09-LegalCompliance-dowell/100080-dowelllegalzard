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
    LICENSE_TYPE_COLLECTION,

    SOFTWARE_LICENSE_DOCUMENT_NAME,
    COMMON_ATTRIBUTE_DOCUMENT_NAME,
    ATTRIBUTE_DOCUMENT_NAME,
    LICENSE_TYPE_DOCUMENT_NAME,

    SOFTWARE_LICENSE_KEY,
    COMMON_ATTRIBUTE_KEY,
    ATTRIBUTE_MAIN_KEY,
    LICENSE_MAIN_KEY

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
    code = serializers.CharField(max_length=150)


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


class SoftwareLicenseSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        software license document
    """
    software_name = serializers.CharField(max_length=100)
    license_name = serializers.CharField(max_length=100)
    version = serializers.CharField(max_length=15)
    type_of_license = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=2000, default="")
    disclaimer = serializers.CharField(max_length=2000, default="")
    risk_for_choosing_license = serializers.CharField(max_length=2000)
    limitation_of_liability = serializers.CharField(max_length=2000)
    license_url = serializers.URLField(max_length=255)
    image_url = serializers.URLField(max_length=255)
    recommendation = serializers.CharField(max_length=2000, default="")
    released_date = serializers.DateField()
    is_active = serializers.BooleanField(default=True)
    license_attributes = serializers.ListField(default=[])
    license_compatibility = serializers.ListField(default=[])
    license_compatible_with_lookup = serializers.ListField(default=[])
    license_not_compatible_with_lookup = serializers.ListField(default=[])

    # LICENSE COMPATIBILITY DOCUMENT
    # license_compatibility =[
    #     {
    #      "license": "APACHE 2.0",
    #      "percentage_of_comaptibility": "80",
    #      "is_compatible": False,
    #     },
    #     {
    #      "license": "GPLv2",
    #      "percentage_of_comaptibility": "80",
    #      "is_compatible": True,
    #     }
    # ]

    # license_compatible_with_lookup = ["GPLv2", "LGPLv2.1"]
    # or
    # license_not_compatible_with_lookup = ["GPLv2", "GPL2+"]

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

        # format date back to iso format
        validated_data['released_date'] = validated_data['released_date'].isoformat()

        # # Create license on localhost
        # SoftwareLicense.objects.create(document = validated_data)
        # # Retrieve license and return license
        # license = SoftwareLicense.objects.last()
        # if license:
        #     status_code = 201
        #     response_json = self.to_representation(license.document, license.license_id)

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
                fields={"_id": response_json["inserted_id"]}
            )

        return response_json, status_code

    def update(self, license_name, validated_data):
        """
        Update and return software license.
        """
        status_code = 500
        response_json = {}

        # format date back to iso format
        validated_data['released_date'] = validated_data['released_date'].isoformat()

        # Update localhost
        # Retrieve license
        # license = SoftwareLicense.objects.get(license_id = license_id)
        # license.document = validated_data
        # license.save()
        # response_json = self.to_representation(license.document, license.id)

        # # Update license on remote server
        response_json = update_document(
            collection=SOFTWARE_LICENSE_COLLECTION,
            document=SOFTWARE_LICENSE_DOCUMENT_NAME,
            key=SOFTWARE_LICENSE_KEY,
            new_value=validated_data,
            license_name=license_name
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve license on remote server
            response_json = fetch_document(
                collection=SOFTWARE_LICENSE_COLLECTION,
                document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields={"softwarelicense.license_name": license_name}
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
