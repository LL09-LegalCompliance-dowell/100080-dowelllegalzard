from django.urls import path
from .views import (ContactList, ContactDetail)

app_name = "contacts"
urlpatterns = [
    path('contacts/', ContactList.as_view(), name="contact_list"),
    path('contacts/<str:event_id>/', ContactDetail.as_view(), name="contact_detail")
]
