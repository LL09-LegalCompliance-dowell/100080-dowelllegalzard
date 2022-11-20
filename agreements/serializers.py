from datetime import datetime
from email.policy import default
from rest_framework import serializers
import json
from utils.dowell import (
    fetch_document,
    save_document,
    update_document,

    SOFTWARE_AGREEMENT_COLLECTION,
    SOFTWARE_AGREEMENT_DOCUMENT_NAME,
    SOFTWARE_AGREEMENT_KEY,
    ATTRIBUTE_COLLECTION,
    ATTRIBUTE_DOCUMENT_NAME,
    ATTRIBUTE_MAIN_KEY

)
from .generate_agreement_compliance_pdf import create_pdf_document

# data = {
#             "_id": "62f61602d8e350aa754b84c7",
#             "eventId": "FB1010000000001660294653510514",
#             "agreement": {
#                 "agreement_compliance_type": "eula",
#                 "date_of_execution_of_document": "2025-10-20",
#                 "party_1_entity_type": "Individual",
#                 "party_1_full_name": "Dowell Research 1",
#                 "party_1_postal_address": "P.O.BOX 45, India",
#                 "party_1_jurisdiction_incorporated": "sample law",
#                 "party_1_registration_number": "RS5428888",
#                 "party_1_registrar_office_address": "sample office address",
#                 "party_1_principal_place_of_business": "India",
#                 "party_2_entity_type": "Organization",
#                 "party_2_full_name": "Organization Name",
#                 "party_2_postal_address": "P.O.BOX 87",
#                 "party_2_jurisdiction_incorporated": "USA",
#                 "party_2_registration_number": "459996665",
#                 "party_2_registrar_office_address": "Some where in USA",
#                 "party_2_principal_place_of_business": "USA"
#             }
#         }

# create_pdf_document(data)




class SoftwareLicensePolicySerializer(serializers.Serializer):
    """ Validate attribute, create and update software
        license agreement document
    """
    agreement_compliance_type = serializers.CharField(max_length=200)
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

            # Generate pdf
            create_pdf_document(response_json['data'][0])

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

            # Generate pdf
            create_pdf_document(response_json['data'][0])

        return response_json, status_code


class EulaSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        end-user-license-agreement document
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    date_of_execution_of_document = serializers.DateField()
    party_details_full_name = serializers.CharField(max_length=150)
    party_details_company_name = serializers.CharField(max_length=150)
    party_details_address_line_1 = serializers.CharField(max_length=300)
    party_details_address_line_2 = serializers.CharField(max_length=300)
    party_details_address_line_3 = serializers.CharField(max_length=300)
    party_details_city = serializers.CharField(max_length=150)
    party_details_country = serializers.CharField(max_length=150)
    party_details_state = serializers.CharField(max_length=150)
    party_details_zipcode = serializers.CharField(max_length=150)
    party_details_phone = serializers.CharField(max_length=150)
    party_details_email = serializers.CharField(max_length=150)

    company_details_nature_of_company = serializers.CharField(max_length=150)
    software_product = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    software_product_license_name = serializers.CharField(max_length=150)
    software_product_license_name_uc = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")

    liability_remedy_amount = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    state_law_applies = serializers.CharField(max_length=150)
    jurisdiction_city = serializers.CharField(max_length=150)
    jurisdiction_state = serializers.CharField(max_length=150)
    date_of_commencement = serializers.DateField()
    is_maintenance_or_support_available_for_app = serializers.BooleanField(default=False)
    will_it_state_number_of_maintenance_and_schedules = serializers.BooleanField(default=False)
    at_which_point_will_users_be_bound_by_terms = serializers.CharField(max_length=150)
    will_users_be_able_to_install_app_on_multiple_device = serializers.BooleanField(default=False)
    violations_that_enable_app_provider_to_cancel_agreement = serializers.CharField(max_length=300)


    def create(self, validated_data):
        """
        Create and return new software agreement.
        """

        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        validated_data["date_of_commencement"]\
            = validated_data["date_of_commencement"].isoformat()

        validated_data["liability_remedy_amount"] = float(
            validated_data["liability_remedy_amount"])


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

            # Generate pdf
            create_pdf_document(response_json['data'][0])

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

        validated_data["date_of_commencement"]\
            = validated_data["date_of_commencement"].isoformat()

        validated_data["liability_remedy_amount"] = float(
            validated_data["liability_remedy_amount"])

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

            # Generate pdf
            create_pdf_document(response_json['data'][0])

        return response_json, status_code



class MOUSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        MOU document
    """

    PERIOD_MENTIONED = (("Days", "Days"), ("Months", "Months"), ("Years", "Years"))

    agreement_compliance_type = serializers.CharField(max_length=200)
    date_of_execution_of_document = serializers.DateField()
    party_1_entity_type = serializers.CharField(max_length=50)
    party_1_full_name = serializers.CharField(max_length=150)
    party_1_address_line_1 = serializers.CharField(max_length=255)
    party_1_address_line_2 = serializers.CharField(max_length=255)
    party_1_address_line_3 = serializers.CharField(max_length=255)
    party_1_zipcode = serializers.CharField(max_length=20)
    party_1_state = serializers.CharField(max_length=50)
    party_1_country = serializers.CharField(max_length=50)
    # party_1_period_mentioned = serializers.CharField(choices = PERIOD_MENTIONED)
    party_2_entity_type = serializers.CharField(max_length=50)
    party_2_full_name = serializers.CharField(max_length=150)
    party_2_address_line_1 = serializers.CharField(max_length=255)
    party_2_address_line_2 = serializers.CharField(max_length=255)
    party_2_address_line_3 = serializers.CharField(max_length=255)
    party_2_zipcode = serializers.CharField(max_length=20)
    party_2_state = serializers.CharField(max_length=50)
    party_2_country = serializers.CharField(max_length=50)
    # party_2_period_mentioned = serializers.CharField(max_length=50, choices = PERIOD_MENTIONED)
    what_will_be_the_purpose_of_this_mou = serializers.CharField(max_length=1000)
    what_is_the_objective_of_this_mou = serializers.CharField(max_length=1000)
    date_of_commencement = serializers.DateField()
    date_of_termination = serializers.DateField()
    # period_for_notice_in_case_of_cancellation_or_amendment = serializers.CharField(choices = PERIOD_MENTIONED)

    state_of_laws_use_as_governing_laws = serializers.CharField(max_length=50)
    state_of_laws_for_governing_laws_in_case_of_reimbursement = serializers.CharField(max_length=50)
    number_of_parties_enter_this_mou = serializers.CharField(max_length=255)
    mou_include_confidentiality = serializers.BooleanField(default=False)
    mou_retrict_working_with_competitors = serializers.BooleanField(default=False)
    
    party_2_entity_type = serializers.CharField(max_length=50)
    party_2_full_name = serializers.CharField(max_length=150)
    party_2_postal_address = serializers.CharField(max_length=255)
    party_2_jurisdiction_incorporated = serializers.CharField(max_length=150)
    party_2_registration_number = serializers.CharField(max_length=50)
    party_2_registrar_office_address = serializers.CharField(max_length=255)
    party_2_principal_place_of_business = serializers.CharField(max_length=255)

    company_details_nature_of_company = serializers.CharField(max_length=150)
    software_product = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    software_product_license_name = serializers.CharField(max_length=150)
    software_product_license_name_uc = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")

    liability_remedy_amount = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    state_law_applies = serializers.CharField(max_length=150)
    jurisdiction_city = serializers.CharField(max_length=150)
    jurisdiction_state = serializers.CharField(max_length=150)
    date_of_commencement = serializers.DateField()
    is_maintenance_or_support_available_for_app = serializers.BooleanField(default=False)
    will_it_state_number_of_maintenance_and_schedules = serializers.BooleanField(default=False)
    at_which_point_will_users_be_bound_by_terms = serializers.CharField(max_length=150)
    will_users_be_able_to_install_app_on_multiple_device = serializers.BooleanField(default=False)
    violations_that_enable_app_provider_to_cancel_agreement = serializers.CharField(max_length=300)


    def create(self, validated_data):
        """
        Create and return new software agreement.
        """

        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        validated_data["date_of_commencement"]\
            = validated_data["date_of_commencement"].isoformat()

        validated_data["liability_remedy_amount"] = float(
            validated_data["liability_remedy_amount"])


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

            # Generate pdf
            create_pdf_document(response_json['data'][0])

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

        validated_data["date_of_commencement"]\
            = validated_data["date_of_commencement"].isoformat()

        validated_data["liability_remedy_amount"] = float(
            validated_data["liability_remedy_amount"])

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

            # Generate pdf
            create_pdf_document(response_json['data'][0])
            
        return response_json, status_code

