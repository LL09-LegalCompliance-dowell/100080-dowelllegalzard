from django.urls import path
from .views import (
    dowell_login,
    SoftwareLicenseList,
    SoftwareLicenseDetail
)
urlpatterns = [
    path('login/', dowell_login, name="dowell_login"),
    path('licenses/', SoftwareLicenseList.as_view(), name="software_license"),
    path('licenses/<str:license_id>/', SoftwareLicenseDetail.as_view(), name="software_license_detail"),
]
