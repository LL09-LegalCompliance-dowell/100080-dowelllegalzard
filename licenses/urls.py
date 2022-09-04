from django.urls import path
from .views import (
    dowell_login,
    SoftwareLicenseList,
    SoftwareLicenseDetail
)

app_name = "licenses"
urlpatterns = [
    path('login/', dowell_login, name="dowell_login"),
    path('licenses/', SoftwareLicenseList.as_view(), name="licenses"),
    path('licenses/<str:event_id>/',
         SoftwareLicenseDetail.as_view(), name="license_detail"),
]
