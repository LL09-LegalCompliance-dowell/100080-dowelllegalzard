from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContactSerializer
from utils.dowell import (
    fetch_document,
    CONTACT_COLLECTION,
    CONTACT_DOCUMENT_NAME,
    RECORD_PER_PAGE)


class ContactList(APIView):
    def get(self, request, format=None):
        try:
            response_json = {}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            action_type = request.GET.get("action_type", "")

            if action_type == "search":
                response_json, status_code = self.search_contact(
                    request, format)
            else:
                # Retrieve contact us from remote server
                response_json = fetch_document(
                    collection=CONTACT_COLLECTION,
                    document=CONTACT_DOCUMENT_NAME,
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
            print(request_data)

            serializer = ContactSerializer(data=request_data)

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

    # SEARCH CONTACT US HERE

    def search_contact(self, request, format=None):
        """ Load contact us base on search term
        """
        try:
            limit = RECORD_PER_PAGE
            offset = int(request.GET.get("offset", "0"))
            search_term = request.GET.get("search_term", "")
            response_json = {}

            # Retrieve contact us on remote server
            response_json = fetch_document(
                collection=CONTACT_COLLECTION,
                document=CONTACT_DOCUMENT_NAME,
                fields={"contacts.search_term": {
                    "$regex": f"{search_term}", "$options": "i"}}
            )

            return response_json, status.HTTP_200_OK

        # The code below will
        # execute when error occur
        except Exception as e:
            print(f"{e}")
            return {"error_msg": f"{e}"}, status.HTTP_500_INTERNAL_SERVER_ERROR


class ContactDetail(APIView):
    def get(self, request, event_id, format=None):
        try:
            response_json = {}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            # Retrieve contact us from remote server
            response_json = fetch_document(
                collection=CONTACT_COLLECTION,
                document=CONTACT_DOCUMENT_NAME,
                fields={"eventId": event_id}
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

    def put(self, request,  event_id, format=None):
        try:
            response_json = {}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            request_data = request.data
            
            serializer = ContactSerializer(event_id, data=request_data)

            # Commit data to database
            if serializer.is_valid():
                response_json, status_code = serializer.update(event_id, serializer.validated_data)

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
