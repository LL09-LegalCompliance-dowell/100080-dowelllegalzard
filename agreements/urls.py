from django.urls import path
from .views import (
    SoftwareAgreementList,
    SoftwareAgreementDetail
)

app_name = "agreements"
urlpatterns = [
    path('agreements/', SoftwareAgreementList.as_view(), name="agreements"),
    path('agreements/<str:agreement_id>/',
         SoftwareAgreementDetail.as_view(), name="agreement_detail"),
]
