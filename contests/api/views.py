from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from django.conf import settings

#from django.http import Http404
#from rest_framework import viewsets
#from rest_framework.permissions import BasePermission
#from django.db.models import Q
      
from contests.models import Contests
from contests.api.serializers import  ContestsSerializer
from extractions.models import Extractions
from users.models import Users, UserAwards
import datetime
from datetime import datetime, timedelta
from django.utils import timezone
import random

class PlayView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):

    user = request.user

    try:
    
      user = Users.objects.get(user_id=user)
    
    except Users.DoesNotExist:
         
      return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    contest_code = request.query_params.get('contest', None)
    now = timezone.now()
    start_time = now.replace(minute=0, second=0, microsecond=0)
    end_time = start_time + timedelta(hours=1) - timedelta(seconds=1)
    start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = start_time + timedelta(days=1) - timedelta(seconds=1)
    response_data = {
      "data": {
        "winner": False,
        "prize": {
          "code": "NoWin",
          "name": "Sorry, you didn't win this time. Try again, you will be luckier.",
        }
      }
    }

    if contest_code is None:

      return Response({'error': "Missing contest code."}, status=status.HTTP_400_BAD_REQUEST)

    try:

      contest = Contests.objects.get(code=contest_code, start_date__lte=now.strftime('%Y-%m-%d'), end_date__gte=now.strftime('%Y-%m-%d'))
      contest = get_object_or_404(Contests, code=contest_code)

    except Contests.DoesNotExist:
  
      return Response({'error': "Contest code isn't found."}, status=status.HTTP_404_NOT_FOUND)

    daily_max_wins = Extractions.objects.filter(contest=contest,date__range=(start_time, end_time)).count()
    
    if contest.active == False:

      return Response({'error': "Contest code isn't active."}, status=status.HTTP_422_OUT_OF_DATE_RANGE)

    contest = Contests.objects.filter(code=contest_code, active=True, deleted=False).first()
    
    actual_hourly_winned_awards = Extractions.objects.filter(contest=contest,date__range=(start_time, end_time)).count()

    if actual_hourly_winned_awards >= round(contest.daily_awards_available / 24):

      response_data = {
        "data": {
          "winner": False,
          "prize": "Sorry, you didn't win this time. Try again, you will be luckier."
        }
      }

      Extractions.objects.create(
        contest = contest,
        result = 'los'
      )

    elif daily_max_wins >= contest.daily_awards_available:

      response_data = {
        "data": {
          "winner": False,
          "prize": "Sorry, you didn't win this time. Try again, you will be luckier."
        }
      }

      Extractions.objects.create(
        contest = contest,
        result = 'los'
      )

    elif random.randint(1, 100) <= settings.WINNING_PERCENTAGES:

      prize = {
        "code": contest.award.code,
        "name": contest.award.name,
      }

      response_data = {
        "data": {
          "winner": True,
          "prize": prize
        }
      }

      extraction = Extractions.objects.create(
        contest = contest,
        result = 'win'
      )

      UserAwards.objects.create(
        user = user,
        contest = contest,
        award  =contest.award,
        extractions = extraction,
      )

    else:

      Extractions.objects.create(
        contest=contest,
        result='los'
      )

    return Response({'data': response_data}, status=status.HTTP_200_OK)    


class ContestsDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:

      contest = Contests.objects.get(pk=pk)
      context = {'request': request}
      results = ContestsSerializer(contest, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = ContestsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      contest = Contests.objects.get(pk=pk)
      serializer = ContestsSerializer(contest, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      contest = Contests.objects.get(pk=pk)
      contest.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class ContestsList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    contests = Contests.objects.filter()
    contests_serializer = ContestsSerializer(contests, many=True, context=context).data

    return Response(contests_serializer)

