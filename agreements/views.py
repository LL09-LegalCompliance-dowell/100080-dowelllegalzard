from urllib import response
from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
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

    def post(self, request, format=None):
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

            # Create serializer object
            serializer = SoftwareAgreementSerializer(data=request_data)

            # Commit data to database
            serializer.is_valid()
            response_json, status_code = serializer.save()

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

    def get(self, request, agreement_id, format=None):
        try:

            # Retrieve license on remote server
            response_json = fetch_document(
                collection=SOFTWARE_AGREEMENT_COLLECTION,
                document=SOFTWARE_AGREEMENT_DOCUMENT_NAME,
                fields={"_id": agreement_id}
            )

            return Response(response_json, status=status.HTTP_200_OK)

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return Response({
                "error_msg": f"{e}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, agreement_id, format=None):
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
                agreement_id, data=request_data)

            if serializer.is_valid():
                response_json, status_code = serializer.update(
                    agreement_id, serializer.validated_data)

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
