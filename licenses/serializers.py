from dataclasses import field
from email.policy import default
from rest_framework import serializers
from licenses.models import (
    SoftwareLicense,
    SoftwareLicenseAgreement,
    CommonAttribute,
    Attribute,
    LicenseAttribute
)
from utils.dowell import (
    save_document,
    SOFTWARE_AGREEMENT_COLLECTION,
    SOFTWARE_LICENSE_COLLECTION,
    COMMON_ATTRIBUTE_COLLECTION,
    ATTRIBUTE_COLLECTION,
    LICENSE_ATTRIBUTE_COLLECTION,
    LICENSE_OF_TYPES_COLLECTION,
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
    name = serializers.CharField(max_length=150, null=False)
    licenses = serializers.ListField()


class CommonAttributeSerializer(serializers.Serializer):
    """ CommonAttribute collection contains
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
    name = serializers.CharField(max_length=150, null=False)
    code = serializers.CharField(max_length=150, null=False)



class AttributeSerializer(serializers.Serializer):
    """ Attribute collection contains
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
    name = serializers.CharField(max_length=150, null=False)
    common_attribute = serializers.JSONField()


class SoftwareLicenseSerializer(serializers.Serializer):
    """ Validate attribute, create and update document
    """
    software_name = serializers.CharField(max_length=100)
    license_name = serializers.CharField(max_length=100)
    version = serializers.CharField(max_length=15)
    type_of_license = serializers.CharField(max_length=150, default="")
    description = serializers.CharField(max_length=2000)
    disclaimer = serializers.CharField(max_length=2000)
    risk_for_choosing_license = serializers.CharField(max_length=2000, defualt= "")
    limitation_of_liability = serializers.CharField(max_length=2000, defualt= "")
    license_url = serializers.URLField(max_length=255, null=True)
    image_url = serializers.URLField(max_length=255, null=True)
    recommendation = serializers.CharField(max_length=2000, defualt= "")
    released_date = serializers.DateField(null=True)
    is_active = serializers.BooleanField(default=True)
    license_attributes = serializers.ListField(default = [])
    license_compatibility = serializers.ListField(default = [])
    license_compatible_with_lookup = serializers.ListField(default = [])
    license_not_compatible_with_lookup = serializers.ListField(default = [])


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


    def create(self, validated_data):
        """
        Create and return new software license.
        """
        # Create license on localhost
        SoftwareLicense.objects.create(document = validated_data)
        # Retrieve license and return license
        software_license = SoftwareLicense.objects.last()

        # Create license on remote server
        save_document()


        return software_license


    def update(self, instance, validated_data):
        """
        Update and return software license.
        """

        instance.document = validated_data
        instance.save()
        return instance




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
    description = serializers.CharField(max_length=2000)
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