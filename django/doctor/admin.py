from django.contrib import admin
from .models import Appointment, PatientInformation
# Register your models here.

admin.site.register(Appointment)
admin.site.register(PatientInformation)
