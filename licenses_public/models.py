from unicodedata import category
from django.db import models
from DowellLicenseProject import settings
import uuid

# Preset common attributes
class CommonAttribute(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    document = models.JSONField()


    class Meta:
        db_table = "common_attributes_public"

    def __str__(self) -> str:
        return f"<name({self.document['name']}), code({self.document['code']})>"

    def __repr__(self) -> str:
        return f"<CommonAttribute: name({self.document['name']}), code({self.document['code']})>"


class Attribute(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    document = models.JSONField()

    class Meta:
        db_table = "attributes_public"

    def __str__(self) -> str:
        return f"<name({self.document['name']})>"

    def __repr__(self) -> str:
        return f"<Attribute: name({self.document['name']})>"


class LicenseType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    document = models.JSONField()
    

    class Meta:
        db_table = "license_types_public"

    def __str__(self) -> str:
        return f"<name({self.document['name']}), licenses({self.document['licenses']})>"

    def __repr__(self) -> str:
        return f"<LicenseType: name({self.document['name']}), licenses({self.document['licenses']})>"


class SoftwareLicense(models.Model):
    license_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    document = models.JSONField()

    class Meta:
        db_table = "software_licenses_public"

    def __str__(self) -> str:
        return f"<license_name({self.document['license_name']}), version({self.document['version']}), software_name({self.document['software_name']})>"

    def __repr__(self) -> str:
        return f"<SoftwareLicense: license_name({self.document['license_name']}), version({self.document['version']}), software_name({self.document['software_name']})>"


class LicenseAttribute(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    document = models.JSONField()

    class Meta:
        db_table = "license_attributes_public"


class SoftwareLicenseAgreement(models.Model):
    license_agreement_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    document = models.JSONField()

    class Meta:
        db_table = "software_license_agreements_public"


    def __str__(self) -> str:
        return f"<Document: {self.software_document_identification}, First Party: {self.party_1_full_name}, Second Party: {self.party_2_full_name}>"


    def __repr__(self) -> str:
        return f"""
        SoftwareLicense Object:
        <Documet: {self.software_document_identification}, First Party: {self.party_1_full_name}, Second Party: {self.party_2_full_name}>
        """
