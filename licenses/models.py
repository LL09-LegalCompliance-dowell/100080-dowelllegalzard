from django.db import models
from DowellLicenseProject import settings
import uuid

class SoftwareLicense(models.Model):
    license_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    software_name = models.CharField(max_length=100)
    license_name = models.CharField(max_length=100)
    version = models.CharField(max_length=15)
    released_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    disclaimer = models.TextField()
    definition = models.TextField()
    grant_of_copy_right_license = models.TextField()
    grant_of_patent_license = models.TextField()
    redistribution = models.TextField()
    trademarks = models.TextField()
    license_url = models.URLField(max_length=255, null=True)
    extra_note = models.TextField(default="")
    image = models.ImageField(upload_to='license/images', null = True)
    submission_of_contributions = models.TextField(default= "")
    limitation_of_liability = models.TextField(default = "")
    accepting_warranty_or_additional_liability = models.TextField(default = "")
    source_code = models.TextField(default = "")
    basic_permission = models.TextField(default = "")
    scope = models.TextField(default = "")


    class Meta:
        db_table = "software_licenses"

    def __str__(self) -> str:
        return f"<License Name: {self.license_name}, Version: {self.version}, Software Name: {self.software_name}>"


    def __repr__(self) -> str:
        return f"""
        SoftwareLicense Object:
        <License Name: {self.license_name}, Version: {self.version}, Software Name: {self.software_name}>
        """


class LicenseCompatibility(models.Model):
    software_license = models.ForeignKey(
        SoftwareLicense,
        related_name="compatibilities",
        on_delete = models.CASCADE
        )
    license_type = models.CharField(max_length=150)
    is_compatible = models.BooleanField(default=False)

    def __repr__(self) -> str:
        return f"<LicenseCompatibility: license type: {self.license_type}, is_compatible: {self.is_compatible}>"

    @staticmethod
    def build_compatible_license_type(software_license:SoftwareLicense,is_compatible:bool,data:str) -> list:
        """Create list of license compatible or non compatible object
         and return result
        """
        # Split non compatible license type
        license_type_list  = data.split(",")
        license_compatibilities = []
        
        # Loop over license type
        # Create license not compatible object
        # And add to not_compatible_list_obj
        for license_type in license_type_list:
            license_compatibilities.append(
                LicenseCompatibility(
                    software_license = software_license,
                    license_type = license_type,
                    is_compatible = is_compatible
                    )
                )
        return license_compatibilities
    
    

class SoftwareLicenseAgreement(models.Model):
    license_agreement_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date_of_execution_of_document = models.DateField()
    party_1_entity_type = models.CharField(max_length= 50)
    party_1_full_name = models.CharField(max_length= 150)
    party_1_postal_address = models.CharField(max_length= 255)
    party_1_jurisdiction_incorporated = models.CharField(max_length= 150)
    party_1_registration_number = models.CharField(max_length= 50)
    party_1_registrar_office_address = models.CharField(max_length=255)
    party_1_principal_place_of_business = models.CharField(max_length=255)
    party_2_entity_type = models.CharField(max_length=50)
    party_2_full_name = models.CharField(max_length=150)
    party_2_postal_address = models.CharField(max_length=255)
    party_2_jurisdiction_incorporated = models.CharField(max_length=150)
    party_2_registration_number = models.CharField(max_length=50)
    party_2_registrar_office_address = models.CharField(max_length=255)
    party_2_principal_place_of_business = models.CharField(max_length=255)
    charges_payable = models.DecimalField(max_digits=18, decimal_places=2, default = 0)
    software_document_identification = models.CharField(max_length=255)
    contract_effective_date = models.DateField()
    minimum_terms_apply = models.CharField(max_length= 50)
    is_software_form_specified = models.BooleanField(default=False)
    software_form = models.CharField(max_length= 100)
    is_non_material_defects_count_as_software_defects = models.BooleanField(default=False)
    ways_defect_affect_software = models.CharField(max_length=255)
    is_set_of_exclusions_included = models.BooleanField(default=False)
    exclusions_apply = models.CharField(max_length=255)
    software_specification = models.CharField(max_length=255)
    can_software_specification_be_varied_by_the_parties = models.BooleanField(default=False)
    terms_of_contract_duration = models.CharField(max_length=50)
    is_inline_copy_right_remove = models.BooleanField(default=False)
    is_term_of_contract_indefinite = models.BooleanField(default=False)
    contract_termination_date = models.DateField(null=True)
    events_that_will_cause_contract_to_be_terminated = models.CharField(max_length=255)
    number_of_license_to_be_deliver  = models.IntegerField(default=1)
    software_delivery_channel = models.CharField(max_length=50)
    software_delivery_period = models.CharField(max_length=50)
    what_did_licensor_supply_to_the_licensee = models.CharField(max_length=150)
    purpose_of_supply = models.CharField(max_length=255)
    when_should_invoice_be_issued  = models.CharField(max_length=255)
    invoicing_date = models.DateField(null=True)
    period_for_payment_of_invoices = models.CharField(max_length=50)
    effective_date_for_invoice_payment = models.DateField(null=True)
    invoice_payment_method  = models.CharField(max_length=100)
    interest_rate_apply_to_late_payment = models.DecimalField(max_digits=18, decimal_places=2, default = 0)
    optional_element_warranty  = models.CharField(max_length=255)
    is_warranty_relate_to_a_specific_period = models.BooleanField(default=False)
    period_apply_to_warranty  = models.CharField(max_length=50)
    scope_of_warranty  = models.CharField(max_length=255)
    jurisdictional_coverage_of_warranty  = models.CharField(max_length=255)
    circumstances_in_which_licensor_may_exercise_its_rights  = models.CharField(max_length=255)
    should_there_be_an_express_requirement_for_licensor_to_act_reasonably = models.BooleanField(default=False)
    are_there_limitations_on_right_to_modify = models.BooleanField(default=False)
    limitations_on_right_to_modify_specification  = models.CharField(max_length=255)
    termination_notice_period_apply = models.BooleanField(default=False)
    is_termination_period_expirable = models.BooleanField(default=False)
    relevant_termination_period  = models.CharField(max_length=50)
    circumstances_in_which_a_party_may_terminate_for_breach  = models.CharField(max_length=255)
    time_frame_for_the_notice_period  = models.CharField(max_length=50)
    contact_details_to_sent_contractual_notices_to_the_licensor  = models.CharField(max_length=255)
    contact_details_to_sent_contractual_notices_to_the_licensee  = models.CharField(max_length=255)
    law_governs_document = models.CharField(max_length=255)
    court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document = models.CharField(max_length=255)
    will_the_contract_signed_by_pary_1_contracting_entity = models.BooleanField(default=False)
    party_1_signatory_scanned_copy_url  = models.CharField(max_length=255)
    full_name_of_party_1_signatory  = models.CharField(max_length=150)
    party_1_date_of_signing_contract = models.DateField(null=True)
    full_name_of_party_1_witness  = models.CharField(max_length=150)
    party_1_witness_date_of_signing_contract = models.DateField(null=True)
    will_the_contract_signed_by_pary_2_contracting_entity = models.BooleanField(default=False)
    party_2_signatory_scanned_copy_url  = models.CharField(max_length=255)
    full_name_of_party_2_signatory  = models.CharField(max_length=150)
    party_2_date_of_signing_contract = models.DateField(null=True)
    full_name_of_party_2_witness  = models.CharField(max_length=150)
    party_2_witness_date_of_signing_contract = models.DateField(null=True)


    class Meta:
        db_table = "software_license_agreements"


    def __str__(self) -> str:
        return f"<Documet: {self.software_document_identification}, First Party: {self.party_1_full_name}, Second Party: {self.party_2_full_name}>"


    def __repr__(self) -> str:
        return f"""
        SoftwareLicense Object:
        <Documet: {self.software_document_identification}, First Party: {self.party_1_full_name}, Second Party: {self.party_2_full_name}>
        """
