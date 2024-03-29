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
)


class SoftwareLicensePolicySerializer(serializers.Serializer):
    """ Validate attribute, create and update software
        license agreement document
    """
    agreement_compliance_type = serializers.CharField(max_length=200)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    date_of_execution_of_document = serializers.DateField()
    party_1_entity_type = serializers.CharField(max_length=50)
    party_1_full_name = serializers.CharField(max_length=150)
    party_1_postal_address = serializers.CharField(max_length=255)
    party_1_jurisdiction_incorporated = serializers.CharField(max_length=150)
    party_1_registration_number = serializers.CharField(max_length=50)
    party_1_registrar_office_address_1 = serializers.CharField(max_length=255)
    party_1_registrar_office_address_2 = serializers.CharField(max_length=255,allow_blank=True, required=False, default="")
    party_1_registrar_office_address_3 = serializers.CharField(max_length=255,allow_blank=True, required=False, default="")
    party_1_principal_place_of_business = serializers.CharField(max_length=255)
    party_2_entity_type = serializers.CharField(max_length=50)
    party_2_full_name = serializers.CharField(max_length=150)
    party_2_postal_address = serializers.CharField(max_length=255)
    party_2_jurisdiction_incorporated = serializers.CharField(max_length=150)
    party_2_registration_number = serializers.CharField(max_length=50)
    party_2_registrar_office_address_1 = serializers.CharField(max_length=255)
    party_2_registrar_office_address_2 = serializers.CharField(max_length=255,allow_blank=True, required=False, default="")
    party_2_registrar_office_address_3 = serializers.CharField(max_length=255,allow_blank=True, required=False, default="")
    party_2_principal_place_of_business = serializers.CharField(max_length=255)
    charges_payable = serializers.DecimalField(max_digits=18, decimal_places=2, default=0)
    software_document_identification = serializers.CharField(max_length=255, allow_blank=True, required=False, default="")
    contract_effective_date = serializers.DateField()
    minimum_terms_apply = serializers.IntegerField(default=1)
    minimum_terms_apply_unit = serializers.CharField(max_length=50)
    is_software_form_specified = serializers.BooleanField(default=False)
    software_form = serializers.CharField(max_length=100)
    is_non_material_defects_count_as_software_defects = serializers.BooleanField(
        default=False)
    ways_defect_affect_software = serializers.CharField(max_length=255)
    is_set_of_exclusions_included = serializers.BooleanField(default=False)
    exclusions_apply = serializers.CharField(max_length=255,allow_blank=True, required=False, default="")
    software_specification = serializers.CharField(max_length=255)
    can_software_specification_be_varied_by_the_parties = serializers.BooleanField(
        default=False)
    terms_of_contract_duration = serializers.IntegerField(default=0)
    terms_of_contract_duration_unit = serializers.CharField(max_length=50)
    is_inline_copy_right_remove = serializers.BooleanField(default=False)
    is_term_of_contract_indefinite = serializers.CharField(max_length=255, allow_blank=True, required=False, default="")
    contract_termination_date = serializers.DateField()
    events_that_will_cause_contract_to_be_terminated = serializers.CharField(
        max_length=255)
    number_of_license_to_be_deliver = serializers.IntegerField(default=1)
    number_of_license_to_be_deliver_unit = serializers.CharField(max_length=50)
    software_delivery_channel = serializers.CharField(max_length=100)
    within_what_period_must_software_be_delivered = serializers.IntegerField(default=1)
    within_what_period_must_software_be_delivered_unit = serializers.CharField(max_length=50)
    what_did_licensor_supply_to_the_licensee = serializers.CharField(max_length=150)
    purpose_by_reference_to_which_sub_licensing_is_permitted = serializers.CharField(max_length=255)
    when_should_invoice_be_issued = serializers.CharField(max_length=255)
    invoicing_date = serializers.DateField()
    period_for_payment_of_invoices = serializers.IntegerField(default=1)
    period_for_payment_of_invoices_unit = serializers.CharField(max_length=50)
    effective_date_for_invoice_payment = serializers.DateField()
    invoice_payment_method = serializers.CharField(max_length=100)
    interest_rate_apply_to_late_payment = serializers.DecimalField(
        max_digits=18, decimal_places=2, default=0)

    add_warranty_optional_element = serializers.BooleanField(default=False)
    optional_element = serializers.CharField(max_length=500,allow_blank=True, required=False, default="")
    is_warranty_relate_to_a_specific_period = serializers.BooleanField(
        default=False)
    scope_of_warranty = serializers.CharField(max_length=255,allow_blank=True, required=False, default="")
    jurisdictional_coverage_of_warranty = serializers.CharField(max_length=255)
    period_apply_to_warranty = serializers.IntegerField(default=0)
    period_apply_to_warranty_unit = serializers.CharField(max_length=50)
    circumstances_in_which_licensor_may_exercise_its_rights = serializers.CharField(
        max_length=255)
    should_there_be_an_express_requirement_for_licensor_to_act_reasonably = serializers.BooleanField(
        default=False)
    are_there_limitations_on_right_to_modify = serializers.BooleanField(
        default=False)
    limitations_on_right_to_modify_specification = serializers.CharField(
        max_length=255)
    termination_notice_period_apply = serializers.IntegerField(default=1)
    termination_notice_period_apply_unit = serializers.CharField(max_length=50)
    is_termination_period_expirable = serializers.BooleanField(default=False)
    relevant_termination_period = serializers.IntegerField(default=0)
    relevant_termination_period_unit = serializers.CharField(max_length=50)
    relevant_termination_period_date = serializers.DateField()
    circumstances_in_which_a_party_may_terminate_for_breach = serializers.CharField(
        max_length=255)
    time_frame_for_the_notice_period = serializers.IntegerField(default=0)
    time_frame_for_the_notice_period_unit = serializers.CharField(max_length=50)
    sent_contractual_notices_to_the_licensor_name = serializers.CharField(
        max_length=255)
    sent_contractual_notices_to_the_licensor_address_1 = serializers.CharField(
        max_length=255)
    sent_contractual_notices_to_the_licensor_address_2 = serializers.CharField(
        max_length=255)
    sent_contractual_notices_to_the_licensor_address_3 = serializers.CharField(
        max_length=255)
    sent_contractual_notices_to_the_licensor_contact_details = serializers.CharField(
        max_length=500)
    sent_contractual_notices_to_the_licensee_name = serializers.CharField(
        max_length=255)
    sent_contractual_notices_to_the_licensee_address_1 = serializers.CharField(
        max_length=255)
    sent_contractual_notices_to_the_licensee_address_2 = serializers.CharField(
        max_length=255)
    sent_contractual_notices_to_the_licensee_address_3 = serializers.CharField(
        max_length=255)
    sent_contractual_notices_to_the_licensee_contact_details = serializers.CharField(
        max_length=500)
    law_governs_document = serializers.CharField(max_length=255)
    court_of_jurisdiction_which_has_exclusive_right_to_adjudicate_disputes_on_document = serializers.CharField(
        max_length=255)
    which_entity_will_sign_contract_on_behalf_of_party_1 = serializers.CharField(max_length=255)
    party_1_signatory_scanned_copy_detail = serializers.DictField()
    full_name_of_party_1_signatory = serializers.CharField(max_length=150)
    party_1_date_of_signing_contract = serializers.DateField()
    full_name_of_the_person_sign_on_behalf_of_party_1 = serializers.CharField(max_length=150)
    date_contract_was_sign_on_behalf_of_party_1 = serializers.DateField()
    which_entity_will_sign_contract_on_behalf_of_party_2 = serializers.CharField(max_length=255)    
    party_2_signatory_scanned_copy_detail = serializers.DictField()
    full_name_of_party_2_signatory = serializers.CharField(max_length=150)
    party_2_date_of_signing_contract = serializers.DateField()
    full_name_of_the_person_sign_on_behalf_of_party_2 = serializers.CharField(max_length=150)
    date_contract_was_sign_on_behalf_of_party_2 = serializers.DateField()
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500,allow_blank=True, required=False, default="")


    def create(self, validated_data):
        """
        Create and return new software agreement.
        """
        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        validated_data["contract_effective_date"]\
            = validated_data["contract_effective_date"].isoformat()

        validated_data["contract_termination_date"]\
            = validated_data["contract_termination_date"].isoformat()

        validated_data["invoicing_date"]\
            = validated_data["invoicing_date"].isoformat()

        validated_data["effective_date_for_invoice_payment"]\
            = validated_data["effective_date_for_invoice_payment"].isoformat()

        validated_data["relevant_termination_period_date"]\
            = validated_data["relevant_termination_period_date"].isoformat()

        validated_data["party_1_date_of_signing_contract"]\
            = validated_data["party_1_date_of_signing_contract"].isoformat()

        validated_data["date_contract_was_sign_on_behalf_of_party_1"]\
            = validated_data["date_contract_was_sign_on_behalf_of_party_1"].isoformat()

        validated_data["party_2_date_of_signing_contract"]\
            = validated_data["party_2_date_of_signing_contract"].isoformat()

        validated_data["date_contract_was_sign_on_behalf_of_party_2"]\
            = validated_data["date_contract_was_sign_on_behalf_of_party_2"].isoformat()

        validated_data["charges_payable"] = float(
            validated_data["charges_payable"])

        validated_data["interest_rate_apply_to_late_payment"] = float(
            validated_data["interest_rate_apply_to_late_payment"])



        # Create software agreement on remote server
        response_json = save_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            value=validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return software agreement.
        """
        status_code = 500
        response_json = {}


        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()


        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        validated_data["contract_effective_date"]\
            = validated_data["contract_effective_date"].isoformat()

        validated_data["contract_termination_date"]\
            = validated_data["contract_termination_date"].isoformat()

        validated_data["invoicing_date"]\
            = validated_data["invoicing_date"].isoformat()

        validated_data["effective_date_for_invoice_payment"]\
            = validated_data["effective_date_for_invoice_payment"].isoformat()

        validated_data["relevant_termination_period_date"]\
            = validated_data["relevant_termination_period_date"].isoformat()

        validated_data["party_1_date_of_signing_contract"]\
            = validated_data["party_1_date_of_signing_contract"].isoformat()

        validated_data["date_contract_was_sign_on_behalf_of_party_1"]\
            = validated_data["date_contract_was_sign_on_behalf_of_party_1"].isoformat()

        validated_data["party_2_date_of_signing_contract"]\
            = validated_data["party_2_date_of_signing_contract"].isoformat()

        validated_data["date_contract_was_sign_on_behalf_of_party_2"]\
            = validated_data["date_contract_was_sign_on_behalf_of_party_2"].isoformat()

        validated_data["charges_payable"] = float(
            validated_data["charges_payable"])

        validated_data["interest_rate_apply_to_late_payment"] = float(
            validated_data["interest_rate_apply_to_late_payment"])


        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )


        return response_json, status_code


class EulaSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        end-user-license-agreement document
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    date_of_execution_of_document = serializers.DateField()
    party_details_full_name = serializers.CharField(max_length=150)
    party_details_company_name = serializers.CharField(max_length=150)
    party_details_address_line_1 = serializers.CharField(max_length=300)
    party_details_address_line_2 = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    party_details_address_line_3 = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    party_details_country = serializers.CharField(max_length=150)
    party_details_state = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    party_details_zipcode = serializers.CharField(max_length=150)
    party_details_phone = serializers.CharField(max_length=150)
    party_details_email = serializers.CharField(max_length=150)

    company_details_nature_of_company = serializers.CharField(max_length=150)
    software_product = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    software_product_license_name = serializers.CharField(max_length=150)

    liability_remedy_amount = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    liability_remedy_amount_currency = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    state_law_applies = serializers.CharField(max_length=150)
    jurisdiction_city = serializers.CharField(max_length=150)
    jurisdiction_state = serializers.CharField(max_length=150)
    date_of_commencement = serializers.DateField()
    is_maintenance_or_support_available_for_app = serializers.BooleanField(default=False)
    will_it_state_number_of_maintenance_and_schedules = serializers.BooleanField(default=False)
    at_which_point_will_users_be_bound_by_terms = serializers.CharField(max_length=150)
    will_users_be_able_to_install_app_on_multiple_device = serializers.BooleanField(default=False)
    violations_that_enable_app_provider_to_cancel_agreement = serializers.CharField(max_length=300)
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")


    def create(self, validated_data):
        """
        Create and return new end-user-license-agreement.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        validated_data["date_of_commencement"]\
            = validated_data["date_of_commencement"].isoformat()

        validated_data["liability_remedy_amount"] = float(
            validated_data["liability_remedy_amount"])


        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return end-user-license-agreement.
        """
        status_code = 500
        response_json = {}

        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

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
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code



class MOUSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        MOU document
    """

    PERIOD_MENTIONED = (("Days", "Days"), ("Months", "Months"), ("Years", "Years"))

    agreement_compliance_type = serializers.CharField(max_length=200)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    date_of_execution_of_document = serializers.DateField()
    party_1_entity_type = serializers.CharField(max_length=50)
    party_1_full_name = serializers.CharField(max_length=150)
    party_1_address_line_1 = serializers.CharField(max_length=255)
    party_1_address_line_2 = serializers.CharField(max_length=255)
    party_1_address_line_3 = serializers.CharField(max_length=255)
    party_1_zipcode = serializers.CharField(max_length=20)
    party_1_state = serializers.CharField(max_length=50)
    party_1_country = serializers.CharField(max_length=50)
    party_1_period_mentioned = serializers.IntegerField(default = 0)
    party_1_period_mentioned_unit = serializers.ChoiceField(choices = PERIOD_MENTIONED, default="Days")
    party_2_entity_type = serializers.CharField(max_length=50)
    party_2_full_name = serializers.CharField(max_length=150)
    party_2_address_line_1 = serializers.CharField(max_length=255)
    party_2_address_line_2 = serializers.CharField(max_length=255)
    party_2_address_line_3 = serializers.CharField(max_length=255)
    party_2_zipcode = serializers.CharField(max_length=20)
    party_2_state = serializers.CharField(max_length=50)
    party_2_country = serializers.CharField(max_length=50)
    party_2_period_mentioned = serializers.IntegerField(default = 0)
    party_2_period_mentioned_unit = serializers.ChoiceField(choices = PERIOD_MENTIONED, default="Days")
    what_will_be_the_purpose_of_this_mou = serializers.CharField(max_length=2000)
    what_is_the_objective_of_this_mou = serializers.CharField(max_length=2000)
    date_of_commencement = serializers.DateField()
    date_of_termination = serializers.DateField()
    period_for_notice_in_case_of_cancellation_or_amendment = serializers.IntegerField(default = 0)
    period_for_notice_in_case_of_cancellation_or_amendment_unit = serializers.ChoiceField(choices = PERIOD_MENTIONED, default="Days")

    state_of_laws_use_as_governing_laws = serializers.CharField(max_length=50)
    state_of_laws_for_governing_laws_in_case_of_reimbursement = serializers.CharField(max_length=50)
    number_of_parties_enter_this_mou = serializers.IntegerField(default=0)
    mou_include_confidentiality = serializers.BooleanField(default=False)
    mou_retrict_working_with_competitors = serializers.BooleanField(default=False)
    period_mou_retrict_working_with_competitors = serializers.IntegerField(default = 0)
    period_mou_retrict_working_with_competitors_unit = serializers.ChoiceField(choices = PERIOD_MENTIONED, default="Days")
    date_for_legally_binding_definitive_agreement = serializers.DateField()
    should_the_parties_agree_to_refrain_from_negotiating_with_third_parties = serializers.BooleanField(default=False)
    will_mou_agreement_be_terminated_in_case_of_force_majeure = serializers.BooleanField(default=False)
    any_other_contracts_entered_between_parties_together_with_this_mou = serializers.BooleanField(default=False)
    organization_id = serializers.CharField(max_length=250)


    project_name = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    project_detail = serializers.CharField(max_length=5000, allow_blank=True, required=False, default="")


    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")
    


    def create(self, validated_data):
        """
        Create and return new momorandum of understanding (MOU).
        """
        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        validated_data["date_of_commencement"]\
            = validated_data["date_of_commencement"].isoformat()

        validated_data["date_of_termination"]\
            = validated_data["date_of_termination"].isoformat()

        validated_data["date_for_legally_binding_definitive_agreement"]\
            = validated_data["date_for_legally_binding_definitive_agreement"].isoformat()



        # Create software agreement on remote server
        response_json = save_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            value=validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return momorandum of understanding (MOU).
        """
        status_code = 500
        response_json = {}


        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()


        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        validated_data["date_of_commencement"]\
            = validated_data["date_of_commencement"].isoformat()

        validated_data["date_of_termination"]\
            = validated_data["date_of_termination"].isoformat()

        validated_data["date_for_legally_binding_definitive_agreement"]\
            = validated_data["date_for_legally_binding_definitive_agreement"].isoformat()


        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )


        return response_json, status_code


class WebsiteTermsOfUseSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        website terms of use document
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    terms_last_updated = serializers.DateField()
    full_name_of_the_party = serializers.CharField(max_length=150)
    website_url = serializers.CharField(max_length=500)
    email_id = serializers.CharField(max_length=300)
    email_id_for_acquiring_written_permission = serializers.CharField(max_length=300)
    liability_limit_amount = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    liability_limit_amount_currency = serializers.CharField(max_length=20)
    liability_must_not_exceed_amount = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    liability_must_not_exceed_amount_currency = serializers.CharField(max_length=20)
    email_id_for_requesting_access_or_correction_of_personal_info = serializers.CharField(max_length=300)
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")


    def create(self, validated_data):
        """
        Create and return website terms of use.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["terms_last_updated"]\
            = validated_data["terms_last_updated"].isoformat()
        validated_data["liability_limit_amount"] = float(
            validated_data["liability_limit_amount"])
        validated_data["liability_must_not_exceed_amount"] = float(
            validated_data["liability_must_not_exceed_amount"])


        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return website terms of use.
        """
        status_code = 500
        response_json = {}


        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["terms_last_updated"]\
            = validated_data["terms_last_updated"].isoformat()
        validated_data["liability_limit_amount"] = float(
            validated_data["liability_limit_amount"])
        validated_data["liability_must_not_exceed_amount"] = float(
            validated_data["liability_must_not_exceed_amount"])

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code

class WebsitePrivacyPolicySerializer(serializers.Serializer):
    """ Validate attribute, create and update
        website privacy policy document
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    last_updated = serializers.DateField()
    company_name = serializers.CharField(max_length=150)
    company_address = serializers.CharField(max_length=500)
    registration_number = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    website_name = serializers.CharField(max_length=100)
    website_url = serializers.CharField(max_length=250)
    website_contact_page_url = serializers.CharField(max_length=500)
    website_contact_email = serializers.CharField(max_length=255)
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")


    def create(self, validated_data):
        """
        Create and return website terms of use.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["last_updated"]\
            = validated_data["last_updated"].isoformat()


        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return website privacy policy .
        """
        status_code = 500
        response_json = {}

        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["last_updated"]\
            = validated_data["last_updated"].isoformat()

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code

class WebsiteSecurityPolicySerializer(serializers.Serializer):
    """ Validate attribute, create and update
        website security policy document
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    last_updated = serializers.DateField()
    company_name = serializers.CharField(max_length=150)
    website_name = serializers.CharField(max_length=100)
    jurisdiction = serializers.CharField(max_length=100)
    website_url = serializers.CharField(max_length=250)
    website_contact_email = serializers.CharField(max_length=255)
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")



    def create(self, validated_data):
        """
        Create and return website security policy.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["last_updated"]\
            = validated_data["last_updated"].isoformat()

        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return website security policy.
        """
        status_code = 500
        response_json = {}


        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["last_updated"]\
            = validated_data["last_updated"].isoformat()

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code


class NonCompeteAgreementSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        non compete agreement document
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    date_of_execution_of_document = serializers.DateField()
    party_full_name = serializers.CharField(max_length=150)
    company_name = serializers.CharField(max_length=150)
    company_address_line_1 = serializers.CharField(max_length=255)
    company_address_line_2 = serializers.CharField(max_length=255)
    company_address_line_3 = serializers.CharField(max_length=255)
    company_zipcode = serializers.CharField(max_length=20)
    type_of_company = serializers.CharField(max_length=100)
    restricted_area = serializers.CharField(max_length=100)
    date_of_termination = serializers.DateField()
    duration_for_solicit = serializers.IntegerField(default = 0)
    duration_for_solicit_unit = serializers.CharField(max_length=20)
    governing_laws_country = serializers.CharField(max_length=50)
    will_there_be_a_litigation_matter_in_case_of_dispute = serializers.BooleanField(default=False)
    which_state_should_abide_litigation_matter = serializers.CharField(max_length=100, allow_blank=True, required=False, default="")
    will_electronic_notices_be_allowed = serializers.CharField(max_length=50, allow_blank=True, required=False, default="")

    name_of_witnesse_1 = serializers.CharField(max_length=100, allow_blank=True, required=False, default="")
    signature_of_witnesse_1_detail = serializers.DictField()
    witnesse_1_address_line_1 = serializers.CharField(max_length=255, allow_blank=True, required=False, default="")
    witnesse_1_address_line_2 = serializers.CharField(max_length=255, allow_blank=True, required=False, default="")
    witnesse_1_address_line_3 = serializers.CharField(max_length=255, allow_blank=True, required=False, default="")
    name_of_witnesse_2 = serializers.CharField(max_length=100, allow_blank=True, required=False, default="")
    signature_of_witnesse_2_detail = serializers.DictField()
    witnesse_2_address_line_1 = serializers.CharField(max_length=255, allow_blank=True, required=False, default="")
    witnesse_2_address_line_2 = serializers.CharField(max_length=255, allow_blank=True, required=False, default="")
    witnesse_2_address_line_3 = serializers.CharField(max_length=255, allow_blank=True, required=False, default="")

    organization_id = serializers.CharField(max_length=250)
    company_nature_of_work = serializers.CharField(max_length=10000, allow_blank=True, required=False, default="")
    employee_job_title = serializers.CharField(max_length=100, allow_blank=True, required=False, default="")



    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")





    def create(self, validated_data):
        """
        Create and return non compete agreement.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()
        validated_data["date_of_termination"]\
            = validated_data["date_of_termination"].isoformat()

        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return non compete agreement.
        """
        status_code = 500
        response_json = {}

        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()
        validated_data["date_of_termination"]\
            = validated_data["date_of_termination"].isoformat()
            

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code


class CookiesPolicySerializer(serializers.Serializer):
    """ Validate attribute, create and update
        cookies policy document
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    date_of_execution_of_document = serializers.DateField()
    party_full_name = serializers.CharField(max_length=150)
    will_the_cookie_store_personal_information = serializers.BooleanField(default=False)
    type_of_personal_information_store_by_cookies = serializers.ListField()
    other_type_of_personal_information_store_by_cookies = serializers.CharField(max_length=100, allow_blank=True, required=False, default="")
    does_your_website_or_app_use_essential_cookies = serializers.BooleanField(default=False)
    does_your_website_or_app_use_any_perfomance_and_functionality_cookies = serializers.BooleanField(default=False)

    does_your_website_or_app_use_marketing_cookies  = serializers.BooleanField(default=False)
    does_your_website_or_app_use_analytic_and_customization_cookies  = serializers.BooleanField(default=False)
    does_your_website_or_app_use_social_media_cookies  = serializers.BooleanField(default=False)

    does_your_website_or_app_use_third_party_cookies = serializers.BooleanField(default=False)
    personal_information_store_by_third_party_cookies = serializers.ListField()
    does_your_website_or_app_show_ads = serializers.BooleanField(default=False)
    website_uses_other_technologies_to_perform_other_functions_achieved_via_cookie = serializers.BooleanField(default=False)
    which_medium_can_website_users_raise_question_regarding_cookies = serializers.DictField()
    provide_situations_where_cookies_may_be_collected_without_consent_of_users = serializers.CharField(max_length=100, allow_blank=True, required=False, default="")
    name_of_third_party_cookies= serializers.CharField(max_length=100)
    owner_of_third_party_cookies= serializers.CharField(max_length=100)
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")



    def create(self, validated_data):
        """
        Create and return cookies policy.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return cookies policy.
        """
        status_code = 500
        response_json = {}

        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code

class AppDisclaimerSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        app disclaimer document
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    last_update = serializers.DateField()
    app_name = serializers.CharField(max_length=150)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")



    def create(self, validated_data):
        """
        Create and return app disclaimer.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()
        validated_data['website_or_app_name'] = validated_data['app_name']

        # format date back to iso format
        validated_data["last_update"]\
            = validated_data["last_update"].isoformat()

        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return app disclaimer.
        """
        status_code = 500
        response_json = {}


        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()
        validated_data['website_or_app_name'] = validated_data['app_name']

        # format date back to iso format
        validated_data["last_update"]\
            = validated_data["last_update"].isoformat()

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code

class ReturnAndRefundSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        return-and-fund document
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    date = serializers.DateField()
    website_or_app_name = serializers.CharField(max_length=150)
    company_info = serializers.CharField(max_length=400)
    website_url = serializers.CharField(max_length=255)
    cancellation_right_of_order= serializers.IntegerField(default=0)
    cancellation_right_of_order_unit= serializers.CharField(max_length=20)
    reimbursement_of_cancellation_money = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    reimbursement_of_cancellation_money_currency= serializers.CharField(max_length=20)
    website_contact_email = serializers.CharField(max_length=255)
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")



    def create(self, validated_data):
        """
        Create return-and-fund.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["date"]\
            = validated_data["date"].isoformat()
        validated_data["reimbursement_of_cancellation_money"] = float(
            validated_data["reimbursement_of_cancellation_money"])

        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update return-and-fund.
        """
        status_code = 500
        response_json = {}


        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["date"]\
            = validated_data["date"].isoformat()
        validated_data["reimbursement_of_cancellation_money"] = float(
            validated_data["reimbursement_of_cancellation_money"])

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code

class AppPrivacyPolicySerializer(serializers.Serializer):
    """ Validate attribute, create and update
        app privacy policy document
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    last_update = serializers.DateField()
    company_name = serializers.CharField(max_length=150)
    app_name = serializers.CharField(max_length=150)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    app_url = serializers.URLField()
    website_contact_page_url = serializers.URLField()
    website_contact_email = serializers.CharField(max_length=255)
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")



    def create(self, validated_data):
        """
        Create and return app privacy policy.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()
        validated_data['website_or_app_name'] = validated_data['app_name']

        # format date back to iso format
        validated_data["last_update"]\
            = validated_data["last_update"].isoformat()

        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return app privacy policy.
        """
        status_code = 500
        response_json = {}

        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()
        validated_data['website_or_app_name'] = validated_data['app_name']

        # format date back to iso format
        validated_data["last_update"]\
            = validated_data["last_update"].isoformat()

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code

class NDASerializer(serializers.Serializer):
    """ Validate attribute, create and update
        non disclosure agreement
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    party_1_full_name = serializers.CharField(max_length=150)
    party_1_address_line_1 = serializers.CharField(max_length=300)
    party_1_address_line_2 = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    party_1_address_line_3 = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    party_1_country = serializers.CharField(max_length=150)
    party_1_state = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    party_1_zipcode = serializers.CharField(max_length=150)
    party_1_city = serializers.CharField(max_length=150)
    party_2_full_name = serializers.CharField(max_length=150)
    party_2_address_line_1 = serializers.CharField(max_length=300)
    party_2_address_line_2 = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    party_2_address_line_3 = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    party_2_country = serializers.CharField(max_length=150)
    party_2_state = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    party_2_zipcode = serializers.CharField(max_length=150)
    party_2_city = serializers.CharField(max_length=150)

    what_shall_be_the_of_term_this_agrement = serializers.IntegerField(default=0)
    what_shall_be_the_of_term_this_agrement_unit = serializers.CharField(max_length=150)
    what_shall_be_the_governing_this_law_this_agrement = serializers.CharField(max_length=150)
    date_of_execution_of_document = serializers.DateField()
    number_of_witness = serializers.IntegerField(default=2)

    witnesses = serializers.ListField()

    will_the_obligations_of_confidentiality_subsist_after_expiry = serializers.BooleanField(default=False)
    what_will_be_the_date_for_termination_of_this_nda = serializers.DateField()
    will_the_party_be_allow_to_enter_into_similar_arragements_with_other_party = serializers.BooleanField(default=False)
    the_period_a_party_is_entitle_to_enter_into_similar_arragement_with_other_party = serializers.IntegerField(default=0)
    the_period_a_party_is_entitle_to_enter_into_similar_arragement_with_other_party_unit = serializers.CharField(max_length=100)
    how_will_the_agreement_be_terminated= serializers.CharField(max_length=100)
    other_medium_agreement_can_be_terminated= serializers.CharField(max_length=200, allow_blank=True, required=False, default="")
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")



    def create(self, validated_data):
        """
        Create and return non disclosure agreement.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()
        validated_data["what_will_be_the_date_for_termination_of_this_nda"]\
            = validated_data["what_will_be_the_date_for_termination_of_this_nda"].isoformat()

        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return non disclosure agreement.
        """
        status_code = 500
        response_json = {}


        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["date_of_execution_of_document"]\
            = validated_data["date_of_execution_of_document"].isoformat()
        validated_data["what_will_be_the_date_for_termination_of_this_nda"]\
            = validated_data["what_will_be_the_date_for_termination_of_this_nda"].isoformat()

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code


class StatementOfWorkSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        non statement of work
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    client_full_name = serializers.CharField(max_length=150)
    jurisdiction = serializers.CharField(max_length=300)
    project_name = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    effective_date = serializers.DateField()
    freelancers_full_name = serializers.CharField(max_length=150)
    freelancer_access = serializers.ListField()
    what_is_the_goal_of_this_project = serializers.CharField(max_length=150)
    deliverables_expected_in_this_scope_of_work = serializers.ListField()
    
    mode_of_communication_between_the_parties = serializers.CharField(max_length=200)
    when_will_the_freelancer_share_his_status_on_deliverables = serializers.DateTimeField()
    when_will_the_progress_meetings_occur = serializers.DateTimeField()

    what_is_the_minimum_time_required_to_complete_this_project = serializers.IntegerField()
    what_is_the_minimum_time_required_to_complete_this_project_unit = serializers.CharField(max_length=30)
    what_is_value_in_respect_to_time_required = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    what_is_value_in_respect_to_time_required_currency = serializers.CharField(max_length=30)
    what_is_the_billing_rate = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    what_is_the_billing_rate_currency = serializers.CharField(max_length=30)
    what_is_the_charges_for_rush_work = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    what_is_the_charges_for_rush_work_currency = serializers.CharField(max_length=30)

    whom_should_the_invoices_be_submitted_to = serializers.CharField(max_length=100)
    whom_should_the_invoices_be_submitted_to_department_name = serializers.CharField(max_length=200, allow_blank=True, required=False, default="")

    when_should_the_invoices_be_submitted = serializers.DateField()
    when_will_the_invoices_be_payable_by_after_receipt = serializers.DateField()
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=200, allow_blank=True, required=False, default="")



    def create(self, validated_data):
        """
        Create and return statement of work.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["effective_date"]\
            = validated_data["effective_date"].isoformat()
        validated_data["when_will_the_freelancer_share_his_status_on_deliverables"]\
            = validated_data["when_will_the_freelancer_share_his_status_on_deliverables"].isoformat()
        validated_data["when_will_the_progress_meetings_occur"]\
            = validated_data["when_will_the_progress_meetings_occur"].isoformat()
        validated_data["when_should_the_invoices_be_submitted"]\
            = validated_data["when_should_the_invoices_be_submitted"].isoformat()
        validated_data["when_will_the_invoices_be_payable_by_after_receipt"]\
            = validated_data["when_will_the_invoices_be_payable_by_after_receipt"].isoformat()

        validated_data["what_is_value_in_respect_to_time_required"] = float(
            validated_data["what_is_value_in_respect_to_time_required"])
        validated_data["what_is_the_billing_rate"] = float(
            validated_data["what_is_the_billing_rate"])
        validated_data["what_is_the_charges_for_rush_work"] = float(
            validated_data["what_is_the_charges_for_rush_work"])

        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return statement of work.
        """
        status_code = 500
        response_json = {}

        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["effective_date"]\
            = validated_data["effective_date"].isoformat()
        validated_data["when_will_the_freelancer_share_his_status_on_deliverables"]\
            = validated_data["when_will_the_freelancer_share_his_status_on_deliverables"].isoformat()
        validated_data["when_will_the_progress_meetings_occur"]\
            = validated_data["when_will_the_progress_meetings_occur"].isoformat()
        validated_data["when_should_the_invoices_be_submitted"]\
            = validated_data["when_should_the_invoices_be_submitted"].isoformat()
        validated_data["when_will_the_invoices_be_payable_by_after_receipt"]\
            = validated_data["when_will_the_invoices_be_payable_by_after_receipt"].isoformat()

        validated_data["what_is_value_in_respect_to_time_required"] = float(
            validated_data["what_is_value_in_respect_to_time_required"])
        validated_data["what_is_the_billing_rate"] = float(
            validated_data["what_is_the_billing_rate"])
        validated_data["what_is_the_charges_for_rush_work"] = float(
            validated_data["what_is_the_charges_for_rush_work"])

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code


class DisclaimerForWebsiteSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        disclaimer for website
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    last_update = serializers.DateField()
    effective_date = serializers.DateField()
    jurisdiction = serializers.CharField(max_length=300)
    company_name = serializers.CharField(max_length=300)
    website_name = serializers.CharField(max_length=150)
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    website_url = serializers.URLField()
    website_contact_email = serializers.EmailField()
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")



    def create(self, validated_data):
        """
        Create and return disclaimer for website.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()
        validated_data['website_or_app_name'] = validated_data['website_name']

        # format date back to iso format
        validated_data["last_update"]\
            = validated_data["last_update"].isoformat()
        validated_data["effective_date"]\
            = validated_data["effective_date"].isoformat()

        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return disclaimer for website.
        """
        status_code = 500
        response_json = {}

        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["last_update"]\
            = validated_data["last_update"].isoformat()
        validated_data["effective_date"]\
            = validated_data["effective_date"].isoformat()

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code


class EmploymentContractSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        employment contract
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    policy_reference = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    website_or_app_name = serializers.CharField(max_length=100,allow_blank=True, required=False, default="")
    company_name = serializers.CharField(max_length=150)
    company_address_line_1 = serializers.CharField(max_length=300)
    company_address_line_2 = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    company_address_line_3 = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    employee_full_name = serializers.CharField(max_length=150)
    type_of_business_the_company_engaged = serializers.CharField(max_length=500)
    start_date = serializers.DateField()
    company_state = serializers.CharField(max_length=150)
    company_country = serializers.CharField(max_length=150)
    duties_of_employee = serializers.CharField(max_length=10000)
    time_frame_of_the_compensation = serializers.CharField(max_length=50)
    amount = serializers.DecimalField(max_digits=18, decimal_places=2, default = 0)
    amount_currency = serializers.CharField(max_length=30)

    full_name_of_company_signatory = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    company_signatory_scanned_copy_detail = serializers.DictField()
    company_signatory_date = serializers.DateField(required=False, allow_null=True)
    full_name_of_employee_signatory = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    employee_signatory_scanned_copy_detail = serializers.DictField()
    employee_signatory_date = serializers.DateField(required=False, allow_null=True)
    
    jurisdiction = serializers.CharField(max_length=150)
    employee_state = serializers.CharField(max_length=150)
    employee_country = serializers.CharField(max_length=150)

    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")


    def create(self, validated_data):
        """
        Create and return employment contract.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["start_date"]\
            = validated_data["start_date"].isoformat()

        validated_data["amount"] = float(
            validated_data["amount"])


        if validated_data["company_signatory_date"] is not None:
            validated_data["company_signatory_date"] = validated_data["company_signatory_date"].isoformat()           

        if validated_data["employee_signatory_date"] is not None:
            validated_data["employee_signatory_date"] = validated_data["employee_signatory_date"].isoformat()


        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return employment contract.
        """
        status_code = 500
        response_json = {}


        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["start_date"]\
            = validated_data["start_date"].isoformat()

        validated_data["amount"] = float(
            validated_data["amount"])

        if validated_data["company_signatory_date"] is not None:
            validated_data["company_signatory_date"] = validated_data["company_signatory_date"].isoformat()           

        if validated_data["employee_signatory_date"] is not None:
            validated_data["employee_signatory_date"] = validated_data["employee_signatory_date"].isoformat()

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code


class TermsAndConditionSerializer(serializers.Serializer):
    """ Validate attribute, create and update
        terms and conditions
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    last_update = serializers.DateField()
    country_name = serializers.CharField(max_length=150)
    company_name = serializers.CharField(max_length=150)
    website_or_app_name = serializers.CharField(max_length=150)
    website_url = serializers.URLField()
    support_email = serializers.EmailField()
    organization_id = serializers.CharField(max_length=250)
    jurisdiction = serializers.CharField(max_length=150, allow_blank=True, required=False, default="")
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")


    def create(self, validated_data):
        """
        Create and return terms and conditions.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["last_update"]\
            = validated_data["last_update"].isoformat()

        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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

    def update(self, old_policy, validated_data):
        """
        Update and return terms and conditions.
        """
        status_code = 500
        response_json = {}


        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["last_update"]\
            = validated_data["last_update"].isoformat()

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code


class GDPRPrivacyPolicySerializer(serializers.Serializer):
    """ Validate attribute, create and update
        GDPR Privacy Policy
    """

    agreement_compliance_type = serializers.CharField(max_length=200)
    location = serializers.CharField(max_length=300)
    jurisdictional_laws = serializers.CharField(max_length=300)
    privacy_policy_will_be_used_for = serializers.CharField(max_length=300)
    would_you_like_to_create_a_premium_privacy_policy  = serializers.CharField(max_length=300)
    do_you_operate_your_app_under_a_company_name = serializers.CharField(max_length=300)
    company_name = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    does_your_company_have_a_short_or_trade_name = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    short_or_trade_name_of_your_company = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    can_users_sign_up_and_create_account_in_your_app = serializers.CharField(max_length=300)
    can_users_sign_up_using_social_media_and_other_third_party_service = serializers.CharField(max_length=300)
    can_users_view_and_change_their_personal_information = serializers.CharField(max_length=300)
    can_users_delete_their_account_and_personal_information = serializers.CharField(max_length=300)
    how_can_users_delete_their_account_and_personal_information = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    can_users_publish_anything_in_your_app = serializers.CharField(max_length=300)

    can_users_share_content_available_in_your_app = serializers.CharField(max_length=300)
    can_users_interact_with_each_other_in_your_app = serializers.CharField(max_length=300)
    when_users_interact_can_they_see_other_users_personally_identifiable_information = serializers.CharField(max_length=300)
    does_your_target_audience_include_resident_of_california_usa = serializers.CharField(max_length=300)
    does_your_target_audience_include_resident_of_european_union = serializers.CharField(max_length=300)
    does_your_target_audience_include_those_under_the_age_of_18 = serializers.CharField(max_length=300)
    does_your_target_audience_include_those_under_the_age_of_13 = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    do_you_collect_any_information_from_children = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    will_information_submitted_by_children_be_publicly_available = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    is_there_an_option_to_keep_submitted_information_private = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    items_apply_to_children_using_the_app = serializers.ListField(default=[])
    do_you_currently_sell_or_plan_on_selling_products_or_services_in_your_app = serializers.CharField(max_length=300)
    do_you_offer_products_or_services_provided_by_third_party_companies = serializers.CharField(max_length=300)
    do_you_have_security_measures_in_place_to_protect_sensitive_payment_information = serializers.CharField(max_length=300)
    do_you_store_any_sensitive_payment_information = serializers.CharField(max_length=300)
    do_you_perform_credit_checks_on_your_customers_members_of_their_household = serializers.CharField(max_length=300)
    do_you_use_third_party_analytics_or_tracking_tools = serializers.CharField(max_length=300)


    do_you_anonymize_users_personal_information = serializers.CharField(max_length=300)
    do_you_have_affiliate_links_in_your_app = serializers.CharField(max_length=300)
    do_you_display_ads_in_your_app = serializers.CharField(max_length=300)
    do_you_collect_users_data_for_remarketing = serializers.CharField(max_length=300)
    do_you_send_email_newsletters_to_users = serializers.CharField(max_length=300)
    do_you_send_push_notifications_to_your_users = serializers.CharField(max_length=300)
    do_you_use_third_party_provider_to_send_push_notification = serializers.CharField(max_length=300)
    what_kind_of_information_do_you_collect_from_your_users = serializers.ListField(default=[])
    will_you_be_requesting_access_to_the_geolocation_of_your_users = serializers.CharField(max_length=300)
    will_you_be_requesting_access_to_various_features_on_yours_users_device = serializers.CharField(max_length=300)
    do_you_collect_any_derivative_data_from_your_users = serializers.CharField(max_length=300)

    do_you_collect_users_personal_information_from_third_party_source = serializers.CharField(max_length=300)
    what_will_you_do_with_the_information_you_collect = serializers.ListField(default=[])
    do_you_combine_different_bits_of_personal_information = serializers.CharField(max_length=300)
    will_you_disclose_personal_information_to_business_affiliates = serializers.CharField(max_length=300)
    will_you_disclose_personal_information_to_third_parties = serializers.CharField(max_length=300)
    what_are_the_categories_of_third_parties_you_may_disclose_personal_information_to = serializers.ListField(default=[])
    will_the_information_disclosed_to_third_parties_contain_any_personally_identifiable_details = serializers.CharField(max_length=300)
    will_you_disclose_personal_information_in_the_event_of_a_business_sale_or_merger = serializers.CharField(max_length=300)
    will_you_disclose_personal_information_to_law_enforcement_agencies_upon_lawful_requests = serializers.CharField(max_length=300)

    how_long_will_you_store_your_users_personal_information = serializers.CharField(max_length=300)
    what_is_the_maximum_time_you_will_store_users_personal_information = serializers.IntegerField(default=0)
    is_the_person_or_company_responsible_for_the_protection_of_personal_information = serializers.CharField(max_length=300)
    
    what_is_your_dpos_name = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    how_can_users_contact_your_dpo = serializers.ListField(default=[])
    what_is_your_dpos_email_address = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")

    do_you_have_security_measures_in_place_to_project_personal_information = serializers.CharField(max_length=300)
    what_kind_of_responsive_action_will_you_take_if_you_have_a_data_breach = serializers.ListField(default=[])
   
    how_can_users_contact_you_regarding_this_policy = serializers.ListField(default=[])
    what_is_the_url_of_your_contact_form = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    what_is_your_email_address = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")
    what_is_your_business_address = serializers.CharField(max_length=300, allow_blank=True, required=False, default="")

    how_will_you_notify_users_of_the_updates_to_this_policy = serializers.ListField(default=[])
    last_update = serializers.DateField()
    website_or_app_name = serializers.CharField(max_length=300)
    website_or_app_url = serializers.URLField()
    website_or_app_contact_page_url = serializers.URLField()
    website_or_app_contact_email = serializers.EmailField()
    organization_id = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)
    pdf_document_name = serializers.CharField(max_length=500, allow_blank=True, required=False, default="")


    




    def create(self, validated_data):
        """
        Create and return GDPR Privacy Policy.
        """

        validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()

        # format date back to iso format
        validated_data["last_update"]\
            = validated_data["last_update"].isoformat()

        # Create software agreement on remote server
        response_json = save_document(
            collection = SOFTWARE_AGREEMENT_COLLECTION,
            document = SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key = SOFTWARE_AGREEMENT_KEY,
            value = validated_data,
            event_id = validated_data['event_id']
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


    def update(self, old_policy, validated_data):
        """
        Update and return GDPR Privacy Policy.
        """
        status_code = 500
        response_json = {}


        old_data = old_policy['agreement']
        if "policy_created_datetime" in old_data:
            validated_data['policy_created_datetime'] = old_data["policy_created_datetime"]
        else:
            validated_data['policy_created_datetime'] = datetime.utcnow().isoformat()
        validated_data['policy_updated_datetime'] = datetime.utcnow().isoformat()


        # format date back to iso format
        validated_data["last_update"]\
            = validated_data["last_update"].isoformat()

        # Update software agreement on remote server
        response_json = update_document(
            collection=SOFTWARE_AGREEMENT_COLLECTION,
            document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            key=SOFTWARE_AGREEMENT_KEY,
            new_value=validated_data,
            event_id=old_policy["eventId"]
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve software agreement on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": old_policy["eventId"]}
            )

        return response_json, status_code

