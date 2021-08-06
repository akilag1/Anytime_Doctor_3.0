from rest_framework import serializers

from .models import appointment_details, test_details, video_chat

class AppoSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment_details
        fields = ('patient_id','doctor_id', 'hospital_id', 'date', 'time')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = test_details
        fields = ('patient_id', 'test', 'hospital_id', 'date', 'time')        

