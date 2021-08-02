from rest_framework import viewsets

from .serializers import UserSerializer,UserExSerializer
from django.contrib.auth.models import User
from .models import UserExtra
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserExViewSet(viewsets.ModelViewSet):
    queryset = UserExtra.objects.all()
    serializer_class = UserExSerializer

