from django.urls import path, include
from .views import (
    dowell_login,
    SoftwareLicenseList,
    SoftwareLicenseDetail,
    SoftwareLicenseSearch,
    CheckLicenseCompatibility
)
urlpatterns = [
    path('login/', dowell_login, name="dowell_login"),
    path('licenses/', SoftwareLicenseList.as_view(), name="license"),
    path('licenses/search/', SoftwareLicenseSearch.as_view(), name="license_search"),
    path('licenses/check-compatibility/', CheckLicenseCompatibility.as_view(), name="license_compatibility"),
    path('licenses/<str:license_id>/', SoftwareLicenseDetail.as_view(), name="license_detail"),
]
