import os
from django.http import JsonResponse
from django.shortcuts import  HttpResponse
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from DowellLicenseProject.settings import BASE_DIR
from django.conf import settings
import pathlib
from django.http import FileResponse
from django.views.decorators.clickjacking import xframe_options_exempt
import json

from utils.dowell import (
    fetch_document,
    get_event_id,
    SOFTWARE_AGREEMENT_COLLECTION,
    SOFTWARE_AGREEMENT_DOCUMENT_NAME,
    RECORD_PER_PAGE,
    BASE_DOC_URL,
    BASE_URL
)
from utils.general import read_template, get_compliance_template_name
from agreements.serializers import (
    SoftwareLicensePolicySerializer,
    EulaSerializer,
    MOUSerializer,
    WebsiteTermsOfUseSerializer,
    WebsitePrivacyPolicySerializer,
    WebsiteSecurityPolicySerializer,
    NonCompeteAgreementSerializer,
    CookiesPolicySerializer,
    ReturnAndRefundSerializer,
    AppDisclaimerSerializer,
    AppPrivacyPolicySerializer,
    NDASerializer,
    StatementOfWorkSerializer,
    DisclaimerForWebsiteSerializer,
    EmploymentContractSerializer,
    TermsAndConditionSerializer,
    GDPRPrivacyPolicySerializer
    
    )


MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
    "January"
]


def index(request):
    return JsonResponse({
        "message": "Welcome to legalzard"
    })

# @method_decorator(csrf_exempt, name='dispatch')
class health_check(APIView):
    def get(self, request ):
        return Response("Sever is running fine. Stop Doubting server!",status=status.HTTP_200_OK)
class AgreementComplianceList(APIView):
    """ List all and create software agreements policy
    """

    def get(self, request, format=None):
        try:

            limit = int(request.GET.get("limit", "10"))
            offset = int(request.GET.get("offset", "0"))
            action_type = request.GET.get("action_type", "")
            organization_id = request.GET.get("organization_id", "")


            # Retrieve agreement on remote server
            if action_type == "agreement-compliance-generated-by-orgainization":
                response_json = fetch_document(
                    collection=SOFTWARE_AGREEMENT_COLLECTION,
                    document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                    fields={"agreement.organization_id": organization_id}
                )

                response_json = AgreementComplianceList.sort_and_categorize_agreement_compliance(request, response_json)



            else:

                response_json = fetch_document(
                    collection=SOFTWARE_AGREEMENT_COLLECTION,
                    document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                    fields={}
                )
                response_json = AgreementComplianceList.add_document_url(request, response_json)


            return Response(response_json,
                            status=status.HTTP_200_OK
                            )

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return Response({
                "error_msg": f"{e}"
            },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def post(self, request: Request, format=None):
        try:
            request_data = request.data
            response_json = {}
            status_code = 500

            
            request_data['event_id'] = get_event_id()
            request_data['pdf_document_name'] = "nil"

            if request_data['agreement_compliance_type'] == "software-license-policy":
                response_json, status_code = self.create_software_license_policy(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "eula":
                response_json, status_code = self.create_eula(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "mou":
                response_json, status_code = self.create_mou(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "website-terms-of-use":
                response_json, status_code = self.create_website_terms_of_use(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "website-privacy-policy":
                response_json, status_code = self.create_website_privacy_policy(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "website-security-policy":
                response_json, status_code = self.create_website_security_policy(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "non-compete-agreement":
                response_json, status_code = self.create_non_compete_agreement(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "cookie-policy":
                response_json, status_code = self.create_cookie_policy(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "return-and-refund":
                response_json, status_code = self.create_return_and_fund(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "app-disclaimer":
                response_json, status_code = self.create_app_disclaimer(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "app-privacy-policy":
                response_json, status_code = self.create_app_privacy_policy(
                    request_data,
                    response_json,
                    status_code)
            
            elif request_data['agreement_compliance_type'] == "nda":
                response_json, status_code = self.create_nda(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "discliamer-for-website":

                if "effective_date" not in request_data:
                    request_data["effective_date"] = request_data['last_update']
                if "jurisdiction" not in request_data:
                    request_data["jurisdiction"] = " "
                if "company_name" not in request_data:
                    request_data["company_name"] = " "
                    
                response_json, status_code = self.create_discliamer_for_website(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "statement-of-work":
                response_json, status_code = self.create_statement_of_work(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "employment-contract":
                response_json, status_code = self.create_employment_contract(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "terms-and-conditions":
                response_json, status_code = self.create_terms_and_conditions(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "gdpr-privacy-policy":
                response_json, status_code = self.create_gdpr_privacy_policy(
                    request_data,
                    response_json,
                    status_code)

            response_json = AgreementComplianceList.add_document_url(request, response_json)
            return Response(response_json, status=status_code)

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            response_json = {
                "isSuccess": False,
                "message": str(e),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def create_software_license_policy(self, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])

        request_data["contract_effective_date"] = date.fromisoformat(
            request_data["contract_effective_date"])

        request_data["contract_termination_date"] = date.fromisoformat(
            request_data["contract_termination_date"])

        request_data["invoicing_date"] = date.fromisoformat(
            request_data["invoicing_date"])

        request_data["effective_date_for_invoice_payment"] = date.fromisoformat(
            request_data["effective_date_for_invoice_payment"])

        request_data["relevant_termination_period_date"] = date.fromisoformat(
            request_data["relevant_termination_period_date"])

        request_data["party_1_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_1_date_of_signing_contract"])

        request_data["date_contract_was_sign_on_behalf_of_party_1"] = date.fromisoformat(
            request_data["date_contract_was_sign_on_behalf_of_party_1"])

        request_data["party_2_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_2_date_of_signing_contract"])

        request_data["date_contract_was_sign_on_behalf_of_party_2"] = date.fromisoformat(
            request_data["date_contract_was_sign_on_behalf_of_party_2"])


        # Create serializer object
        serializer = SoftwareLicensePolicySerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            print(request_data)
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code


    def create_eula(self, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])

        request_data["date_of_commencement"] = date.fromisoformat(
            request_data["date_of_commencement"])


        # Create serializer object
        serializer = EulaSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code


    def create_mou(self, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])

        request_data["date_of_commencement"] = date.fromisoformat(
            request_data["date_of_commencement"])

        request_data["date_of_termination"] = date.fromisoformat(
            request_data["date_of_termination"])

        request_data["date_for_legally_binding_definitive_agreement"] = date.fromisoformat(
            request_data["date_for_legally_binding_definitive_agreement"])



        # Create serializer object
        serializer = MOUSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code


    def create_website_terms_of_use(self, request_data, response_json, status_code):

        from datetime import date

        request_data["terms_last_updated"] = date.fromisoformat(
            request_data["terms_last_updated"])


        # Create serializer object
        serializer = WebsiteTermsOfUseSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_website_privacy_policy(self, request_data, response_json, status_code):

        from datetime import date

        request_data["last_updated"] = date.fromisoformat(
            request_data["last_updated"])


        # Create serializer object
        serializer = WebsitePrivacyPolicySerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_website_security_policy(self, request_data, response_json, status_code):

        from datetime import date

        request_data["last_updated"] = date.fromisoformat(
            request_data["last_updated"])


        # Create serializer object
        serializer = WebsiteSecurityPolicySerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code


    def create_non_compete_agreement(self, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])
        request_data["date_of_termination"] = date.fromisoformat(
            request_data["date_of_termination"])


        # Create serializer object
        serializer = NonCompeteAgreementSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_cookie_policy(self, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])


        # Create serializer object
        serializer = CookiesPolicySerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_return_and_fund(self, request_data, response_json, status_code):

        from datetime import date

        request_data["date"] = date.fromisoformat(
            request_data["date"])


        # Create serializer object
        serializer = ReturnAndRefundSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_app_disclaimer(self, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])


        # Create serializer object
        serializer = AppDisclaimerSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_app_privacy_policy(self, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])


        # Create serializer object
        serializer = AppPrivacyPolicySerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_nda(self, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])
        request_data["what_will_be_the_date_for_termination_of_this_nda"] = date.fromisoformat(
            request_data["what_will_be_the_date_for_termination_of_this_nda"])

        # Create serializer object
        serializer = NDASerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_statement_of_work(self, request_data, response_json, status_code):

        from datetime import date, datetime

        request_data["effective_date"] = date.fromisoformat(
            request_data["effective_date"])

        request_data["when_should_the_invoices_be_submitted"] = date.fromisoformat(
            request_data["when_should_the_invoices_be_submitted"])

        request_data["when_will_the_invoices_be_payable_by_after_receipt"] = date.fromisoformat(
            request_data["when_will_the_invoices_be_payable_by_after_receipt"])

        request_data["when_will_the_freelancer_share_his_status_on_deliverables"] = datetime.fromisoformat(
            request_data["when_will_the_freelancer_share_his_status_on_deliverables"])

        request_data["when_will_the_progress_meetings_occur"] = datetime.fromisoformat(
            request_data["when_will_the_progress_meetings_occur"])


        # Create serializer object
        serializer = StatementOfWorkSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_discliamer_for_website(self, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])
        request_data["effective_date"] = date.fromisoformat(
            request_data["effective_date"])

        # Create serializer object
        serializer = DisclaimerForWebsiteSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_employment_contract(self, request_data, response_json, status_code):

        from datetime import date

        request_data["start_date"] = date.fromisoformat(
            request_data["start_date"])

        if request_data["company_signatory_date"] is not None:
            request_data["company_signatory_date"] = date.fromisoformat(
                request_data["company_signatory_date"])           

        if request_data["employee_signatory_date"] is not None:
            request_data["employee_signatory_date"] = date.fromisoformat(
                request_data["employee_signatory_date"])


        # Create serializer object
        serializer = EmploymentContractSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                # "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(str(response_json), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

        # return result
        return response_json, status_code

    def create_terms_and_conditions(self, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])

        # Create serializer object
        serializer = TermsAndConditionSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_gdpr_privacy_policy(self, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])

        # Create serializer object
        serializer = GDPRPrivacyPolicySerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }

            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code




    @staticmethod
    def add_document_url(request, response_data):
        data_list = response_data['data']
        new_data_list = []

        for data in data_list:
            agreement = data['agreement']
            # this code only execute
            # if the agreement object
            # does not have logo_detail field

            try:

                agreement['html_doc_url'] = request.build_absolute_uri(
                    reverse('load_public_agreement_compliance', kwargs={'event_id': data["eventId"]}))
                
            except Exception as err:
                print(str(err))


            # add agreement to new data list
            data['agreement'] = agreement
            new_data_list.append(data)

        if new_data_list:
            response_data['data'] = new_data_list

        return response_data


    @staticmethod
    def add_single_document_url(request, data):


        agreement = data['agreement']
        # this code only execute
        # if the agreement object
        # does not have logo_detail field


        try:

            agreement['html_doc_url'] = request.build_absolute_uri(
                reverse('load_public_agreement_compliance', kwargs={'event_id': data["eventId"]}))
            
        except Exception as err:
            print(str(err))


        # add agreement to new data list
        data['agreement'] = agreement

        return data



    @staticmethod
    def generate_pdf_document(context:dict, event_id):
        import time
        import datetime
        from utils.generate_pdf import generate

        try:
            ts = time.time()
            
            context['event_id'] = event_id

            # load commpliance template from the filesystem
            content = read_template(get_compliance_template_name(context['agreement_compliance_type']))


            # html temporary file
            file_name = f'AGREEMENTS{event_id.replace("-", "").upper()}_{ts}'.replace(".", "")
            html_tmp_path = os.path.join('/tmp/', f'{file_name}.html')

            # create html tmp file
            with open(html_tmp_path, "w") as html_tmp_file:

                content = content.substitute(**context, eventId="", base_url="")
                html_tmp_file.write(content)

                #PERMIT READ FILE
                try:
                    os.chmod(html_tmp_path, 0o777)
                except Exception as e:
                    print(str(e))
                # END PERMIT READ FILE

            # Generate PDF
            generate(
                html_file_abs_path_or_url=html_tmp_path, 
                pdf_file_name=file_name)

            context['pdf_document_name'] = f'{file_name}.pdf'

            return context
        except Exception as err:
            print(str(err))
            return context



    @staticmethod
    def sort_and_categorize_agreement_compliance(request, response_data):
        data_list = response_data['data']
        data_list_sorted = sorted(data_list, key=lambda x: x["agreement"]["agreement_compliance_type"])

        data_category = {}

        # Categorize sorted data
        for data in data_list_sorted:

            agreement = data["agreement"]

            # Add agreement compliance type as key to data_category
            if agreement["agreement_compliance_type"] not in data_category:
                data_category[agreement["agreement_compliance_type"]] = []


            data = AgreementComplianceList.add_single_document_url(request, data)
            data_category[agreement["agreement_compliance_type"]].append(data)

        


        # Update data
        response_data["data"] = data_category

        return response_data







class AgreementComplianceDetail(APIView):
    """
     Retrieve , update and delete software license
    """

    def get(self, request, event_id, format=None):
        try:

            # Retrieve license on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )

            AgreementComplianceList.add_document_url(request, response_json)
            return Response(response_json, status=status.HTTP_200_OK)

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return Response({
                "error_msg": f"{e}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, event_id, format=None):
        try:
            from datetime import date
            request_data = request.data
            response_json = {}
            status_code = 500



           # Retrieve old record
            old_policy_response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )


            request_data['event_id'] = event_id
            request_data['pdf_document_name'] = " "


            if request_data['agreement_compliance_type'] == "software-license-policy":
                response_json, status_code = self.update_software_license_policy(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "eula":
                response_json, status_code = self.update_eula(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "mou":
                response_json, status_code = self.update_mou(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)


            elif request_data['agreement_compliance_type'] == "website-terms-of-use":
                response_json, status_code = self.update_website_terms_of_use(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "website-privacy-policy":
                response_json, status_code = self.update_website_privacy_policy(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "website-security-policy":
                response_json, status_code = self.update_website_security_policy(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "non-compete-agreement":
                response_json, status_code = self.update_non_compete_agreement(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "cookie-policy":
                response_json, status_code = self.update_cookie_policy(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "return-and-refund":
                response_json, status_code = self.update_return_and_fund(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "app-disclaimer":
                response_json, status_code = self.update_app_disclaimer(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "app-privacy-policy":
                response_json, status_code = self.update_app_privacy_policy(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "nda":
                response_json, status_code = self.update_nda(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "discliamer-for-website":

                if "effective_date" not in request_data:
                    request_data["effective_date"] = request_data['last_update']
                if "jurisdiction" not in request_data:
                    request_data["jurisdiction"] = " "
                if "company_name" not in request_data:
                    request_data["company_name"] = " "


                response_json, status_code = self.update_discliamer_for_website(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "statement-of-work":
                response_json, status_code = self.update_statement_of_work(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "employment-contract":
                response_json, status_code = self.update_employment_contract(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "terms-and-conditions":
                response_json, status_code = self.update_terms_and_conditions(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "gdpr-privacy-policy":
                response_json, status_code = self.update_gdpr_privacy_policy(
                    old_policy= old_policy_response_json["data"][0],
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)


            response_json = AgreementComplianceList.add_document_url(request, response_json)
            return Response(response_json, status=status_code)


        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            response_json = {
                "isSuccess": False,
                "message": str(e),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update_software_license_policy(self, old_policy, request_data, response_json, status_code):

        from datetime import date
        

        # Convert date string (yyyy-mm-dd)
        # to date object
        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])

        request_data["contract_effective_date"] = date.fromisoformat(
            request_data["contract_effective_date"])

        request_data["contract_termination_date"] = date.fromisoformat(
            request_data["contract_termination_date"])

        request_data["invoicing_date"] = date.fromisoformat(
            request_data["invoicing_date"])

        request_data["effective_date_for_invoice_payment"] = date.fromisoformat(
            request_data["effective_date_for_invoice_payment"])

        request_data["relevant_termination_period_date"] = date.fromisoformat(
            request_data["relevant_termination_period_date"])

        request_data["party_1_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_1_date_of_signing_contract"])

        request_data["date_contract_was_sign_on_behalf_of_party_1"] = date.fromisoformat(
            request_data["date_contract_was_sign_on_behalf_of_party_1"])

        request_data["party_2_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_2_date_of_signing_contract"])

        request_data["date_contract_was_sign_on_behalf_of_party_2"] = date.fromisoformat(
            request_data["date_contract_was_sign_on_behalf_of_party_2"])



        # Update and Commit data into database
        serializer = SoftwareLicensePolicySerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code



    def update_eula(self, old_policy, request_data, response_json, status_code):
        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])

        request_data["date_of_commencement"] = date.fromisoformat(
            request_data["date_of_commencement"])


        # Update and Commit data into database
        serializer = EulaSerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code


    def update_mou(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])

        request_data["date_of_commencement"] = date.fromisoformat(
            request_data["date_of_commencement"])

        request_data["date_of_termination"] = date.fromisoformat(
            request_data["date_of_termination"])

        request_data["date_for_legally_binding_definitive_agreement"] = date.fromisoformat(
            request_data["date_for_legally_binding_definitive_agreement"])


        # Update and Commit data into database
        serializer = MOUSerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_website_terms_of_use(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["terms_last_updated"] = date.fromisoformat(
            request_data["terms_last_updated"])


        # Update and Commit data into database
        serializer = WebsiteTermsOfUseSerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_website_privacy_policy(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["last_updated"] = date.fromisoformat(
            request_data["last_updated"])


        # Update and Commit data into database
        serializer = WebsitePrivacyPolicySerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_website_security_policy(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["last_updated"] = date.fromisoformat(
            request_data["last_updated"])


        # Update and Commit data into database
        serializer = WebsiteSecurityPolicySerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_non_compete_agreement(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])
        request_data["date_of_termination"] = date.fromisoformat(
            request_data["date_of_termination"])


        # Update and Commit data into database
        serializer = NonCompeteAgreementSerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_cookie_policy(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])


        # Update and Commit data into database
        serializer = CookiesPolicySerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_return_and_fund(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["date"] = date.fromisoformat(
            request_data["date"])


        # Update and Commit data into database
        serializer = ReturnAndRefundSerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_app_disclaimer(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])


        # Update and Commit data into database
        serializer = AppDisclaimerSerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_app_privacy_policy(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])


        # Update and Commit data into database
        serializer = AppPrivacyPolicySerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_nda(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])
        request_data["what_will_be_the_date_for_termination_of_this_nda"] = date.fromisoformat(
            request_data["what_will_be_the_date_for_termination_of_this_nda"])

        # Update and Commit data into database
        serializer = NDASerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code


    def update_statement_of_work(self, old_policy, request_data, response_json, status_code):

        from datetime import date, datetime

        request_data["effective_date"] = date.fromisoformat(
            request_data["effective_date"])

        request_data["when_should_the_invoices_be_submitted"] = date.fromisoformat(
            request_data["when_should_the_invoices_be_submitted"])

        request_data["when_will_the_invoices_be_payable_by_after_receipt"] = date.fromisoformat(
            request_data["when_will_the_invoices_be_payable_by_after_receipt"])

        request_data["when_will_the_freelancer_share_his_status_on_deliverables"] = datetime.fromisoformat(
            request_data["when_will_the_freelancer_share_his_status_on_deliverables"])

        request_data["when_will_the_progress_meetings_occur"] = datetime.fromisoformat(
            request_data["when_will_the_progress_meetings_occur"])


        # Update and Commit data into database
        serializer = StatementOfWorkSerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code


    def update_discliamer_for_website(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])
        request_data["effective_date"] = date.fromisoformat(
            request_data["effective_date"])

        # Update and Commit data into database
        serializer = DisclaimerForWebsiteSerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code


    def update_employment_contract(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["start_date"] = date.fromisoformat(
            request_data["start_date"])

        if request_data["company_signatory_date"] is not None:
            request_data["company_signatory_date"] = date.fromisoformat(
                request_data["company_signatory_date"])           

        if request_data["employee_signatory_date"] is not None:
            request_data["employee_signatory_date"] = date.fromisoformat(
                request_data["employee_signatory_date"])

        # Update and Commit data into database
        serializer = EmploymentContractSerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_terms_and_conditions(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])

        # Update and Commit data into database
        serializer = TermsAndConditionSerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_gdpr_privacy_policy(self, old_policy, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])

        # Update and Commit data into database
        serializer = GDPRPrivacyPolicySerializer(
            old_policy, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                old_policy, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": json.dumps(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code





@xframe_options_exempt
def load_public_agreement_compliance(request, event_id:str):
    try:

        format = request.GET.get("format", "html")
        base_url = "http://127.0.0.1:8000/" if settings.DEBUG else BASE_URL

        # retrieve compliance related data from
        # database
        response_data = fetch_document(
            SOFTWARE_AGREEMENT_COLLECTION,
            SOFTWARE_AGREEMENT_DOCUMENT_NAME,
            fields={"eventId": event_id}
            )
        
        data = response_data['data'][0]
        agreement = data['agreement']
        

        # load commpliance template from the filesystem
        content = read_template(get_compliance_template_name(agreement['agreement_compliance_type']))
        
        # replace placeholders in the template with actual values
        agreement = format_content(agreement)

        content = content.substitute(**agreement, base_url=base_url, eventId=data["eventId"])

        # return html context
        if format == "html":
            return HttpResponse(content= content)


        # return json data
        from django.http import JsonResponse
        return JsonResponse({
            "event_id": event_id,
            "content": content
        })


    except Exception as err:
        print(str(err))
        return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Convert money
format_money = lambda value: '{:20,.2f}'.format(float(value))

def check_and_format_money(data:dict):
    
    if "liability_limit_amount" in data:
        data['liability_limit_amount'] = format_money(float(data['liability_limit_amount']))

    if "liability_must_not_exceed_amount" in data:
        data['liability_must_not_exceed_amount'] = format_money(float(data['liability_must_not_exceed_amount']))

    if "reimbursement_of_cancellation_money" in data:
        data['reimbursement_of_cancellation_money'] = format_money(float(data['reimbursement_of_cancellation_money']))

    if "amount" in data:
        data['amount'] = format_money(float(data['amount']))

    if "amount" in data:
        data['amount'] = format_money(float(data['amount']))

    if "what_is_value_in_respect_to_time_required" in data:
        data['what_is_value_in_respect_to_time_required'] = format_money(float(data['what_is_value_in_respect_to_time_required']))
    
    if "what_is_the_billing_rate" in data:
        data['what_is_the_billing_rate'] = format_money(float(data['what_is_the_billing_rate']))



    return data





def split_date_and_format_data(data):
    from datetime import date, datetime
    form_datetime = ""

    if "date" in data:
        date_c = date.fromisoformat(data["date"])
        form_datetime = date_c.strftime("%d/%m/%Y")
        data["date"] = form_datetime


    # Statement of work
    if "when_will_the_freelancer_share_his_status_on_deliverables" in data:
        date_c = datetime.fromisoformat(data["when_will_the_freelancer_share_his_status_on_deliverables"])
        form_datetime = date_c.strftime("%d/%m/%Y %H:%M:%S %p")
        data["when_will_the_freelancer_share_his_status_on_deliverables"] = form_datetime

    if "when_will_the_progress_meetings_occur" in data:
        date_c = datetime.fromisoformat(data["when_will_the_progress_meetings_occur"])
        form_datetime = date_c.strftime("%d/%m/%Y %H:%M:%S %p")
        data["when_will_the_progress_meetings_occur"] = form_datetime

    if "whom_should_the_invoices_be_submitted_to" in data:
        if not data['whom_should_the_invoices_be_submitted_to']:
            data['whom_should_the_invoices_be_submitted_to'] = data['whom_should_the_invoices_be_submitted_to_department_name']

    if "when_should_the_invoices_be_submitted" in data:
        date_c = date.fromisoformat(data["when_should_the_invoices_be_submitted"])
        form_datetime = date_c.strftime("%B, ")
        text = "(st)" if date_c.day == 1 else "(nd)" if date_c.day == 2 else "(rd)" if date_c.day == 3 else "(th)"
        form_datetime = f"{date_c.day}{text}, {MONTHS[date_c.month - 1]}"
        data["when_should_the_invoices_be_submitted"] = form_datetime

    if "when_will_the_invoices_be_payable_by_after_receipt" in data:
        date_c = date.fromisoformat(data["when_will_the_invoices_be_payable_by_after_receipt"])
        form_datetime = date_c.strftime("%d/%m/%Y")
        data["when_will_the_invoices_be_payable_by_after_receipt"] = form_datetime

    if "effective_date" in data:
        date_c = date.fromisoformat(data["effective_date"])
        form_datetime = date_c.strftime("%d/%m/%Y")
        data["effective_date"] = form_datetime

    if "last_update" in data:
        date_c = date.fromisoformat(data["last_update"])
        form_datetime = date_c.strftime("%d/%m/%Y")
        data["last_update"] = form_datetime

    if "last_updated" in data:
        date_c = date.fromisoformat(data["last_updated"])
        form_datetime = date_c.strftime("%d/%m/%Y")
        data["last_updated"] = form_datetime


    if "date_of_commencement" in data:
        date_c = date.fromisoformat(data["date_of_commencement"])
        form_datetime = date_c.strftime("%d/%m/%Y")
        data["date_of_commencement"] = form_datetime

    if "date_of_termination" in data:
        date_c = date.fromisoformat(data["date_of_termination"])
        form_datetime = date_c.strftime("%d/%m/%Y")
        data["date_of_termination"] = form_datetime

    if "date_for_legally_binding_definitive_agreement" in data:
        date_c = date.fromisoformat(data["date_for_legally_binding_definitive_agreement"])
        form_datetime = date_c.strftime("%d/%m/%Y")
        data["date_for_legally_binding_definitive_agreement"] = form_datetime

    if "date_of_execution_of_document" in data:
        date_c = date.fromisoformat(data["date_of_execution_of_document"])
        form_datetime = date_c.strftime("%d/%m/%Y")
        data["date_of_execution_of_document"] = form_datetime

        if data['agreement_compliance_type'] == "non-compete-agreement":
            execution_day = date_c.day
            execution_month = date_c.month
            execution_year = date_c.year
            execution_month_ = MONTHS[execution_month - 1]
            data["execution_day"] = execution_day
            data["execution_month"] = execution_month_
            data["execution_year"] = execution_year



    if "company_signatory_date" in data:
        if data["company_signatory_date"]:
            date_c = date.fromisoformat(data["company_signatory_date"])
            form_datetime = date_c.strftime("%d/%m/%Y")
            data["company_signatory_date"] = form_datetime

    if "employee_signatory_date" in data:
        
        if data["employee_signatory_date"]:
            date_c = date.fromisoformat(data["employee_signatory_date"])
            form_datetime = date_c.strftime("%d/%m/%Y")
        data["employee_signatory_date"] = form_datetime



    return data



def format_content(data):
    data = check_and_format_money(data)
    data = split_date_and_format_data(data)

    ### BEGIN  Statement Of Work
    # freelancer access list
    if "freelancer_access" in data:
        content = ""
        for access in data['freelancer_access']:
            content += f'<li class="c0 li-bullet-0">{access}</li>'
        
        data['freelancer_access'] = content

    # deliverables expected in this scope of work list
    if "deliverables_expected_in_this_scope_of_work" in data:
        content = ""
        for scope in data['deliverables_expected_in_this_scope_of_work']:
            content += f'<li class="c0 li-bullet-0">{scope}</li>'
        
        data['deliverables_expected_in_this_scope_of_work'] = content

    ### END Statement Of Work


    ### BEGIN GDPR privacy policy
    # what_kind_of_information_do_you_collect_from_your_users
    if "what_kind_of_information_do_you_collect_from_your_users" in data:
        content = ""
        for value in data['what_kind_of_information_do_you_collect_from_your_users']:
            content += f'<li class="c0 li-bullet-0">{value}</li>'
        
        data['what_kind_of_information_do_you_collect_from_your_users'] = content

    # what_will_you_do_with_the_information_you_collect
    if "what_will_you_do_with_the_information_you_collect" in data:
        content = ""
        for value in data['what_will_you_do_with_the_information_you_collect']:
            content += f'<li class="c0 li-bullet-0">{value}</li>'
        
        data['what_will_you_do_with_the_information_you_collect'] = content

    # 
    if "what_are_the_categories_of_third_parties_you_may_disclose_personal_information_to" in data:
        content = ""
        for value in data['what_are_the_categories_of_third_parties_you_may_disclose_personal_information_to']:
            content += f'<li class="c0 li-bullet-0">{value}</li>'
        
        data['what_are_the_categories_of_third_parties_you_may_disclose_personal_information_to'] = content

    # 
    if "what_kind_of_responsive_action_will_you_take_if_you_have_a_data_breach" in data:
        content = ""
        for value in data['what_kind_of_responsive_action_will_you_take_if_you_have_a_data_breach']:
            content += f'<li class="c0 li-bullet-0">{value}</li>'
        
        data['what_kind_of_responsive_action_will_you_take_if_you_have_a_data_breach'] = content

    # 
    if "how_can_users_contact_you_regarding_this_policy" in data:
        content = ""
        for value in data['how_can_users_contact_you_regarding_this_policy']:
            content += f'<li class="c0 li-bullet-0"><span class="c2">{value}</span></li>'
        
        data['how_can_users_contact_you_regarding_this_policy'] = content

    # 
    if "how_will_you_notify_users_of_the_updates_to_this_policy" in data:
        content = ""
        for value in data['how_will_you_notify_users_of_the_updates_to_this_policy']:
            content += f'<li class="c0 li-bullet-0">{value}</li>'
        
        data['how_will_you_notify_users_of_the_updates_to_this_policy'] = content

    # 
    if "how_can_users_contact_your_dpo" in data:
        content = ""
        for value in data['how_can_users_contact_your_dpo']:
            content += f'<li class="c0 li-bullet-0">{value}</li>'
        
        data['how_can_users_contact_your_dpo'] = content
    ### END GDPR privacy policy


    if "company_signatory_scanned_copy_detail" in data:
        company_signatory_scanned_copy_detail = data["company_signatory_scanned_copy_detail"]
        company_signatory_scanned_extension = "png"
        company_signatory_scanned_bit64string = ""

        if "file_extension" in company_signatory_scanned_copy_detail:
            company_signatory_scanned_extension = company_signatory_scanned_copy_detail["file_extension"].lower()
        
        if "filename" in company_signatory_scanned_copy_detail:
            company_signatory_scanned_bit64string = company_signatory_scanned_copy_detail["filename"]

        data["company_signatory_scanned_bit64string"] = company_signatory_scanned_bit64string
        data["company_signatory_scanned_extension"] = company_signatory_scanned_extension



    if "employee_signatory_scanned_copy_detail" in data:
        employee_signatory_scanned_copy_detail = data["employee_signatory_scanned_copy_detail"]
        employee_signatory_scanned_extension = "png"
        employee_signatory_scanned_bit64string = ""

        if "file_extension" in employee_signatory_scanned_copy_detail:
            employee_signatory_scanned_extension = employee_signatory_scanned_copy_detail["file_extension"].lower()
        
        if "filename" in employee_signatory_scanned_copy_detail:
            employee_signatory_scanned_bit64string = employee_signatory_scanned_copy_detail["filename"]

        data["employee_signatory_scanned_bit64string"] = employee_signatory_scanned_bit64string
        data["employee_signatory_scanned_extension"] = employee_signatory_scanned_extension


    if "signature_of_witnesse_1_detail" in data:
        signature_of_witnesse_1_detail = data["signature_of_witnesse_1_detail"]
        file_extension = "png"
        filename = ""

        if "file_extension" in signature_of_witnesse_1_detail:
            file_extension = signature_of_witnesse_1_detail["file_extension"].lower()
        
        if "filename" in signature_of_witnesse_1_detail:
            filename = signature_of_witnesse_1_detail["filename"]

        data["signature_of_witnesse_1_detail_file_extension"] = file_extension
        data["signature_of_witnesse_1_detail_filename"] = filename



    if "signature_of_witnesse_2_detail" in data:
        signature_of_witnesse_2_detail = data["signature_of_witnesse_2_detail"]
        file_extension = "png"
        filename = ""

        if "file_extension" in signature_of_witnesse_2_detail:
            file_extension = signature_of_witnesse_2_detail["file_extension"].lower()
        
        if "filename" in signature_of_witnesse_2_detail:
            filename = signature_of_witnesse_2_detail["filename"]

        data["signature_of_witnesse_2_detail_file_extension"] = file_extension
        data["signature_of_witnesse_2_detail_filename"] = filename




    if "party_1_signatory_scanned_copy_detail" in data:
        party_1_signatory_scanned_copy_detail = data["party_1_signatory_scanned_copy_detail"]
        file_extension = "png"
        filename = ""

        if "file_extension" in party_1_signatory_scanned_copy_detail:
            file_extension = party_1_signatory_scanned_copy_detail["file_extension"].lower()
        
        if "filename" in party_1_signatory_scanned_copy_detail:
            filename = party_1_signatory_scanned_copy_detail["filename"]

        data["party_1_signatory_scanned_copy_detail_file_extension"] = file_extension
        data["party_1_signatory_scanned_copy_detail_filename"] = filename


    if "party_2_signatory_scanned_copy_detail" in data:
        party_2_signatory_scanned_copy_detail = data["party_2_signatory_scanned_copy_detail"]
        file_extension = "png"
        filename = ""

        if "file_extension" in party_2_signatory_scanned_copy_detail:
            file_extension = party_2_signatory_scanned_copy_detail["file_extension"].lower()
        
        if "filename" in party_2_signatory_scanned_copy_detail:
            filename = party_2_signatory_scanned_copy_detail["filename"]

        data["party_2_signatory_scanned_copy_detail_file_extension"] = file_extension
        data["party_2_signatory_scanned_copy_detail_filename"] = filename

    return data





def download_file(request):
    try:

        file_name = request.GET.get('fn','')
        file_path = os.path.join(settings.MEDIA_ROOT, f'documents/{file_name}')
        file_path=file_path.replace("\\","/")
        file_server = pathlib.Path(file_path)

        if not file_server.exists():
            print('file not found.')
        else:
            file_to_download = open(str(file_server), 'rb')
            response = FileResponse(file_to_download, content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename="'+file_name+'"'
            return response


    except Exception as e:
        return HttpResponse(f"{e}")
