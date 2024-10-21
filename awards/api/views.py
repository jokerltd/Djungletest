from rest_framework import status
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
      
from awards.models import Awards
from awards.api.serializers import  AwardsSerializer
      
class AwardsDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:

      award = Awards.objects.get(pk=pk)
      context = {'request': request}
      results = AwardsSerializer(award, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = AwardsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      award = Awards.objects.get(pk=pk)
      serializer = AwardsSerializer(award, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      award = Awards.objects.get(pk=pk)
      award.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class AwardsList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    awards = Awards.objects.filter()
    awards_serializer = AwardsSerializer(awards, many=True, context=context).data

    return Response(awards_serializer)

