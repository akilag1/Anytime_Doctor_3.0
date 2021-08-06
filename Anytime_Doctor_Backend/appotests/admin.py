from django.contrib import admin

from .models import appointment_details

class ListingAdmin(admin.ModelAdmin):
    list_display=('patient_id','doctor_id', 'hospital_id', 'date', 'time')

admin.site.register(appointment_details,ListingAdmin)