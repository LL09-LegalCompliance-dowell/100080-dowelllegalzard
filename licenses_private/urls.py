from django.urls import path
from .views import (
    SoftwareLicenseList,
    SoftwareLicenseDetail
)

app_name = "licenses_experienced"

urlpatterns = [
    path('licenses/', SoftwareLicenseList.as_view(), name="licenses"),
    path('licenses/<str:event_id>/',
         SoftwareLicenseDetail.as_view(), name="license_detail"),
]
