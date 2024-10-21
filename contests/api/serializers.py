from rest_framework import serializers
from django.conf import settings
from contests.models import *
    

class ContestsSerializer(serializers.ModelSerializer):

  class Meta:
    model=Contests
    fields="__all__"
      