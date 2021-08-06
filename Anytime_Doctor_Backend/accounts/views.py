# from rest_framework import viewsets

# from .serializers import UserSerializer,UserExSerializer
# from django.contrib.auth.models import User
# from .models import UserExtra
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import Http404
# from rest_framework.authtoken.models import Token

# from accounts import serializers


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def login(request):
#         if request.method == "POST":
#             email=request.POST["email"]
#             password=request.POST["pass"]
#             user=auth.authenticate(username=email,password=password)

#             if user is not None:
#                 token=Token.objects.get(user).key
#                 return token
#             else:
#                 messages.error(request,"Invalid Credentials")
#                 return redirect("login")    

#         else:    
#             return render(request,"accounts/login.html")

# class UserExViewSet(viewsets.ModelViewSet):
#     queryset = UserExtra.objects.all()
#     serializer_class = UserExSerializer

# # @api_view(['POST',])
# # def register_view(request):
# #     if request.method=='POST':
# #         serializer=UserSerializer(data=request.data)
# #         data={}
# #         if serializer.is_valid:
# #             instance=serializer.save()
# #             data['response']="Sussesfull"
# #             data['id']=instance.id
# #             data['username']=instance.username
# #             data['first_name']=instance.first_name
# #             data['last_name']=instance.last_name
# #             data['email']=instance.email
# #             data['password']=instance.password
#             # token=Token.objects.get(user=instance).key
# #             data['token']=token
# #         else:
# #             data=serializer.errors
# #         return Response(data)        

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_id_main=user.id
        login(request, user)
        # return super(LoginAPI, self).post(request, format=None)
        temp_list=super(LoginAPI, self).post(request, format=None)
        temp_list.data["user_id"]=user_id_main
        return Response({"data":temp_list.data})