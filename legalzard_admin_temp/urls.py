from django.urls import path
import legalzard_admin_temp.views as vw



app_name = "legalzard_admin_temp"
urlpatterns = [
    path('', vw.index, name="dashboard"),
    path('licenses/', vw.licenses, name="licenses"),
    path('comparisons/', vw.comparisons, name="comparisons"),
    path('comparison-categories/<str:comparison_event_id>/', vw.comparison_categories, name="comparison_categories"),
]