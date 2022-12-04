import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.dowell import (
    fetch_document,
    
    SOFTWARE_LICENSE_COLLECTION,
    ATTRIBUTE_COLLECTION,

    SOFTWARE_LICENSE_DOCUMENT_NAME,
    ATTRIBUTE_DOCUMENT_NAME,
    RECORD_PER_PAGE,
    BASE_IMAGE_URL
)
from licenses.serializers import SoftwareLicenseSerializer


class SoftwareLicenseList(APIView):
    """ List all and create software license
    """

    def get(self, request, format=None):
        try:

            limit = RECORD_PER_PAGE
            offset = int(request.GET.get("offset", "0"))
            action_type = request.GET.get("action_type", "")
            response_json = {}
            status_code = 500

            if action_type == "search":
                response_json, status_code = self.search_license(
                    request, format)
            else:
                # Retrieve license on remote server
                response_json = fetch_document(
                    collection=SOFTWARE_LICENSE_COLLECTION,
                    document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                    fields={}
                )

                response_json = self.add_license_logo_url(response_json)
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

            from datetime import date
            request_data = request.data

            action_type = ""
            if "action_type" in request_data:
                action_type = request_data["action_type"]

            if action_type == "check-compatibility":
                response_json, status_code = self.check_license_compatibility(
                    request, format)
            else:
                request_data["is_active"] = True

                serializer = SoftwareLicenseSerializer(data=request_data)

                # Commit data to database
                if serializer.is_valid():
                    response_json, status_code = serializer.save()

                else:
                    print(serializer.errors)
                    response_json = {
                       "error_msg": f"{serializer.errors}" 
                    }
                    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


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

    # CHECK FOR COMPATIBILITY HERE

    def check_license_compatibility(self, request, format=None):
        """ Check for two licnese and return True if 
            license_one == license_two
        """
        is_compatible = False
        try:

            license_event_id_one = request.data.get("license_event_id_one", "")
            license_event_id_two = request.data.get("license_event_id_two", "")

            # Retrieve license on remote server
            # Get license two
            license_one_json = fetch_document(
                collection=SOFTWARE_LICENSE_COLLECTION,
                document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields={"eventId": license_event_id_one}
            )
            license_one = license_one_json["data"][0]['softwarelicense']

            # Get license two
            license_two_json = fetch_document(
                collection=SOFTWARE_LICENSE_COLLECTION,
                document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields={"eventId": license_event_id_two}
            )

            
            # Get licence comparision
            identifier = f"{license_event_id_one}-{license_event_id_two}"
            license_comparison_json = fetch_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                fields={
                    "attributes.identifier":{"$regex": identifier, "$options": "i"},
                    "attributes.attribute_type": "comparisions"
                    })


            license_comparison = {}
            if license_comparison_json["data"]:
                license_comparison = license_comparison_json["data"][0]["attributes"]

                

            # Get license compatible list
            license_two = license_two_json["data"][0]['softwarelicense']
            license_compatible_with_lookup = license_two["license_compatible_with_lookup"]

            

            # Check for compatibility
            if license_one["license_name"] in license_compatible_with_lookup:
                is_compatible = True


            return ({
                "is_compatible": is_compatible,
                "license_comparison": license_comparison

            }), status.HTTP_200_OK

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return {"error_msg": f"{e}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

    # SEARCH FOR LICENSES HERE

    def search_license(self, request, format=None):
        """ Load linceses base on search term
        """
        try:
            print("I was called")
            limit = RECORD_PER_PAGE
            offset = int(request.GET.get("offset", "0"))
            search_term = request.GET.get("search_term", "")
            response_json = {}

            # Retrieve license on remote server
            response_json = fetch_document(
                collection=SOFTWARE_LICENSE_COLLECTION,
                document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields={"softwarelicense.license_name": {
                    "$regex": f"{search_term}", "$options": "i"}}
            )

            return response_json, status.HTTP_200_OK

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return {"error_msg": f"{e}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

    @staticmethod
    def add_license_logo_url(response_data):
        data_list = response_data['data']
        new_data_list = []

        for data in data_list:
            softwarelicense = data['softwarelicense']
            # this code only execute
            # if the license object
            # does not have logo_detail field
            if "logo_detail" not in softwarelicense:
                new_data_list.append(data)
                continue

            logo_detail = softwarelicense['logo_detail']
            logo_detail['url'] = f'{BASE_IMAGE_URL}{logo_detail["filename"]}'

            # update license logo detail
            softwarelicense['logo_detail'] = logo_detail

            # add licence to new data list
            data['softwarelicense'] = softwarelicense
            new_data_list.append(data)

        if new_data_list:
            response_data['data'] = new_data_list

        return response_data


class SoftwareLicenseDetail(APIView):
    """
     Retrieve , update and delete software license
    """

    def get(self, request, event_id, format=None):
        try:
            # # Localhost
            # license = SoftwareLicense.objects.get(license_id = license_id)
            # # Serialize data
            # serializer = SoftwareLicenseSerializer()
            # data = serializer.to_representation(license.document, license.id)

            # Retrieve license on remote server
            response_json = fetch_document(
                collection=SOFTWARE_LICENSE_COLLECTION,
                document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )

            response_json = SoftwareLicenseList.add_license_logo_url(
                response_json)
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
            from datetime import date
            request_data = request.data


            # Update and Commit data into database
            serializer = SoftwareLicenseSerializer(
                event_id, data=request_data)
            if serializer.is_valid():
                response_json, status_code = serializer.update(
                    event_id, serializer.validated_data)

                return Response(
                    response_json,
                    status=status_code
                )

            else:
                print(serializer.errors)
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
