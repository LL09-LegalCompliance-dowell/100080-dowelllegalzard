from django.urls import path

from .views import (
    ComparisionList,
    ComparisionDetail
)

app_name = "license_comparision"
urlpatterns = [
    path('comparisons/', ComparisionList.as_view(), name="comparisons"),
    path('comparisons/<str:event_id>/',
         ComparisionDetail.as_view(), name="comparisons_detail"),
]
