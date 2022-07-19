from django.urls import path, include
from .views import dowell_login
urlpatterns = [
    path('login/', dowell_login, name="dowell_login"),
]
