from rest_framework import serializers
from django.conf import settings
from users.models import *
    

class UsersSerializer(serializers.ModelSerializer):

  class Meta:
    model=Users
    fields="__all__"
      

class UserAwardsSerializer(serializers.ModelSerializer):

  class Meta:
    model=UserAwards
    fields="__all__"
      