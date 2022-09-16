from rest_framework import serializers, status
from utils.dowell import (
    fetch_document,
    save_document,
    update_document,

    CONTACT_COLLECTION,
    CONTACT_DOCUMENT_NAME,
    CONTACT_KEY,

)


class ContactSerializer(serializers.Serializer):
    """ Create and update contact us
        eg.
        {
            "first_name": "sample",
            "last_name": "sample 1",
            "email": "sample@sample.com",
            "phone_number":"000-000-0000",
            "message": "sample message",
            "search_term": "sample sample 1-sample@sample.com-000-000-0000"
        }
    """
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=50)
    message = serializers.CharField(max_length=5000)

    def create(self, validated_data):
        response_json = {}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        # Create contact on remote server
        search_term = f"{validated_data['first_name']} {validated_data['first_name']}-"
        search_term += f"{validated_data['email']} {validated_data['phone_number']}"
        validated_data['search_term'] = search_term

        print(validated_data)
        response_json = save_document(
            collection=CONTACT_COLLECTION,
            document=CONTACT_DOCUMENT_NAME,
            key=CONTACT_KEY,
            value=validated_data
        )

        if response_json["isSuccess"]:
            status_code = 201
            # Retrieve contact from remote server
            response_json = fetch_document(
                collection=CONTACT_COLLECTION,
                document=CONTACT_DOCUMENT_NAME,
                fields={
                    "eventId": response_json["event_id"]
                }
            )
        return response_json, status_code

    def update(self, event_id, validated_data):

        # # Update contact on remote server
        search_term = f"{validated_data['first_name']} {validated_data['first_name']}-"
        search_term += f"{validated_data['email']} {validated_data['phone_number']}"
        validated_data['search_term'] = search_term
        response_json = update_document(
            collection=CONTACT_COLLECTION,
            document=CONTACT_DOCUMENT_NAME,
            key=CONTACT_KEY,
            new_value=validated_data,
            event_id=event_id
        )

        if response_json["isSuccess"]:
            status_code = 200
            # Retrieve contact on remote server
            response_json = fetch_document(
                collection=CONTACT_COLLECTION,
                document=CONTACT_DOCUMENT_NAME,
                fields={"eventId": event_id}
            )

        return response_json, status_code
