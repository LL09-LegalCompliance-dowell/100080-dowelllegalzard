from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from licenses.models import (
    SoftwareLicense,
    SoftwareLicenseAgreement
)

class SoftwareLicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoftwareLicense
        fields = (

            "software_name",
            "license_name",
            "version",
            "license_compatible_with",
            "license_not_compatible_with",
            "is_active",
            "disclaimer",
            "definition",
            "grant_of_license",
            "grant_of_patent_license",
            "redistribution",
            "trademarks",
            "license_url",
            "released_date"
            
            )

    def to_representation(self, instance:SoftwareLicense):
        data = super().to_representation(instance)
        data["license_id"] = instance.license_id
        return data

    def create(self, validated_data):
        """
        Create and return new software license.
        """
        SoftwareLicense.objects.create(**validated_data)
        return SoftwareLicense.objects.last()


    def update(self, instance, validated_data):
        """
         Update and return software license.
        """
        instance.software_name = validated_data["software_name"]
        instance.license_name = validated_data["license_name"]
        instance.version = validated_data["version"]
        instance.license_compatible_with = validated_data["license_compatible_with"]
        instance.license_not_compatible_with = validated_data["license_not_compatible_with"]
        instance.is_active = validated_data["is_active"]
        instance.disclaimer = validated_data["disclaimer"]
        instance.grant_of_license = validated_data["grant_of_license"]
        instance.grant_of_patent_license = validated_data["grant_of_patent_license"]
        instance.redistribution = validated_data["redistribution"]
        instance.definition = validated_data["definition"]
        instance.trademarks = validated_data["trademarks"]
        instance.license_url = validated_data["license_url"]
        instance.released_date = validated_data["released_date"]
        instance.save()

        return instance