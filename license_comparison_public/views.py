from urllib import response
from django.shortcuts import render
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from storage.upload import upload_img
import uuid
from .validateapi import validateApikey
from utils.dowell import (
    fetch_document,
    update_document,
    format_id,
    SOFTWARE_LICENSE_COLLECTION,
    ATTRIBUTE_COLLECTION,

    SOFTWARE_LICENSE_DOCUMENT_NAME,
    ATTRIBUTE_DOCUMENT_NAME,
    ATTRIBUTE_MAIN_KEY,
    
    RECORD_PER_PAGE,
    BASE_IMAGE_URL
)


from .serializers import ComparisionSerializer
from licenses.views import SoftwareLicenseList


class ComparisionList(APIView):
    """ List all and create comparision
    """

    def get(self, request, format=None):
        user_api_key = request.META.get('HTTP_API_KEY')
        validate_api_count = validateApikey(user_api_key)
        data_count = json.loads(validate_api_count)
        if not user_api_key or not data_count['success'] or not data_count['count'] >=  0:
            status_code = 422
            return Response(
                {
                    "isSuccess": False,
                    "Error Message": "API Key not found or is Invalid!",
                },
                status=status_code
            )
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
        user_api_key = request.META.get('HTTP_API_KEY')
        validate_api_count = validateApikey(user_api_key)
        data_count = json.loads(validate_api_count)
        if not user_api_key or not data_count['success'] or not data_count['total_credits'] >=  0:
            status_code = 422
            return Response(
                {
                    "isSuccess": False,
                    "Error Message": "API Key not found or is Invalid!",
                },
                status=status_code
            )
        try:
            response_json = {}
            status_code = 500


            request_data = request.data

            license_1_event_id = request_data['license_1_event_id']
            license_2_event_id = request_data['license_2_event_id']

            
            license_1 = self.get_license(license_1_event_id)["data"][0]["softwarelicense"]
            license_2 = self.get_license(license_2_event_id)["data"][0]["softwarelicense"]

            license_1_logo_url = "#"
            if "logo_detail" in license_1:
                license_1_logo_url = license_1["logo_detail"]["url"]


            license_2_logo_url = "#"
            if "logo_detail" in license_1:
                license_2_logo_url = license_2["logo_detail"]["url"]



            request_data['attribute_type'] = "comparisions"
            request_data['identifier'] = f"{license_1_event_id}-{license_2_event_id},{license_2_event_id}-{license_1_event_id}"
            request_data['license_1_logo_url'] = license_1_logo_url
            request_data['license_2_logo_url'] = license_2_logo_url
            request_data['license_1_name'] = license_1["license_name"]
            request_data['license_2_name'] = license_2["license_name"]
            request_data['license_1_version'] = license_1["version"]
            request_data['license_2_version'] = license_2["version"]
            request_data['license_1_event_id'] = license_1_event_id
            request_data['license_2_event_id'] = license_2_event_id
            request_data['percentage_of_compatibility'] = int(request_data['percentage_of_compatibility'])
            request_data['comparisons'] = []

            serializer = ComparisionSerializer(data=request_data)

            # Commit data to database
            if serializer.is_valid():
                response_json, status_code = serializer.save()

            else:
                print(f"{serializer.errors}")
                return Response({
                    "error_msg": f"{serializer.errors}"
                },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )                

            return Response(response_json,
                            status=status_code
                            )

        
        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return Response({
                "error_msg": f"{e}",
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
            },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @staticmethod
    def get_license(event_id):
        
        # Retrieve license
        user_api_key = request.META.get('HTTP_API_KEY')
        validate_api_count = validateApikey(user_api_key)
        data_count = json.loads(validate_api_count)
        if not user_api_key or not data_count['success'] or not data_count['total_credits'] >=  0:
            status_code = 422
            return Response(
                {
                    "isSuccess": False,
                    "Error Message": "API Key not found or is Invalid!",
                },
                status=status_code
            )
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
        user_api_key = request.META.get('HTTP_API_KEY')
        validate_api_count = validateApikey(user_api_key)
        data_count = json.loads(validate_api_count)
        if not user_api_key or not data_count['success'] or not data_count['total_credits'] >=  0:
            status_code = 422
            return Response(
                {
                    "isSuccess": False,
                    "Error Message": "API Key not found or is Invalid!",
                },
                status=status_code
            )
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
                "error_msg": f"{e}",
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
            },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, event_id, format=None):
        user_api_key = request.META.get('HTTP_API_KEY')
        validate_api_count = validateApikey(user_api_key)
        data_count = json.loads(validate_api_count)
        if not user_api_key or not data_count['success'] or not data_count['total_credits'] >=  0:
            status_code = 422
            return Response(
                {
                    "isSuccess": False,
                    "Error Message": "API Key not found or is Invalid!",
                },
                status=status_code
            )
        try:

            request_data = request.data

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

            
            # move this block of code
            # Delete attribute name comparisions
            if "comparisions" in license_comparison:
                del license_comparison["comparisions"]
                license_comparison["comparisons"] = []
            # move this block of code



            if action_type == "add-license-category-comparison":
                comparison = request_data["comparison"]
                comparison['_id'] = str(uuid.uuid4())
                license_comparison["comparisons"].append(comparison)


                # Update
                serializer = ComparisionSerializer(
                    event_id, data=license_comparison)
                if serializer.is_valid():
                    response_json, status_code = serializer.update(
                        event_id, serializer.validated_data)

                    return Response(
                        {
                        "isSuccess": response_json["isSuccess"],
                        "comparison": comparison
                        },
                        status=status_code
                    )

                else:
                    return Response({"error_msg": f"{serializer.errors}"},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                    )
                
            elif action_type == "update-license-category-comparison":
                comparison = request_data["comparison"]
                temp_comparisons = []

                comparison_id = request_data["comparison_id"]

                for data in license_comparison["comparisons"]:

                    if comparison_id == data["_id"]:

                        # Update license comparison object
                        comparison_new = {**data, **comparison}
                        temp_comparisons.append(comparison_new)

                    else:
                        temp_comparisons.append(data)

                # Update list of license comparison object
                license_comparison["comparisons"] = temp_comparisons


                # Update
                serializer = ComparisionSerializer(
                    event_id, data=license_comparison)
                if serializer.is_valid():
                    response_json, status_code = serializer.update(
                        event_id, serializer.validated_data)

                    return Response(
                        {
                        "isSuccess": response_json["isSuccess"],
                        "comparison": comparison_new,
                        "status_code": status_code
                        },
                        status=status_code
                    )

            elif action_type == "update-license-comparison":

                license_1_event_id = request_data['license_1_event_id']
                license_2_event_id = request_data['license_2_event_id']

                
                license_1 = ComparisionList.get_license(license_1_event_id)["data"][0]["softwarelicense"]
                license_2 = ComparisionList.get_license(license_2_event_id)["data"][0]["softwarelicense"]

                license_1_logo_url = "#"
                if "logo_detail" in license_1:
                    license_1_logo_url = license_1["logo_detail"]["url"]

                license_2_logo_url = "#"
                if "logo_detail" in license_1:
                    license_2_logo_url = license_2["logo_detail"]["url"]

                
                license_comparison['identifier'] = f"{license_1_event_id}-{license_2_event_id},{license_2_event_id}-{license_1_event_id}"
                license_comparison['license_1_logo_url'] = license_1_logo_url
                license_comparison['license_2_logo_url'] = license_2_logo_url
                license_comparison['license_1_name'] = license_1["license_name"]
                license_comparison['license_2_name'] = license_2["license_name"]
                license_comparison['license_1_version'] = license_1["version"]
                license_comparison['license_2_version'] = license_2["version"]
                license_comparison['license_1_event_id'] = license_1_event_id
                license_comparison['license_2_event_id'] = license_2_event_id
                license_comparison['percentage_of_compatibility'] = int(request_data['percentage_of_compatibility'])
                license_comparison['recommendation'] = request_data['recommendation']
                license_comparison['recommendation_details'] = request_data['recommendation_details']
                license_comparison['disclaimer'] = request_data['disclaimer']

                # Update
                serializer = ComparisionSerializer(
                    event_id, data=license_comparison)
                if serializer.is_valid():
                    response_json, status_code = serializer.update(
                        event_id, serializer.validated_data)

                    return Response(
                        {
                        "isSuccess": response_json["isSuccess"],
                        "status_code": status_code
                        },
                        status=status_code
                    )


                else:
                    return Response({
                        "error_msg": str(serializer.errors),
                        "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
                    },
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR )


            
        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return Response({
                "error_msg": f"{e}",
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
            },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



    def delete(self, request, event_id, format=None):
        user_api_key = request.META.get('HTTP_API_KEY')
        validate_api_count = validateApikey(user_api_key)
        data_count = json.loads(validate_api_count)
        if not user_api_key or not data_count['success'] or not data_count['total_credits'] >=  0:
            status_code = 422
            return Response(
                {
                    "isSuccess": False,
                    "Error Message": "API Key not found or is Invalid!",
                },
                status=status_code
            )
        try:

            request_data = request.data

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

            
            # Update comparision
            license_comparison['is_active'] = False
            license_comparison['identifier'] = ""
            response_json = update_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                key=ATTRIBUTE_MAIN_KEY,
                new_value=license_comparison,
                event_id=event_id
            )

            return Response(
                {
                "isSuccess": response_json["isSuccess"],
                "event_id": event_id,
                "status_code": 200
                },
                status=200
            )

                
        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return Response({
                "error_msg": f"{e}",
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
            },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

