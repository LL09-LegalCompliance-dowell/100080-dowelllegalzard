from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import CommonAttributeSerializer, AttributeSerializer
from utils.dowell import (
    fetch_document,

    COMMON_ATTRIBUTE_COLLECTION,
    ATTRIBUTE_COLLECTION,

    COMMON_ATTRIBUTE_DOCUMENT_NAME,
    ATTRIBUTE_DOCUMENT_NAME,
    RECORD_PER_PAGE
)


class CommonAttributeList(APIView):
    def get(self, request, format=None):
        try:
            response_json = {}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            action_type = request.GET.get("action_type", "")

            if action_type == "search":
                response_json, status_code = self.search_common_attribute(
                    request, format)
            else:
                # Retrieve common attribute from remote server
                response_json = fetch_document(
                    collection=COMMON_ATTRIBUTE_COLLECTION,
                    document=COMMON_ATTRIBUTE_DOCUMENT_NAME,
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
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            request_data = request.data

            serializer = CommonAttributeSerializer(data=request_data)

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

    # SEARCH FOR COMMOM ATTRIBUTE HERE
    def search_common_attribute(self, request, format=None):
        """ Load common attribute base on search term
        """
        try:
            limit = RECORD_PER_PAGE
            offset = int(request.GET.get("offset", "0"))
            search_term = request.GET.get("search_term", "")
            response_json = {}

            # Retrieve COMMON ATTRIBUTE on remote server
            response_json = fetch_document(
                collection=COMMON_ATTRIBUTE_COLLECTION,
                document=COMMON_ATTRIBUTE_DOCUMENT_NAME,
                fields={"common_attributes.name": {
                    "$regex": f"{search_term}", "$options": "i"}}
            )

            return response_json, status.HTTP_200_OK

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return {"error_msg": f"{e}"}, status.HTTP_500_INTERNAL_SERVER_ERROR


class CommonAttributeDetail(APIView):
    def get(self, request, event_id, format=None):
        try:
            # Retrieve common attribute from remote server
            response_json = fetch_document(
                collection=COMMON_ATTRIBUTE_COLLECTION,
                document=COMMON_ATTRIBUTE_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )
            print("response_json: ", response_json)
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

            # Update and Commit data into database
            serializer = CommonAttributeSerializer(
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
            },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AttributeList(APIView):
    def get(self, request, format=None):
        try:
            response_json = {}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            action_type = request.GET.get("action_type", "")

            if action_type == "search":
                response_json, status_code = self.search_attribute(
                    request, format)
            else:
                # Retrieve common attribute from remote server
                response_json = fetch_document(
                    collection=ATTRIBUTE_COLLECTION,
                    document=ATTRIBUTE_DOCUMENT_NAME,
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
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            request_data = request.data

            serializer = AttributeSerializer(data=request_data)

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

    # SEARCH FOR ATTRIBUTE HERE

    def search_attribute(self, request, format=None):
        """ Load attribute base on search term
        """
        try:
            limit = RECORD_PER_PAGE
            offset = int(request.GET.get("offset", "0"))
            search_term = request.GET.get("search_term", "")
            response_json = {}

            # Retrieve ATTRIBUTE on remote server
            response_json = fetch_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                fields={"attributes.name": {
                    "$regex": f"{search_term}", "$options": "i"}}
            )

            return response_json, status.HTTP_200_OK

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return {"error_msg": f"{e}"}, status.HTTP_500_INTERNAL_SERVER_ERROR


class AttributeDetail(APIView):
    def get(self, request, event_id, format=None):
        try:
            # Retrieve common attribute from remote server
            response_json = fetch_document(
                collection=ATTRIBUTE_COLLECTION,
                document=ATTRIBUTE_DOCUMENT_NAME,
                fields={"eventId": event_id}
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

            # Update and Commit data into database
            serializer = AttributeSerializer(
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
