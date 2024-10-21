from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.conf import settings

from contests.models import Contests

import requests

class Command(BaseCommand):
  help = 'Make some extractions for each contest'

  def handle(self, *args, **options):

    for contest in Contests.objects.all():

      print(f"\n\nCODE: {contest.code}\n")
      for extraction in range(0, (round(contest.daily_awards_available / 24) * 100)):

        response = requests.get(f"http://localhost:8100/api/play/?contest={contest.code}") 
        print(f"{contest.code}: {response.text}")

