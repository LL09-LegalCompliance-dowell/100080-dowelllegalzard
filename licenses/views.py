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
    SOFTWARE_LICENSE_COLLECTION,
    COMMON_ATTRIBUTE_COLLECTION,
    ATTRIBUTE_COLLECTION,
    LICENSE_TYPE_COLLECTION,

    SOFTWARE_AGREEMENT_DOCUMENT_NAME,
    SOFTWARE_LICENSE_DOCUMENT_NAME,
    COMMON_ATTRIBUTE_DOCUMENT_NAME,
    ATTRIBUTE_DOCUMENT_NAME,
    LICENSE_TYPE_DOCUMENT_NAME,
    )

from licenses.models import (
    SoftwareLicense,
    SoftwareLicenseAgreement
)
from licenses.serializers import (
    SoftwareLicenseSerializer
)


# Create your views here.
def dowell_login(username, password):
    url = "http://100014.pythonanywhere.com/api/login/"
    userurl = "http://100014.pythonanywhere.com/api/user/"
    payload = {
        'username': username,
        'password': password
    }
    with requests.Session() as s:
        p = s.post(url, data=payload)
        if "Username" in p.text:
            return p.text
        else:
            user = s.get(userurl)
            return user.text


class SoftwareLicenseList(APIView):
    """ List all and create software license
    """
    def get(self, request,format=None):
        try:

            limit = int(request.GET.get("limit", "10"))
            offset = int(request.GET.get("offset", "0"))

            # # Localhost
            # licenses_query = SoftwareLicense.objects.all()[offset:limit]
            # # Initialize serialize object
            # serializer = SoftwareLicenseSerializer()
            # licenses = [serializer.to_representation(license.document, license.license_id) for license in licenses_query]
            # response_json = {"data": license}

            # Retrieve license on remote server
            response_json = fetch_document(
                collection= SOFTWARE_LICENSE_COLLECTION,
                document= SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields={}
                )

            return Response({response_json},
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

    def post(self, request, format = None):
        try:
            from datetime import date
            request_data = request.data
            request_data["is_active"] = True


            # Convert release date string (yyyy-mm-dd)
            # to date object
            request_data["released_date"] = date.fromisoformat(request_data["released_date"])
            serializer = SoftwareLicenseSerializer(data=request_data)

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
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


class SoftwareLicenseSearch(APIView):
    """ Load linceses base on search term
    """
    def get(self, request, format=None):
        try:

            limit = int(request.GET.get("limit", "10"))
            offset = int(request.GET.get("offset", "0"))
            search_term = request.GET.get("search_term", "")
            response_json = {}

            # Localhost
            # # Retrieve licenses 
            # licenses_query = SoftwareLicense.objects.filter(
            #     document__license_name__icontains = search_term
            #     )[offset: limit]

            # # Initialize serialize object
            # serializer = SoftwareLicenseSerializer()
            # licenses = [serializer.to_representation(license.document, license.license_id) for license in licenses_query]
            # response_json = {"data": licenses}


            # Retrieve license on remote server 
            response_json = fetch_document(
                collection= SOFTWARE_LICENSE_COLLECTION,
                document= SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields= { "license_name": f"/{search_term}/" }
                )

            return Response({response_json},
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


class SoftwareLicenseDetail(APIView):
    """
     Retrieve , update and delete software license
    """
    def get(self, request, license_id, format = None):
        try:
            # # Localhost
            # license = SoftwareLicense.objects.get(license_id = license_id)
            # # Serialize data
            # serializer = SoftwareLicenseSerializer()
            # data = serializer.to_representation(license.document, license.id)

            # Retrieve license on remote server
            response_json = fetch_document(
                collection= SOFTWARE_LICENSE_COLLECTION,
                document= SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields={"_id": license_id}
                )
            return Response(response_json, status=status.HTTP_200_OK)


        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return Response({
                "error_msg": f"{e}"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


    def put(self, request, license_id, format = None):
        try:
            from datetime import date
            request_data = request.data

            # Convert release date string (yyyy-mm-dd)
            # to date object
            request_data["released_date"] = date.fromisoformat(request_data["released_date"])

            # Update and Commit data into database
            serializer = SoftwareLicenseSerializer(license_id, data=request_data)
            if serializer.is_valid():
                response_json, status_code = serializer.update(license_id, serializer.validated_data)            
                
                return Response(
                    response_json,
                    status = status_code
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
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

class CheckLicenseCompatibility(APIView):
    """ Check for two licnese and return True if 
        license_one == license_two
    """

    def post(self, request, format=None):
        is_compatible = False
        try:
            
            license_one_id = request.data.get("license_one_id", "")
            license_two_id = request.data.get("license_two_id", "")

            # Localhost
            #  # Retrieve licenses 
            # license_one = SoftwareLicense.objects.get(pk = license_one_id)
            # license_two = SoftwareLicense.objects.get(pk = license_two_id)

            # # Check, if license_one is compatible with license_two
            # license_compatible_with_lookup = licenses_two.document["license_compatible_with_lookup"]
            # if licenses_one.document["license_name"] in license_compatible_with_lookup:
            #     is_compatible = True


            # Retrieve license on remote server 
            license_one_json = fetch_document(
                collection= SOFTWARE_LICENSE_COLLECTION,
                document= SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields= { "_id": license_one_id }
                )
            license_one = license_one_json["data"][0]

            license_two_json = fetch_document(
                collection= SOFTWARE_LICENSE_COLLECTION,
                document= SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields= { "_id": license_two_id }
                )

            # Get license compatible list
            license_two = license_two_json["data"][0]
            license_compatible_with_lookup = license_two["license_compatible_with_lookup"]

            if license_one["license_name"] in license_compatible_with_lookup:
                is_compatible = True


            return Response({
                "is_compatible": is_compatible
            },

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



