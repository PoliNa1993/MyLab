from django.contrib import admin
from .models import Patient, Visit

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    pass
