# from django.http import response
# from rest_framework import serializers
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from rest_framework import status

# from django.contrib.auth.models import User
# from .models import UserExtra

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
        # fields = ('id' ,'username', 'first_name', 'last_name', 'email', 'password')

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance

#     def update(self, instance, validated_data):
#         for attr, value in validated_data.items():
#             if attr == 'password':
#                 instance.set_password(value)
#             else:
#                 setattr(instance, attr, value)
#         instance.save()
#         return instance      

# class UserExSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserExtra
#         fields = ('id', 'user','contact_no')
#         lookup_field = 'user'

#     def create(self, validated_data):
#         instance = self.Meta.model(**validated_data)
#         instance.save()
#         return instance


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_tokens(sender, instance=None, created=False, **kwargs):
#     if created:
        # Token.objects.create(user=instance)

from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' ,'username', 'first_name', 'last_name', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' ,'username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], email=validated_data['email'], password=validated_data['password'])

        return user