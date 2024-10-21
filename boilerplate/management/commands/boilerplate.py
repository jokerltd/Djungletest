from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.conf import settings

from re import search 
import os
from pathlib import Path

class Command(BaseCommand):
  help = 'Create boilerplating APIView'

  def handle(self, *args, **options):

    files_list = ['views.py', 'urls.py', 'serializers.py']
    
    applications = [app for app in apps.get_app_configs() if not any(app.name.find(value) > -1 for value in ['django', 'rest', 'boilerplate'])]

    app_models = {}

    for application in applications:

      app_path = settings.BASE_DIR

      app_path = os.path.join(app_path, application.name+"/api")

      if not os.path.exists(app_path):

        os.makedirs(app_path)

      for file_name in files_list:

        file_name = os.path.join(app_path, file_name)
        file1 = open(file_name, "w")
        file1.close()

      app_models[application.name] = [model.__name__ for model in application.get_models() if not any(model.__name__.find(value) > -1 for value in ['LogEntry', 'Permission', 'Group', 'ContentType', 'Session'])]
      print(f"app_models application.name {app_models[application.name]}")

    for app in app_models:

      self.generate_urls(app_models, app)

    for app in app_models:

      self.generate_serializers(app_models, app)

    for app in app_models:

      self.generate_views_imports(app_models, app)
      self.generate_views(app_models, app)

    print("That's all folks!")

  def generate_urls(self, app_models, app):

    urls = f"""from django.urls import include, path
from rest_framework.routers import DefaultRouter
from {app}.api import views

router=DefaultRouter()

urlpatterns = [
"""

    #read model and generate base urls for each Class of the model
    for model_class in app_models[app]:

      urls += f'  path("{app}/{model_class}Detail/<int:pk>/", views.{model_class}DetailView.as_view(), name="{model_class.lower()}-details"),\n'
      urls += f'  path("{app}/{model_class}Detail/", views.{model_class}DetailView.as_view(), name="{model_class.lower()}-details"),\n'
      urls += f'  path("{app}/{model_class}List/", views.{model_class}List.as_view(), name="{model_class.lower()}-list"),\n'

    urls += "]"

    with open(f"{app}/api/urls.py", "w") as urls_py:

      urls_py.write(urls)
      print(f"urls {urls}")

  def generate_serializers(self, app_models, app):

    serializers = f"""from rest_framework import serializers
from django.conf import settings
from {app}.models import *
    """

    for model_class in app_models[app]:

      serializers += f"""

class {model_class}Serializer(serializers.ModelSerializer):

  class Meta:
    model={model_class}
    fields="__all__"
      """

    with open(f"{app}/api/serializers.py", "w") as serializers_py:

      serializers_py.write(serializers)
      print(f"serializers {serializers}")

  def generate_views_imports(self, app_models, app):

    with open(f"{app}/api/views.py", "w") as views_py:

      views_py.write('')

    views = f"""from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework import status

#from django.http import Http404
#from django.shortcuts import get_object_or_404
#from rest_framework import viewsets
#from django.conf import settings
#from rest_framework.permissions import  BasePermission
#from django.db.models import Q
      """

    for model_class in app_models[app]:

      views += f"""
from {app}.models import {model_class}
from {app}.api.serializers import  {model_class}Serializer
      """

    with open(f"{app}/api/views.py", "a") as views_py:

      views_py.write(views)
      print(f"views {views}")

  def generate_views(self, app_models, app):

    for model_class in app_models[app]:

      app_s = model_class[:-1].lower()
        
      if model_class[-3:] == 'ies':
      
        app_s = f"{model_class[:-3]}y".lower()

      views = f"""
class {model_class}DetailView(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:

      {app_s} = {model_class}.objects.get(pk=pk)
      context = {{'request': request}}
      results = {model_class}Serializer({app_s}, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = {model_class}Serializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      {app_s} = {model_class}.objects.get(pk=pk)
      serializer = {model_class}Serializer({app_s}, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      {app_s} = {model_class}.objects.get(pk=pk)
      {app_s}.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class {model_class}List(APIView):
  permission_classes = []

  def get(self, request):

    context = {{'request': request}}
    {model_class.lower()} = {model_class}.objects.filter()
    {app}_serializer = {model_class}Serializer({model_class.lower()}, many=True, context=context).data

    return Response({app}_serializer)

"""

      with open(f"{app}/api/views.py", "a") as views_py:

        views_py.write(views)
        print(f"views {views}")
