from rest_framework import serializers

from .models import appointment_details, test_details, video_chat

class AppoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = appointment_details
        fields = ('patient', 'doctor', 'hospital', 'date', 'time')

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = test_details
        fields = ('patient', 'test', 'hospital', 'date', 'time')        

