from rest_framework import viewsets
from .serializers import AppoSerializer, TestSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import appointment_details, test_details


class AppoViewSet(viewsets.ModelViewSet):
    queryset = appointment_details.objects.all()
    serializer_class = AppoSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = test_details.objects.all()
    serializer_class = TestSerializer    