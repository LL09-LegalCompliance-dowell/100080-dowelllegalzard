from rest_framework import serializers
from licenses.models import (
    SoftwareLicense,
    SoftwareLicenseAgreement,
    LicenseCompatibility
)

class SoftwareLicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoftwareLicense
        fields = (
            "software_name",
            "license_name",
            "version",
            "is_active",
            "disclaimer",
            "definition",
            "grant_of_copy_right_license",
            "grant_of_patent_license",
            "redistribution",
            "trademarks",
            "license_url",
            "released_date",
            "extra_note",
            "submission_of_contributions",
            "limitation_of_liability",
            "source_code",
            "basic_permission",
            "scope"
            )

    def to_representation(self, instance:SoftwareLicense):
        data = super().to_representation(instance)
        data['license_id'] = instance.license_id
        return data


    def create(self, validated_data):
        """
        Create and return new software license.
        """
        # Create license
        SoftwareLicense.objects.create(**validated_data)
        # Retrieve license and return license
        software_license = SoftwareLicense.objects.last()
        return software_license

    def update(self, instance, validated_data):
        """
        Update and return software license.
        """

        instance.software_name = validated_data["software_name"]
        instance.license_name = validated_data["license_name"]
        instance.version = validated_data["version"]
        instance.is_active = validated_data["is_active"]
        instance.disclaimer = validated_data["disclaimer"]
        instance.grant_of_copy_right_license = validated_data["grant_of_copy_right_license"]
        instance.grant_of_patent_license = validated_data["grant_of_patent_license"]
        instance.redistribution = validated_data["redistribution"]
        instance.definition = validated_data["definition"]
        instance.trademarks = validated_data["trademarks"]
        instance.license_url = validated_data["license_url"]
        instance.released_date = validated_data["released_date"]
        instance.extra_note = validated_data["extra_note"]
        instance.submission_of_contributions = validated_data["submission_of_contributions"]
        instance.limitation_of_liability = validated_data["limitation_of_liability"]
        instance.source_code = validated_data["source_code"]
        instance.basic_permission = validated_data["basic_permission"]
        instance.scope = validated_data["scope"]
        instance.save()

        return instance

class LicenseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareLicense
        fields = ('image',)

    def update(self, instance, validated_data):
        instance.image = validated_data['image']
        return instance
