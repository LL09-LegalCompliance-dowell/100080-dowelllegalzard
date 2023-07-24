from django.urls import path

from .views import (
    ComparisionList,
    ComparisionDetail
)

app_name = "license_comparison_public"
urlpatterns = [
    path('comparisons/', ComparisionList.as_view(), name="comparisons_public"),
    path('comparisons/<str:event_id>/',
         ComparisionDetail.as_view(), name="comparisons_detail_public"),
]
