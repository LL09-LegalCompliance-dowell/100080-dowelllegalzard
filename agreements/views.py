from email import message
import os
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.db import transaction
from storage.upload import upload_img
import uuid
from DowellLicenseProject.settings import BASE_DIR
from utils.dowell import (
    fetch_document,
    SOFTWARE_AGREEMENT_COLLECTION,
    SOFTWARE_AGREEMENT_DOCUMENT_NAME,
    RECORD_PER_PAGE
)
from utils.general import read_template, get_compliance_template_name
from agreements.serializers import (
    SoftwareLicensePolicySerializer,
    EulaSerializer
    
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

        request_data["effective_date_for_invoice_payment"] = date.fromisoformat(
            request_data["effective_date_for_invoice_payment"])

        request_data["party_1_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_1_date_of_signing_contract"])

        request_data["party_1_witness_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_1_witness_date_of_signing_contract"])

        request_data["party_2_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_2_date_of_signing_contract"])

        request_data["party_2_witness_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_2_witness_date_of_signing_contract"])

        request_data["invoicing_date"] = date.fromisoformat(
            request_data["invoicing_date"])

        request_data["contract_termination_date"] = date.fromisoformat(
            request_data["contract_termination_date"])

        request_data["contract_effective_date"] = date.fromisoformat(
            request_data["contract_effective_date"])


        # Create serializer object
        serializer = SoftwareLicensePolicySerializer(data=request_data)

        # Commit data to database
        if serializer.is_valid():
            response_json, status_code = serializer.save()
        else:
            response_json = serializer.errors

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
            response_json = serializer.errors

        # return result
        return response_json, status_code



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

        request_data["effective_date_for_invoice_payment"] = date.fromisoformat(
            request_data["effective_date_for_invoice_payment"])

        request_data["party_1_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_1_date_of_signing_contract"])

        request_data["party_1_witness_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_1_witness_date_of_signing_contract"])

        request_data["party_2_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_2_date_of_signing_contract"])

        request_data["party_2_witness_date_of_signing_contract"] = date.fromisoformat(
            request_data["party_2_witness_date_of_signing_contract"])

        request_data["invoicing_date"] = date.fromisoformat(
            request_data["invoicing_date"])

        request_data["contract_termination_date"] = date.fromisoformat(
            request_data["contract_termination_date"])

        request_data["contract_effective_date"] = date.fromisoformat(
            request_data["contract_effective_date"])


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
                "message": serializer.errors,
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
                "message": serializer.errors,
                "error": status_code
            }


        # return result
        return response_json, status_code



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
