from django.urls import path
from .views import (
    dowell_login,
    SoftwareLicenseList,
    SoftwareLicenseDetail,
    SoftwareLicenseAgreementList,
    SoftwareLicenseAgreementDetail
)


urlpatterns = [
    path('login/', dowell_login, name="dowell_login"),
    path('licenses/', SoftwareLicenseList.as_view(), name="licenses"),
    path('licenses/<str:license_id>/', SoftwareLicenseDetail.as_view(), name="license_detail"),
    path('agreements/', SoftwareLicenseAgreementList.as_view(), name="agreements"),
    path('agreements/<str:agreement_id>/', SoftwareLicenseAgreementDetail.as_view(), name="agreement_detail"),
]
