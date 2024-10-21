from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import User

from extractions.models import Extractions
from awards.models import Awards
from contests.models import Contests
from users.models import Users

from faker import Faker
from random import randint
from datetime import date, datetime
from django.utils import timezone
import uuid

class Command(BaseCommand):
  help = 'Extract awards of contests active today and assign to the relative winner'

  def handle(self, *args, **options):

    fake = Faker()

    """
    for index in range(1,4):

      award = Awards.objects.create(
        name = "Sconto del 5%",
        code = "five-percent-discount",
        active = True,
        deleted = False,
      )

      contest = Contests.objects.create(
        code = f"CONTEST00{index}",
        name = f"Super Contest 00{index}",
        description = f"The 00{index} contest.",
        start_date = fake.date_between_dates(date_start=datetime(year=2024, month=1, day=1),date_end=datetime(year=2024, month=12, day=31)),
        end_date=timezone.now() + timezone.timedelta(days=90),
        daily_awards_available=20,
        award=award,
        active=True,
        deleted=False
    )
    """
    contests = Contests.objects.all()

    for index in range(1,50):

      user = User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password="testpassword99!",
      )

      user_profile = Users.objects.create(
        user_id=user,  # ForeignKey to the created User
        token=uuid.uuid4(),
        active=True,   # or fake.boolean() for random active status
        deleted=False
      )      

      """
      if contests.exists():
      
        random_contests = fake.random_elements(elements=contests, length=3)
        user_profile.contests.add(*random_contests)
      """
