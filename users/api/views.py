from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings


#from django.http import Http404
#from django.shortcuts import get_object_or_404
#from rest_framework import viewsets
#from django.conf import settings
#from rest_framework.permissions import  BasePermission
#from django.db.models import Q
      
from users.models import Users
from users.api.serializers import  UsersSerializer
      
from users.models import UserAwards
from users.api.serializers import  UserAwardsSerializer
      
class UsersDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:

      user = Users.objects.get(pk=pk)
      context = {'request': request}
      results = UsersSerializer(user, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = UsersSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      user = Users.objects.get(pk=pk)
      serializer = UsersSerializer(user, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      user = Users.objects.get(pk=pk)
      user.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class UsersList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    users = Users.objects.filter()
    users_serializer = UsersSerializer(users, many=True, context=context).data

    return Response(users_serializer)


class UserAwardsDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:

      useraward = UserAwards.objects.get(pk=pk)
      context = {'request': request}
      results = UserAwardsSerializer(useraward, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = UserAwardsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      useraward = UserAwards.objects.get(pk=pk)
      serializer = UserAwardsSerializer(useraward, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      useraward = UserAwards.objects.get(pk=pk)
      useraward.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class UserAwardsList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    userawards = UserAwards.objects.filter()
    users_serializer = UserAwardsSerializer(userawards, many=True, context=context).data

    return Response(users_serializer)


class CustomAuthToken(ObtainAuthToken):

  def post(self, request, *args, **kwargs):

    serializer = self.serializer_class(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})
