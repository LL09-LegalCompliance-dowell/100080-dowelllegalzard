from django.urls import path
from .views import legalzard_webhook


app_name = "github_webhook"
urlpatterns = [
    path('legalzard/', legalzard_webhook, name="legalzard_webhook"),
]