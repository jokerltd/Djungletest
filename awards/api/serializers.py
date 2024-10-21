from rest_framework import serializers
from django.conf import settings
from awards.models import *
    

class AwardsSerializer(serializers.ModelSerializer):

  class Meta:
    model=Awards
    fields="__all__"
      