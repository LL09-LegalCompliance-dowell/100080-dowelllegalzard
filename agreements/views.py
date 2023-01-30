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

from utils.dowell import (
    fetch_document,
    get_event_id,
    SOFTWARE_AGREEMENT_COLLECTION,
    SOFTWARE_AGREEMENT_DOCUMENT_NAME,
    RECORD_PER_PAGE,
    BASE_DOC_URL
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
    DisclaimerForWebsiteSerializer
    
    )


def index(request):
    return JsonResponse({
        "message": "Welcome to legalzard"
    })

class AgreementComplianceList(APIView):
    """ List all and create software agreements policy
    """

    def get(self, request, format=None):
        try:

            limit = int(request.GET.get("limit", "10"))
            offset = int(request.GET.get("offset", "0"))

            # Retrieve agreement on remote server
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

            # Generate PDF document
            request_data = AgreementComplianceList.generate_pdf_document(
                request_data,
                event_id = get_event_id()
                )

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
                response_json, status_code = self.create_discliamer_for_website(
                    request_data,
                    response_json,
                    status_code)

            elif request_data['agreement_compliance_type'] == "statement-of-work":
                response_json, status_code = self.create_statement_of_work(
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
                "message": str(serializer.errors),
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
                "message": str(serializer.errors),
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

        request_data["date_for_legally_binding_definitive_agreement_2"] = date.fromisoformat(
            request_data["date_for_legally_binding_definitive_agreement_2"])


        # Create serializer object
        serializer = MOUSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
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
                "message": str(serializer.errors),
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
                "message": str(serializer.errors),
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
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
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
                "message": str(serializer.errors),
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
                "message": str(serializer.errors),
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
                "message": str(serializer.errors),
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
                "message": str(serializer.errors),
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
                "message": str(serializer.errors),
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
                "message": str(serializer.errors),
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
                "message": str(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code

    def create_discliamer_for_website(self, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])

        # Create serializer object
        serializer = DisclaimerForWebsiteSerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            print(serializer.errors)
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response_json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return result
        return response_json, status_code





    @staticmethod
    def add_document_url(request, response_data):
        data_list = response_data['data']
        new_data_list = []
        # preview_doc_url
        # download_doc_url

        for data in data_list:
            agreement = data['agreement']
            # this code only execute
            # if the agreement object
            # does not have logo_detail field
            if "pdf_document_name" not in agreement:
                new_data_list.append(data)
                continue

            agreement['preview_doc_url'] = f'{BASE_DOC_URL}{agreement["pdf_document_name"]}'

            agreement['html_doc_url'] = request.build_absolute_uri(
                reverse('load_public_agreement_compliance', kwargs={'event_id': data["eventId"]}))

            agreement['download_doc_url'] = request.build_absolute_uri(
                f'/download/?fn={agreement["pdf_document_name"]}')

            # add agreement to new data list
            data['agreement'] = agreement
            new_data_list.append(data)

        if new_data_list:
            response_data['data'] = new_data_list

        return response_data


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

                content = content.substitute(**context)
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
    def generate_pdf_document_(context:dict):
        import time
        from utils.generate_pdf import generate

        try:
            ts = time.time()
            
            data = context['data'][0]
            agreement_data = data['agreement']

            # load commpliance template from the filesystem
            content = read_template(get_compliance_template_name(agreement_data['agreement_compliance_type']))


            # html temporary file
            file_name = f'{data["_id"].replace("-", "_").upper()}_{ts}'.replace(".", "_")
            html_tmp_path = os.path.join('/tmp/', f'{file_name}.html')

            # create html tmp file
            with open(html_tmp_path, "w") as html_tmp_file:

                content = content.substitute(**agreement_data)
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
            

        except Exception as err:
            print(str(err))
            pass



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

            # Generate PDF document
            request_data = AgreementComplianceList.generate_pdf_document(request_data, event_id)

            if request_data['agreement_compliance_type'] == "software-license-policy":
                response_json, status_code = self.update_software_license_policy(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "eula":
                response_json, status_code = self.update_eula(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "mou":
                response_json, status_code = self.update_mou(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)


            elif request_data['agreement_compliance_type'] == "website-terms-of-use":
                response_json, status_code = self.update_website_terms_of_use(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "website-privacy-policy":
                response_json, status_code = self.update_website_privacy_policy(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "website-security-policy":
                response_json, status_code = self.update_website_security_policy(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "non-compete-agreement":
                response_json, status_code = self.update_non_compete_agreement(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "cookie-policy":
                response_json, status_code = self.update_cookie_policy(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "return-and-refund":
                response_json, status_code = self.update_return_and_fund(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "app-disclaimer":
                response_json, status_code = self.update_app_disclaimer(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "app-privacy-policy":
                response_json, status_code = self.update_app_privacy_policy(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "nda":
                response_json, status_code = self.update_nda(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "discliamer-for-website":
                response_json, status_code = self.update_discliamer_for_website(
                    event_id= event_id,
                    request_data= request_data,
                    response_json= response_json,
                    status_code= status_code)

            elif request_data['agreement_compliance_type'] == "statement-of-work":
                response_json, status_code = self.update_statement_of_work(
                    event_id= event_id,
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


    def update_software_license_policy(self, event_id, request_data, response_json, status_code):

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
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code



    def update_eula(self, event_id, request_data, response_json, status_code):
        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])

        request_data["date_of_commencement"] = date.fromisoformat(
            request_data["date_of_commencement"])


        # Update and Commit data into database
        serializer = EulaSerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code


    def update_mou(self, event_id, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])

        request_data["date_of_commencement"] = date.fromisoformat(
            request_data["date_of_commencement"])

        request_data["date_of_termination"] = date.fromisoformat(
            request_data["date_of_termination"])

        request_data["date_for_legally_binding_definitive_agreement"] = date.fromisoformat(
            request_data["date_for_legally_binding_definitive_agreement"])

        request_data["date_for_legally_binding_definitive_agreement_2"] = date.fromisoformat(
            request_data["date_for_legally_binding_definitive_agreement_2"])


        # Update and Commit data into database
        serializer = MOUSerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_website_terms_of_use(self, event_id, request_data, response_json, status_code):

        from datetime import date

        request_data["terms_last_updated"] = date.fromisoformat(
            request_data["terms_last_updated"])


        # Update and Commit data into database
        serializer = WebsiteTermsOfUseSerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_website_privacy_policy(self, event_id, request_data, response_json, status_code):

        from datetime import date

        request_data["last_updated"] = date.fromisoformat(
            request_data["last_updated"])


        # Update and Commit data into database
        serializer = WebsitePrivacyPolicySerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_website_security_policy(self, event_id, request_data, response_json, status_code):

        from datetime import date

        request_data["last_updated"] = date.fromisoformat(
            request_data["last_updated"])


        # Update and Commit data into database
        serializer = WebsiteSecurityPolicySerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_non_compete_agreement(self, event_id, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])
        request_data["date_of_termination"] = date.fromisoformat(
            request_data["date_of_termination"])


        # Update and Commit data into database
        serializer = NonCompeteAgreementSerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_cookie_policy(self, event_id, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])


        # Update and Commit data into database
        serializer = CookiesPolicySerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_return_and_fund(self, event_id, request_data, response_json, status_code):

        from datetime import date

        request_data["date"] = date.fromisoformat(
            request_data["date"])


        # Update and Commit data into database
        serializer = ReturnAndRefundSerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_app_disclaimer(self, event_id, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])


        # Update and Commit data into database
        serializer = AppDisclaimerSerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_app_privacy_policy(self, event_id, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])


        # Update and Commit data into database
        serializer = AppPrivacyPolicySerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_nda(self, event_id, request_data, response_json, status_code):

        from datetime import date

        request_data["date_of_execution_of_document"] = date.fromisoformat(
            request_data["date_of_execution_of_document"])
        request_data["what_will_be_the_date_for_termination_of_this_nda"] = date.fromisoformat(
            request_data["what_will_be_the_date_for_termination_of_this_nda"])

        # Update and Commit data into database
        serializer = NDASerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code


    def update_statement_of_work(self, event_id, request_data, response_json, status_code):

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
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code

    def update_discliamer_for_website(self, event_id, request_data, response_json, status_code):

        from datetime import date

        request_data["last_update"] = date.fromisoformat(
            request_data["last_update"])

        # Update and Commit data into database
        serializer = DisclaimerForWebsiteSerializer(
            event_id, data=request_data)

        if serializer.is_valid():
            response_json, status_code = serializer.update(
                event_id, serializer.validated_data)

        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_json = {
                "isSuccess": False,
                "message": str(serializer.errors),
                "error": status_code
            }


        # return result
        return response_json, status_code





@xframe_options_exempt
def load_public_agreement_compliance(request, event_id:str):
    try:

        format = request.GET.get("format", "html")

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
        content = content.substitute(**agreement)
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
