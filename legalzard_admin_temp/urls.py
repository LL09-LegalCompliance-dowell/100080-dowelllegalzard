from django.urls import path
import legalzard_admin_temp.views as vw



app_name = "legalzard_admin_temp"
urlpatterns = [
    path('', vw.index, name="dashboard"),
    path('licenses/', vw.licenses, name="licenses"),
    path('license-add/', vw.add_license, name="license_add"),
    path('license-edit/', vw.update_license, name="license_edit"),
    path('comparisons/', vw.comparisons, name="comparisons"),
    path('comparison-categories/<str:comparison_event_id>/', vw.comparison_categories, name="comparison_categories"),
]