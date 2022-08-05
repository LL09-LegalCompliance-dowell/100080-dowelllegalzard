from dataclasses import field
from rest_framework import serializers
from licenses.models import (
    SoftwareLicense,
    SoftwareLicenseAgreement,
    LicenseCompatibility,
    CommonAttribute,
    Attribute,
    LicenseAttribute
)

# Software license serializer

class CommonAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonAttribute
        fields = (
            "name",
            "code",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = instance.id
        return data


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = (
            "name",
            "common_attribute",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = instance.id
        return data


class LicenseAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseAttribute
        fields = (
            "description",
            "software_license",
            "attribute",
        )


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = instance.id
        return data

    def update(self, instance, validated_data):
        instance.description = validated_data["description"]
        instance.attribute = validated_data["attribute"]
        return instance


class SoftwareLicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoftwareLicense
        fields = (
            "software_name",
            "license_name",
            "version",
            "type_of_license",
            "description",
            "disclaimer",
            "risk_for_choosing_license",
            "limitation_of_liability",
            "license_url",
            "recommendation",
            "released_date",
            "is_active",
            )

    def to_representation(self, instance:SoftwareLicense):
        data = super().to_representation(instance)

        data['license_id'] = instance.license_id
        data['image_url'] = instance.image.url if instance.image else ""
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
        instance.type_of_license = validated_data["type_of_license"]
        instance.description = validated_data["description"]
        instance.disclaimer = validated_data["disclaimer"]
        instance.risk_for_choosing_license = validated_data["risk_for_choosing_license"]
        instance.limitation_of_liability = validated_data["limitation_of_liability"]
        instance.license_url = validated_data["license_url"]
        instance.recommendation = validated_data["recommendation"]
        instance.released_date = validated_data["released_date"]
        instance.is_active = validated_data["is_active"]
        instance.save()

        return instance


class LicenseCompatibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseCompatibility
        fields = (
            "license_type",
            "percentage_of_comaptibility",
            "is_compatible",
            "software_license"
        )

    
    def update(self, instance, validated_data):
        instance.license_type = validated_data["license_type"]
        instance.percentage_of_comaptibility = validated_data["percentage_of_comaptibility"]
        instance.is_compatible = validated_data["is_compatible"]
        instance.save()
        return instance


class LicenseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareLicense
        fields = ('image',)

    def update(self, instance, validated_data):
        instance.image = validated_data['image']
        instance.save()
        return instance
