from rest_framework import viewsets
from .serializers import DoctorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import doctor


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = doctor.objects.all()
    serializer_class = DoctorSerializer
