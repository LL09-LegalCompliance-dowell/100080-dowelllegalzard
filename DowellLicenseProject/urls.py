"""DowellLicenseProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings
from agreements.views import load_public_agreement_compliance, index, download_file, health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('licenses.urls')),
    path('api/public/', include('licenses_public.urls')),
    path('api/private/', include('licenses_private.urls')),
    path('api/experienced/', include('licenses_experienced.urls')),
    path('api/', include('agreements.urls')),
    path('api/', include('attributes.urls')),
    path('api/', include('attachments.urls')),
    path('api/', include('contacts.urls')),
    path('api/', include('license_comparision.urls')),
    path('api/', include('github_webhook.urls')),
    path('api/public/', include('license_comparison_public.urls')),
    path('agreement-compliance/<str:event_id>/', load_public_agreement_compliance, name= "load_public_agreement_compliance"),
    path('download/', download_file, name="agreements_download"),
    path('temp-admin/', include('legalzard_admin_temp.urls')),
    path('', health_check.as_view(), name="index")
]\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)