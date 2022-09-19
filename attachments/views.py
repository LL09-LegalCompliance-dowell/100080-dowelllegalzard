from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from storage.upload import upload_img


class AttachmentList(APIView):
    """Save images to filesystem
    """

    def post(self, request, format=None):
        try:
            file = request.FILES['file']

            # save file to file system
            data = upload_img(file)

            return Response({
                "isSuccess": True,
                "file_data": data['file_data']
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(str(e))
            return Response({
                "isSuccess": False,
                "message": "Internal Server Error"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
