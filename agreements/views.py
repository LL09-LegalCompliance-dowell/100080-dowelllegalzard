from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.db import transaction
from storage.upload import upload_img
import uuid
from utils.dowell import (
    fetch_document,
    SOFTWARE_AGREEMENT_COLLECTION,
    SOFTWARE_AGREEMENT_DOCUMENT_NAME,
    RECORD_PER_PAGE
)


from agreements.serializers import SoftwareAgreementSerializer


class SoftwareAgreementList(APIView):
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
            from datetime import date
            request_data = request.data
            request_data["is_active"] = True

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

            # # Save image [part 1 signatory]
            # if request_data['party_1_signatory_scanned_copy_url']:
            #     filename, file_extension, file_path =\
            #         upload_img(
            #             request_data['party_1_signatory_scanned_copy_url'])

            # # Save image [part 2 signatory]
            # if request_data['party_2_signatory_scanned_copy_url']:
            #     filename, file_extension, file_path =\
            #         upload_img(
            #             request_data['party_2_signatory_scanned_copy_url'])

            # Create serializer object
            serializer = SoftwareAgreementSerializer(data=request_data)

            # Commit data to database
            response_json = {}
            status_code = 500
            if serializer.is_valid():
                response_json, status_code = serializer.save()
            else:
                response_json = serializer.errors

            return Response(response_json,
                            status=status_code
                            )

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return Response({
                "error_msg": f"{e}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SoftwareAgreementDetail(APIView):
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

            # Convert release date string (yyyy-mm-dd)
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
            serializer = SoftwareAgreementSerializer(
                event_id, data=request_data)

            if serializer.is_valid():
                response_json, status_code = serializer.update(
                    event_id, serializer.validated_data)

                return Response(
                    response_json,
                    status=status_code
                )

            else:
                return Response({"error_msg": f"{e}"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                )

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return Response({
                "error_msg": f"{e}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
