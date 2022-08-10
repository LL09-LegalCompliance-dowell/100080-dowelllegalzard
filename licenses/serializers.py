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
    name = serializers.CharField(max_length=150)
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
    name = serializers.CharField(max_length=150)
    code = serializers.CharField(max_length=150)


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
        response_ = SoftwareLicense.objects.last()


        # # Create license on remote server
        # response_ = save_document(
        #     collection= SOFTWARE_LICENSE_COLLECTION,
        #     document_name= "software_licence",
        #     document_data= validated_data
        # )

        return response_


    def update(self, instance, validated_data):
        """
        Update and return software license.
        """

        # Update localhost 
        instance.document = validated_data
        instance.save()
        response_ = instance

        # # Update license on remote server
        # response_ = save_document(
        #     collection= SOFTWARE_LICENSE_COLLECTION,
        #     document_name= "software_licence",
        #     document_data= validated_data,
        #     is_update= True
        # )

        return response_


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
    description = serializers.CharField(max_length=2000, default = "")
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



class SoftwareLicenseAgreementSerializer(serializers.Serializer):
    """ Validate attribute, create and update software
        license agreement document
    """
    date_of_execution_of_document = serializers.DateField()
    party_1_entity_type = serializers.CharField(max_length= 50)
    party_1_full_name = serializers.CharField(max_length= 150)
    party_1_postal_address = serializers.CharField(max_length= 255)
    party_1_jurisdiction_incorporated = serializers.CharField(max_length= 150)
    party_1_registration_number = serializers.CharField(max_length= 50)
    party_1_registrar_office_address = serializers.CharField(max_length=255)
    party_1_principal_place_of_business = serializers.CharField(max_length=255)
    party_2_entity_type = serializers.CharField(max_length=50)
    party_2_full_name = serializers.CharField(max_length=150)
    party_2_postal_address = serializers.CharField(max_length=255)
    party_2_jurisdiction_incorporated = serializers.CharField(max_length=150)
    party_2_registration_number = serializers.CharField(max_length=50)
    party_2_registrar_office_address = serializers.CharField(max_length=255)
    party_2_principal_place_of_business = serializers.CharField(max_length=255)
    charges_payable = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    software_document_identification = serializers.CharField(max_length=255)
    contract_effective_date = serializers.DateField()
    minimum_terms_apply = serializers.CharField(max_length= 50)
    is_software_form_specified = serializers.BooleanField(default=False)
    software_form = serializers.CharField(max_length= 100)
    is_non_material_defects_count_as_software_defects = serializers.BooleanField(default=False)
    ways_defect_affect_software = serializers.CharField(max_length=255)
    is_set_of_exclusions_included = serializers.BooleanField(default=False)
    exclusions_apply = serializers.CharField(max_length=255)
    software_specification = serializers.CharField(max_length=255)
    can_software_specification_be_varied_by_the_parties = serializers.BooleanField(default=False)
    terms_of_contract_duration = serializers.CharField(max_length=50)
    is_inline_copy_right_remove = serializers.BooleanField(default=False)
    is_term_of_contract_indefinite = serializers.BooleanField(default=False)
    contract_termination_date = serializers.DateField()
    events_that_will_cause_contract_to_be_terminated = serializers.CharField(max_length=255)
    number_of_license_to_be_deliver  = serializers.IntegerField(default=1)
    software_delivery_channel = serializers.CharField(max_length=50)
    software_delivery_period = serializers.CharField(max_length=50)
    what_did_licensor_supply_to_the_licensee = serializers.CharField(max_length=150)
    purpose_of_supply = serializers.CharField(max_length=255)
    when_should_invoice_be_issued  = serializers.CharField(max_length=255)
    invoicing_date = serializers.DateField()
    period_for_payment_of_invoices = serializers.CharField(max_length=50)
    effective_date_for_invoice_payment = serializers.DateField()
    invoice_payment_method  = serializers.CharField(max_length=100)
    interest_rate_apply_to_late_payment = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    optional_element_warranty  = serializers.CharField(max_length=255)
    is_warranty_relate_to_a_specific_period = serializers.BooleanField(default=False)
    period_apply_to_warranty  = serializers.CharField(max_length=50)
    scope_of_warranty  = serializers.CharField(max_length=255)
    jurisdictional_coverage_of_warranty  = serializers.CharField(max_length=255)
    circumstances_in_which_licensor_may_exercise_its_rights  = serializers.CharField(max_length=255)
    should_there_be_an_express_requirement_for_licensor_to_act_reasonably = serializers.BooleanField(default=False)
    are_there_limitations_on_right_to_modify = serializers.BooleanField(default=False)
    limitations_on_right_to_modify_specification  = serializers.CharField(max_length=255)
    termination_notice_period_apply = serializers.BooleanField(default=False)
    is_termination_period_expirable = serializers.BooleanField(default=False)
    relevant_termination_period  = serializers.CharField(max_length=50)
    circumstances_in_which_a_party_may_terminate_for_breach  = serializers.CharField(max_length=255)
    time_frame_for_the_notice_period  = serializers.CharField(max_length=50)
    contact_details_to_sent_contractual_notices_to_the_licensor  = serializers.CharField(max_length=255)
    contact_details_to_sent_contractual_notices_to_the_licensee  = serializers.CharField(max_length=255)
    law_governs_document = serializers.CharField(max_length=255)
    court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document = serializers.CharField(max_length=255)
    will_the_contract_signed_by_pary_1_contracting_entity = serializers.BooleanField(default=False)
    party_1_signatory_scanned_copy_url  = serializers.CharField(max_length=255)
    full_name_of_party_1_signatory  = serializers.CharField(max_length=150)
    party_1_date_of_signing_contract = serializers.DateField()
    full_name_of_party_1_witness  = serializers.CharField(max_length=150)
    party_1_witness_date_of_signing_contract = serializers.DateField()
    will_the_contract_signed_by_pary_2_contracting_entity = serializers.BooleanField(default=False)
    party_2_signatory_scanned_copy_url  = serializers.CharField(max_length=255)
    full_name_of_party_2_signatory  = serializers.CharField(max_length=150)
    party_2_date_of_signing_contract = serializers.DateField()
    full_name_of_party_2_witness  = serializers.CharField(max_length=150)
    party_2_witness_date_of_signing_contract = serializers.DateField()


    def create(self, validated_data):
        """
        Create and return new software agreement.
        """
        # Create software agreement on localhost
        SoftwareLicenseAgreementSerializer.objects.create(document = validated_data)
        # Retrieve license and return license
        software_license = SoftwareLicenseAgreementSerializer.objects.last()

        # Create software agreement on remote server
        save_document()


        return software_license


    def update(self, instance, validated_data):
        """
        Update and return software agreement.
        """

        instance.document = validated_data
        instance.save()
        return instance