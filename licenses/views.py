import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import _thread
import uuid
from utils.dowell import (
    fetch_document,
    save_document,
    
    SOFTWARE_LICENSE_COLLECTION,
    ATTRIBUTE_COLLECTION,

    SOFTWARE_LICENSE_DOCUMENT_NAME,
    ATTRIBUTE_DOCUMENT_NAME,
    RECORD_PER_PAGE,
    BASE_IMAGE_URL,
    COMPARISON_HISTORY_COLLECTION,
    COMPARISON_HISTORY_DOCUMENT_NAME,
    COMPARISON_HISTORY_KEY
)
from licenses.serializers import SoftwareLicenseSerializer
from licenses.license_percentage_recommendation import calculate_percentage_recommendation


class SoftwareLicenseList(APIView):
    """ List all and create software license
    """

    def get(self, request, format=None):
        try:

            limit = RECORD_PER_PAGE
            offset = int(request.GET.get("offset", "0"))
            action_type = request.GET.get("action_type", "")
            collection_type = request.GET.get("collection_type", "license")
            user_id = request.GET.get("user_id", "")
            organization_id = request.GET.get("organization_id", "")

            response_json = {}
            status_code = 500

            if action_type == "search":

                if collection_type == "license":
                    response_json, status_code = self.search_license(
                        request, format)
                    response_json = self.add_license_logo_url(response_json)

                elif collection_type == "license-compatibility-history":
                    pass
                    # response_json, status_code = self.search_license(
                    #     request, format)

            else:

                
                # Retrieve license on remote server
                if collection_type == "license":
                    
                    response_json = fetch_document(
                        collection=SOFTWARE_LICENSE_COLLECTION,
                        document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                        fields={"softwarelicense.is_active": True}
                    )
                    response_json = self.add_license_logo_url(response_json)
                    status_code = status.HTTP_200_OK


                elif collection_type == "license-compatibility-history":
                    user_id = int(user_id)

                    if organization_id and user_id:
                        print("working")
                        response_json = fetch_document(
                            collection=COMPARISON_HISTORY_COLLECTION,
                            document=COMPARISON_HISTORY_DOCUMENT_NAME,
                            fields={
                                "license_compatibility_history.organization_id": organization_id,
                                "license_compatibility_history.user_id": user_id
                                }
                        )
                    elif organization_id and user_id == "":
                        response_json = fetch_document(
                            collection=COMPARISON_HISTORY_COLLECTION,
                            document=COMPARISON_HISTORY_DOCUMENT_NAME,
                            fields={"license_compatibility_history.organization_id": organization_id}
                        )

                    elif organization_id == "" and user_id == "":
                        response_json = fetch_document(
                            collection=COMPARISON_HISTORY_COLLECTION,
                            document=COMPARISON_HISTORY_DOCUMENT_NAME,
                            fields={}
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
                       "error_msg": str(serializer.errors) 
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
            license_two = license_two_json["data"][0]['softwarelicense']

            
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

            

            

            comparison_detail = {}
            if license_comparison:

                # license_compatible_with_lookup = license_two["license_compatible_with_lookup"]
                percentage_of_compatibility = calculate_percentage_recommendation(license_one, license_two)
                if percentage_of_compatibility >= 60:
                    is_compatible = True


                # Update percentage_of_compatibility
                license_comparison['percentage_of_compatibility'] = percentage_of_compatibility


                comparison_detail = {
                    "is_compatible": is_compatible,
                    "license_comparison": license_comparison,
                    "identifier": identifier
                }

                # log current comparison to history
                _thread.start_new_thread(
                    SoftwareLicenseList.log_comparison_history,(request, comparison_detail))
                
                return (comparison_detail), status.HTTP_200_OK
            
            else:
                return ({}), status.HTTP_500_INTERNAL_SERVER_ERROR


        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return {"error_msg": f"{e}"}, status.HTTP_500_INTERNAL_SERVER_ERROR
        

    @staticmethod
    def log_comparison_history(request, comparison_detail):
        """ log comparison to history
        """
        try:

            user_id = request.data.get("user_id", 0)
            organization_id = request.data.get("organization_id", "")

            if user_id and organization_id:
                data = {
                    "organization_id": organization_id,
                    "user_id": user_id,
                    "comparison_detail": comparison_detail
                }

                # Create log
                response_json = save_document(
                    collection=COMPARISON_HISTORY_COLLECTION,
                    document=COMPARISON_HISTORY_DOCUMENT_NAME,
                    key=COMPARISON_HISTORY_KEY,
                    value=data
                )
            
        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")




    # SEARCH FOR LICENSES HERE

    def search_license(self, request, format=None):
        """ Load linceses base on search term
        """
        try:

            limit = RECORD_PER_PAGE
            offset = int(request.GET.get("offset", "0"))
            search_term = request.GET.get("search_term", "")
            response_json = {}

            # Retrieve license on remote server
            response_json = fetch_document(
                collection=SOFTWARE_LICENSE_COLLECTION,
                document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields={"softwarelicense.license_name": {
                    "$regex": f"{search_term}", "$options": "i"}, "softwarelicense.is_active": True}
            )

            return response_json, status.HTTP_200_OK

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return {"error_msg": f"{e}"}, status.HTTP_500_INTERNAL_SERVER_ERROR

    @staticmethod
    def add_license_logo_url(response_data):

        if "data" not in response_data:
            return response_data
        
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
            if "filename" in logo_detail:
                logo_detail['url'] = f'{BASE_IMAGE_URL}{logo_detail["filename"]}'

            # update license logo detail
            softwarelicense['logo_detail'] = logo_detail

            # add licence to new data list
            data['softwarelicense'] = softwarelicense
            new_data_list.append(data)

        if new_data_list:
            response_data['data'] = new_data_list

        return response_data


    @staticmethod
    def create_other_attribute(attribute_list:list):
        try:

            from attributes.serializers import AttributeSerializer

            for attribute in attribute_list:
                new_attribute = {
                    "name": attribute,
                    "attribute_id": str(uuid.uuid4()),
                    "common_attribute": {
                        "_id": "63a857634686ef65557b6c1f",
                        "eventId": "FB1010000000016719767975641828",
                        "name": "Other",
                        "code": "other"
                    }
                }

                serializer = AttributeSerializer(data=new_attribute)

                # Commit data to database
                serializer.is_valid()
                response_json, status_code = serializer.save()

        except Exception as err:
            print(str(err))




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
                return Response({"error_msg": str(serializer.errors)},
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

    def delete(self, request, event_id, format=None):
        try:
            from datetime import date
            from utils.dowell import (
                fetch_document,
                update_document,
                SOFTWARE_LICENSE_COLLECTION,
                SOFTWARE_LICENSE_DOCUMENT_NAME,
                SOFTWARE_LICENSE_KEY,
            )


            response_json = fetch_document(
                collection=SOFTWARE_LICENSE_COLLECTION,
                document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )

            license = response_json["data"][0]["softwarelicense"]
            license["is_active"] = False


            # # Update license on remote server
            response_json = update_document(
                collection=SOFTWARE_LICENSE_COLLECTION,
                document=SOFTWARE_LICENSE_DOCUMENT_NAME,
                key=SOFTWARE_LICENSE_KEY,
                new_value=license,
                event_id=event_id
            )

            if response_json["isSuccess"]:
                return Response(
                    {
                        "event_id": event_id,
                        "isSuccess": True
                    },
                    status=200
                )

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return Response({
                "error_msg": f"{e}",
                "isSuccess": False
            },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
