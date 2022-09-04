from django.urls import path
from .views import (
    CommonAttributeList,
    CommonAttributeDetail,
    AttributeList,
    AttributeDetail
)

app_name = "attributes"

urlpatterns = [
    path('commonattributes/', CommonAttributeList.as_view(),
         name="common_attributes"),
    path('commonattributes/<str:event_id>/',
         CommonAttributeDetail.as_view(), name="common_attribute_detail"),
    path('attributes/', AttributeList.as_view(), name="attributes"),
    path('attributes/<str:event_id>/',
         AttributeDetail.as_view(), name="attribute_detail")
]
