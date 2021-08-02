from rest_framework import serializers

from .models import hospital

class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hospital
        fields = ('id', 'name', 'location', 'contact_no', 'email', 'blood_count', 'biopsy', 'ecg', 'ct_scan', 'angiogram', 'ultra_sound', 'picture', 'description', 'password')
    
