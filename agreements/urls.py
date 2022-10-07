from django.urls import path
from .views import (
    AgreementComplianceList,
    AgreementComplianceDetail
)

app_name = "agreements"
urlpatterns = [
    path('agreements/', AgreementComplianceList.as_view(), name="agreements"),
    path('agreements/<str:event_id>/',
         AgreementComplianceDetail.as_view(), name="agreement_detail"),
]
