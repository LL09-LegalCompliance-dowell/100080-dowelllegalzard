from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
import uuid

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
    def get(self, request, format=None):
        try:
            licenses = SoftwareLicense.objects.all()
            # Initialize serialize object
            serializer = SoftwareLicenseSerializer()

            return Response({
                "licenses": [serializer.to_representation(license) for license in licenses]
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
            software_license = serializer.save()

            return Response(
                {"license": serializer.to_representation(software_license)},
                status=status.HTTP_201_CREATED
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

            license = SoftwareLicense.objects.get(license_id = license_id)
            # Serialize data
            serializer = SoftwareLicenseSerializer()
            data = serializer.to_representation(license)

            return Response({"license": data}, status=status.HTTP_200_OK)


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
            # Get license
            software_license = SoftwareLicense.objects.get(license_id = license_id)
            request_data = request.data

            # Convert release date string (yyyy-mm-dd)
            # to date object
            request_data["released_date"] = date.fromisoformat(request_data["released_date"])

            # Update and Commit data into database
            serializer = SoftwareLicenseSerializer(software_license, data=request_data)
            if serializer.is_valid():
                software_license = serializer.save()            

            return Response(
                {"license": serializer.to_representation(software_license)},
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




    def delete(self, request, license_id, format = None):
        try:

            # Get License
            license = SoftwareLicense.objects.get(license_id = license_id)
            # Delete License
            license.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)


        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return Response({
                "error_msg": f"{e}"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            

