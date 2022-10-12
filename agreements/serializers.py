from datetime import datetime
from rest_framework import serializers
import json
from utils.dowell import (
    fetch_document,
    save_document,
    update_document,

    SOFTWARE_AGREEMENT_COLLECTION,
    SOFTWARE_AGREEMENT_DOCUMENT_NAME,
    SOFTWARE_AGREEMENT_KEY

)


from . generate_policy_pdf_document import create_pdf_document


# sample 
context = {
    "_id":"dldndeoe-eeldld-eldlld-3344",
    "software_product_license_name": "Apache v2.0",
    "software_product": "Friends Packet",
    "software_product_license_name_uc": "Packet 400",
    "liability_remedy_amount": "2000.00",
    "state_law_applies": "India",
    "license_jurisdiction_city": "Mubai",
    "license_jurisdiction_state": "India",
    "license_representative_name": "Charu",
    "license_representative_address": "784 state road",
    "license_representative_city": "Mubai",
    "license_representative_state": "India",
    "license_representative_zipcode": "00245",
    "license_representative_phone": "02154555555",
    "license_representative_email": "sample@sample.com"
    }

create_pdf_document(context, "end-user-licensing-agreement.html")






class SoftwareLicensePolicySerializer(serializers.Serializer):
    """ Validate attribute, create and update software
        license agreement document
    """
    date_of_execution_of_document = serializers.DateField()
    party_1_entity_type = serializers.CharField(max_length=50)
    party_1_full_name = serializers.CharField(max_length=150)
    party_1_postal_address = serializers.CharField(max_length=255)
    party_1_jurisdiction_incorporated = serializers.CharField(max_length=150)
    party_1_registration_number = serializers.CharField(max_length=50)
    party_1_registrar_office_address = serializers.CharField(max_length=255)
    party_1_principal_place_of_business = serializers.CharField(max_length=255)
    party_2_entity_type = serializers.CharField(max_length=50)
    party_2_full_name = serializers.CharField(max_length=150)
    party_2_postal_address = serializers.CharField(max_length=255)
    party_2_jurisdiction_incorporated = serializers.CharField(max_length=150)
    party_2_registration_number = serializers.CharField(max_length=50)
    party_2_registrar_office_address = serializers.CharField(max_length=255)
    party_2_principal_place_of_business = serializers.CharField(max_length=255)
    charges_payable = serializers.DecimalField(
        max_digits=18, decimal_places=2, default=0)
    software_document_identification = serializers.CharField(max_length=255)
    contract_effective_date = serializers.DateField()
    minimum_terms_apply = serializers.CharField(max_length=50)
    is_software_form_specified = serializers.BooleanField(default=False)
    software_form = serializers.CharField(max_length=100)
    is_non_material_defects_count_as_software_defects = serializers.BooleanField(
        default=False)
    ways_defect_affect_software = serializers.CharField(max_length=255)
    is_set_of_exclusions_included = serializers.BooleanField(default=False)
    exclusions_apply = serializers.CharField(max_length=255)
    software_specification = serializers.CharField(max_length=255)
    can_software_specification_be_varied_by_the_parties = serializers.BooleanField(
        default=False)
    terms_of_contract_duration = serializers.CharField(max_length=50)
    is_inline_copy_right_remove = serializers.BooleanField(default=False)
    is_term_of_contract_indefinite = serializers.BooleanField(default=False)
    contract_termination_date = serializers.DateField()
    events_that_will_cause_contract_to_be_terminated = serializers.CharField(
        max_length=255)
    number_of_license_to_be_deliver = serializers.IntegerField(default=1)
    software_delivery_channel = serializers.CharField(max_length=50)
    software_delivery_period = serializers.CharField(max_length=50)
    what_did_licensor_supply_to_the_licensee = serializers.CharField(
        max_length=150)
    purpose_of_supply = serializers.CharField(max_length=255)
    when_should_invoice_be_issued = serializers.CharField(max_length=255)
    invoicing_date = serializers.DateField()
    period_for_payment_of_invoices = serializers.CharField(max_length=50)
    effective_date_for_invoice_payment = serializers.DateField()
    invoice_payment_method = serializers.CharField(max_length=100)
    interest_rate_apply_to_late_payment = serializers.DecimalField(
        max_digits=18, decimal_places=2, default=0)
    optional_element_warranty = serializers.CharField(max_length=255)
    is_warranty_relate_to_a_specific_period = serializers.BooleanField(
        default=False)
    period_apply_to_warranty = serializers.CharField(max_length=50)
    scope_of_warranty = serializers.CharField(max_length=255)
    jurisdictional_coverage_of_warranty = serializers.CharField(max_length=255)
    circumstances_in_which_licensor_may_exercise_its_rights = serializers.CharField(
        max_length=255)
    should_there_be_an_express_requirement_for_licensor_to_act_reasonably = serializers.BooleanField(
        default=False)
    are_there_limitations_on_right_to_modify = serializers.BooleanField(
        default=False)
    limitations_on_right_to_modify_specification = serializers.CharField(
        max_length=255)
    termination_notice_period_apply = serializers.BooleanField(default=False)
    is_termination_period_expirable = serializers.BooleanField(default=False)
    relevant_termination_period = serializers.CharField(max_length=50)
    circumstances_in_which_a_party_may_terminate_for_breach = serializers.CharField(
        max_length=255)
    time_frame_for_the_notice_period = serializers.CharField(max_length=50)
    
    contact_details_to_sent_contractual_notices_to_the_licensor = serializers.CharField(
        max_length=255)
    contact_details_to_sent_contractual_notices_to_the_licensee = serializers.CharField(
        max_length=255)
    law_governs_document = serializers.CharField(max_length=255)
    court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document = serializers.CharField(
        max_length=255)
    will_the_contract_signed_by_party_1_contracting_entity = serializers.BooleanField(
        default=False)
    party_1_signatory_scanned_copy_url = serializers.CharField(max_length=255)
    full_name_of_party_1_signatory = serializers.CharField(max_length=150)
    party_1_date_of_signing_contract = serializers.DateField()
    full_name_of_party_1_witness = serializers.CharField(max_length=150)
    party_1_witness_date_of_signing_contract = serializers.DateField()
    will_the_contract_signed_by_pary_2_contracting_entity = serializers.BooleanField(
        default=False)
    party_2_signatory_scanned_copy_url = serializers.CharField(max_length=255)
    full_name_of_party_2_signatory = serializers.CharField(max_length=150)
    party_2_date_of_signing_contract = serializers.DateField()
    full_name_of_party_2_witness = serializers.CharField(max_length=150)
    party_2_witness_date_of_signing_contract = serializers.DateField()

    software_product_license_name = serializers.CharField(max_length=150)
    software_product = serializers.CharField(max_length=150)
    software_product_license_name_uc = serializers.CharField(max_length=150)
    liability_remedy_amount = serializers.CharField(max_length=150)
    state_law_applies = serializers.CharField(max_length=150)
    license_jurisdiction_city = serializers.CharField(max_length=150)
    license_jurisdiction_state = serializers.CharField(max_length=150)
    license_representative_address = serializers.CharField(max_length=150)
    license_representative_city = serializers.CharField(max_length=150)
    license_representative_state = serializers.CharField(max_length=150)
    license_representative_zipcode = serializers.CharField(max_length=150)
    license_representative_phone = serializers.CharField(max_length=150)
    license_representative_email = serializers.CharField(max_length=150)

    def create(self, validated_data):
        """
        Create and return new software agreement.
        """

        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        validated_data["effective_date_for_invoice_payment"]\
            = validated_data["effective_date_for_invoice_payment"].isoformat()

        validated_data["party_1_date_of_signing_contract"]\
            = validated_data["party_1_date_of_signing_contract"].isoformat()

        validated_data["party_1_witness_date_of_signing_contract"]\
            = validated_data["party_1_witness_date_of_signing_contract"].isoformat()

        validated_data["party_2_date_of_signing_contract"]\
            = validated_data["party_2_date_of_signing_contract"].isoformat()

        validated_data["party_2_witness_date_of_signing_contract"]\
            = validated_data["party_2_witness_date_of_signing_contract"].isoformat()

        validated_data["invoicing_date"]\
            = validated_data["invoicing_date"].isoformat()

        validated_data["contract_termination_date"]\
            = validated_data["contract_termination_date"].isoformat()

        validated_data["contract_effective_date"]\
            = validated_data["contract_effective_date"].isoformat()

        validated_data["charges_payable"] = float(
            validated_data["charges_payable"])

        validated_data["interest_rate_apply_to_late_payment"] = float(
            validated_data["interest_rate_apply_to_late_payment"])


        # Generate pdf document
        filename = create_pdf_document(validated_data, "softwarelicensepolicy.html")
        validated_data['pdf_policy_generated_name'] = filename


        # Create software agreement on remote server
        response_json = save_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            value=validated_data
        )

        if response_json["isSuccess"]:
            status_code = 201
            # Retrieve license on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": response_json["event_id"]}
            )

        return response_json, status_code

    def update(self, event_id, validated_data):
        """
        Update and return software agreement.
        """
        status_code = 500
        response_json = {}

        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        validated_data["effective_date_for_invoice_payment"]\
            = validated_data["effective_date_for_invoice_payment"].isoformat()

        validated_data["party_1_date_of_signing_contract"]\
            = validated_data["party_1_date_of_signing_contract"].isoformat()

        validated_data["party_1_witness_date_of_signing_contract"]\
            = validated_data["party_1_witness_date_of_signing_contract"].isoformat()

        validated_data["party_2_date_of_signing_contract"]\
            = validated_data["party_2_date_of_signing_contract"].isoformat()

        validated_data["party_2_witness_date_of_signing_contract"]\
            = validated_data["party_2_witness_date_of_signing_contract"].isoformat()

        validated_data["invoicing_date"]\
            = validated_data["invoicing_date"].isoformat()

        validated_data["contract_termination_date"]\
            = validated_data["contract_termination_date"].isoformat()

        validated_data["contract_effective_date"]\
            = validated_data["contract_effective_date"].isoformat()

        validated_data["charges_payable"] = float(
            validated_data["charges_payable"])

        validated_data["interest_rate_apply_to_late_payment"] = float(
            validated_data["interest_rate_apply_to_late_payment"])


        # Generate pdf document
        filename = create_pdf_document(validated_data, "enduserlicensingagreement.html")
        validated_data['pdf_document_generated'] = filename



        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=event_id
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )

        return response_json, status_code


class EulaSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        end-user-license-agreement document
    """

    software_product_license_name = serializers.CharField(max_length=150)
    software_product = serializers.CharField(max_length=150)
    software_product_license_name_uc = serializers.CharField(max_length=150)
    liability_remedy_amount = serializers.CharField(max_length=150)
    state_law_applies = serializers.CharField(max_length=150)
    license_jurisdiction_city = serializers.CharField(max_length=150)
    license_jurisdiction_state = serializers.CharField(max_length=150)
    license_representative_name = serializers.CharField(max_length=150)
    license_representative_address = serializers.CharField(max_length=150)
    license_representative_city = serializers.CharField(max_length=150)
    license_representative_state = serializers.CharField(max_length=150)
    license_representative_zipcode = serializers.CharField(max_length=150)
    license_representative_phone = serializers.CharField(max_length=150)
    license_representative_email = serializers.CharField(max_length=150)


    def create(self, validated_data):
        """
        Create and return new software agreement.
        """

        # # Generate pdf document
        # filename = create_pdf_document(validated_data, "enduserlicensingagreement.html")
        # validated_data['pdf_policy_generated_name'] = filename


        # Create software agreement on remote server
        response_json = save_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            value=validated_data
        )

        if response_json["isSuccess"]:
            status_code = 201
            # Retrieve license on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": response_json["event_id"]}
            )

        return response_json, status_code

    def update(self, event_id, validated_data):
        """
        Update and return software agreement.
        """
        status_code = 500
        response_json = {}

        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        validated_data["effective_date_for_invoice_payment"]\
            = validated_data["effective_date_for_invoice_payment"].isoformat()

        validated_data["party_1_date_of_signing_contract"]\
            = validated_data["party_1_date_of_signing_contract"].isoformat()

        validated_data["party_1_witness_date_of_signing_contract"]\
            = validated_data["party_1_witness_date_of_signing_contract"].isoformat()

        validated_data["party_2_date_of_signing_contract"]\
            = validated_data["party_2_date_of_signing_contract"].isoformat()

        validated_data["party_2_witness_date_of_signing_contract"]\
            = validated_data["party_2_witness_date_of_signing_contract"].isoformat()

        validated_data["invoicing_date"]\
            = validated_data["invoicing_date"].isoformat()

        validated_data["contract_termination_date"]\
            = validated_data["contract_termination_date"].isoformat()

        validated_data["contract_effective_date"]\
            = validated_data["contract_effective_date"].isoformat()

        validated_data["charges_payable"] = float(
            validated_data["charges_payable"])

        validated_data["interest_rate_apply_to_late_payment"] = float(
            validated_data["interest_rate_apply_to_late_payment"])


        # # Generate pdf document
        # filename = create_pdf_document(validated_data, "enduserlicensingagreement.html")
        # validated_data['pdf_document_generated'] = filename



        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=event_id
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )

        return response_json, status_code
