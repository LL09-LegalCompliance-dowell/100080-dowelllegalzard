from django.urls import path
from .views import (
    SoftwareLicenseList,
    SoftwareLicenseDetail
)

app_name = "licenses_public"
urlpatterns = [
    path('licenses/', SoftwareLicenseList.as_view(), name="licenses_public"),
    path('licenses/<str:event_id>/',
         SoftwareLicenseDetail.as_view(), name="license_detail_public"),
]
