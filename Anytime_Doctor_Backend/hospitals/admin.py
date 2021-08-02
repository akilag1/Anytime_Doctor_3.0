from django.contrib import admin

from django.contrib import admin

from .models import hospital

class ListingAdmin(admin.ModelAdmin):
    list_display=("name","location","ecg","blood_count","biopsy","angiogram","ct_scan","ultra_sound", "password")

admin.site.register(hospital,ListingAdmin)
