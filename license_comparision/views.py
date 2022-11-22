from urllib import response
from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from storage.upload import upload_img
import uuid
from utils.dowell import (
    fetch_document,
    format_id,
    SOFTWARE_LICENSE_COLLECTION,
    ATTRIBUTE_COLLECTION,

    SOFTWARE_LICENSE_DOCUMENT_NAME,
    ATTRIBUTE_DOCUMENT_NAME,
    
    RECORD_PER_PAGE,
    BASE_IMAGE_URL
)


from .serializers import ComparisionSerializer
from licenses.views import SoftwareLicenseList


class ComparisionList(APIView):
    """ List all and create comparision
    """

    def get(self, request, format=None):
        try:

            limit = RECORD_PER_PAGE
            offset = int(request.GET.get("offset", "0"))
            action_type = request.GET.get("action_type", "")
            response_json = {}
            status_code = 500

            # Retrieve comparision
            response_json = fetch_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                fields={"attributes.attribute_type": "comparisions"}
            )

            status_code = status.HTTP_200_OK

            return Response(
                response_json,
                status=status_code)


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
            response_json = {}
            status_code = 500


            request_data = request.data

            license_1_event_id = request_data['license_1_event_id']
            license_2_event_id = request_data['license_2_event_id']

            
            license_1 = self.get_license(license_1_event_id)["data"][0]["softwarelicense"]
            license_2 = self.get_license(license_2_event_id)["data"][0]["softwarelicense"]

            license_1_logo_url = ""
            if "logo_detail" in license_1:
                license_1_logo_url = license_1["logo_detail"]["url"]

            license_2_logo_url = ""
            if "logo_detail" in license_1:
                license_2_logo_url = license_2["logo_detail"]["url"]



            request_data['attribute_type'] = "comparisions"
            request_data['indentifier'] = f"{license_1_event_id}+{license_2_event_id},{license_2_event_id}+{license_1_event_id}"
            request_data['license_1_logo_url'] = license_1_logo_url
            request_data['license_2_logo_url'] = license_2_logo_url
            request_data['license_1_name'] = license_1["license_name"]
            request_data['license_2_name'] = license_2["license_name"]
            request_data['license_1_version'] = license_1["version"]
            request_data['license_2_version'] = license_2["version"]
            request_data['license_1_event_id'] = license_1_event_id
            request_data['license_2_event_id'] = license_2_event_id
            request_data['comparisions'] = []

            serializer = ComparisionSerializer(data=request_data)

            # Commit data to database
            print("working")
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

    @staticmethod
    def get_license(event_id):
        
        # Retrieve license
        response_json = fetch_document(
            collection=SOFTWARE_LICENSE_COLLECTION,
            document=SOFTWARE_LICENSE_DOCUMENT_NAME,
            fields={"eventId": event_id}
        )

        response_json = SoftwareLicenseList.add_license_logo_url(
            response_json)


        return response_json



class ComparisionDetail(APIView):
    """
     Retrieve , update and comparision
    """

    def get(self, request, event_id, format=None):
        try:

            # Get comparision
            response_json = fetch_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                fields={"eventId": event_id, "attributes.attribute_type": "comparisions"}
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

    def put(self, request, event_id, format=None):
        try:

            request_data = request.data
            comparision = request_data["comparision"]

            action_type = ""
            if "action_type" in request_data:
                action_type = request_data["action_type"]

            # Get license comparision 
            response_json = fetch_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )
            license_comparison = response_json["data"][0]["attributes"]


            if action_type == "add-license-category-comparison":

                comparision['_id'] = str(uuid.uuid4())
                license_comparison["comparisions"].append(comparision)


                # Update
                serializer = ComparisionSerializer(
                    event_id, data=license_comparison)
                if serializer.is_valid():
                    response_json, status_code = serializer.update(
                        event_id, serializer.validated_data)

                    return Response(
                        response_json,
                        status=status_code
                    )

                else:
                    return Response({"error_msg": f"{serializer.errors}"},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                    )
                
            elif action_type == "update-license-category-comparison":

                temp_comparisions = []
                comparision_id = request_data["comparision_id"]

                for data in license_comparison["comparisions"]:

                    if comparision_id == data["_id"]:

                        # Update license comparison object
                        comparision_new = {**data, **comparision}
                        temp_comparisions.append(comparision_new)

                    else:
                        temp_comparisions.append(data)

                # Update list of license comparison object
                license_comparison["comparisions"] = temp_comparisions


                # Update
                serializer = ComparisionSerializer(
                    event_id, data=license_comparison)
                if serializer.is_valid():
                    response_json, status_code = serializer.update(
                        event_id, serializer.validated_data)

                    return Response(
                        response_json,
                        status=status_code
                    )

                else:
                    return Response({"error_msg": f"{serializer.errors}"},
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