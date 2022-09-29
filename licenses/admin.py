from django.contrib import admin
from .models import SoftwareLicense, SoftwareLicenseAgreement
# Register your models here.
admin.site.register(SoftwareLicense)
admin.site.register(SoftwareLicenseAgreement)