from django.contrib import admin

from .models import appointment_details

class ListingAdmin(admin.ModelAdmin):
    list_display=('doctor', 'hospital', 'date', 'time')

admin.site.register(appointment_details,ListingAdmin)