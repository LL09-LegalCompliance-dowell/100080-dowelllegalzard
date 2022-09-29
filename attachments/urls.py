from django.urls import path
from .views import (AttachmentList)

app_name = "attachments"
urlpatterns = [
    path('attachments/', AttachmentList.as_view(), name="attachment_list")
]
