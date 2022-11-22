from django.urls import path

from .views import (
    ComparisionList,
    ComparisionDetail
)

app_name = "license_comparision"
urlpatterns = [
    path('comparisions/', ComparisionList.as_view(), name="comparisions"),
    path('comparisions/<str:event_id>/',
         ComparisionDetail.as_view(), name="comparision_detail"),
]
