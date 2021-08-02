from rest_framework import serializers

from .models import doctor

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = doctor
        fields = ('id','name', 'speciality', 'hospital_id', 'email', 'picture', 'description', 'password','available_online', 'available_person')
    
