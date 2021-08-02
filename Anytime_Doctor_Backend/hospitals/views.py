from rest_framework import viewsets
from .serializers import HospitalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import hospital


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = hospital.objects.all()
    serializer_class = HospitalSerializer
