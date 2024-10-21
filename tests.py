from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from django.contrib.auth.models import User

from contests.models import Contests
from extractions.models import Extractions
from awards.models import Awards
from users.models import Users

import uuid

class ContestsModelTest(TestCase):

  def setUp(self):
  
    self.award = Awards.objects.create(
      code='AWD001',
      name='First Prize',
      active=True,
      deleted=False
    )
    
    self.contest = Contests.objects.create(
      code='CON001',
      name='Contest 1',
      description='A sample contest',
      start_date=timezone.now(),
      end_date=timezone.now() + timezone.timedelta(days=10),
      daily_awards_available=10,
      award=self.award,
      active=True,
      deleted=False
    )

def test_contest_creation(self):

  self.assertEqual(self.contest.code, 'CON001')
  self.assertEqual(self.contest.name, 'Contest 1')
  self.assertEqual(self.contest.daily_awards_available, 10)
  self.assertEqual(self.contest.award, self.award)

class ExtractionsModelTest(TestCase):

  def setUp(self):

    self.award = Awards.objects.create(
      code='AWD002',
      name='Second Prize',
      active=True,
      deleted=False
    )

    self.contest = Contests.objects.create(
      code='CON002',
      name='Contest 2',
      description='Another sample contest',
      start_date=timezone.now(),
      end_date=timezone.now() + timezone.timedelta(days=10),
      daily_awards_available=15,
      award=self.award,
      active=True,
      deleted=False
    )

    self.user = User.objects.create_user(
      username='testuser',
      password='password'
    )

    self.user_profile = Users.objects.create(
      user_id=self.user,
      token=uuid.uuid4(),
      active=True,
      deleted=False
    )

    self.extraction = Extractions.objects.create(
      contest=self.contest,
      winner=self.user_profile
    )

  def test_extraction_creation(self):

    self.assertEqual(self.extraction.contest, self.contest)
    self.assertEqual(self.extraction.winner, self.user_profile)

class AwardsModelTest(TestCase):

  def setUp(self):

    self.award = Awards.objects.create(
      code='AWD003',
      name='Third Prize',
      active=True,
      deleted=False
    )

    def test_award_creation(self):

      self.assertEqual(self.award.code, 'AWD003')
      self.assertEqual(self.award.name, 'Third Prize')
      self.assertTrue(self.award.active)

class UsersModelTest(TestCase):

  def setUp(self):

    self.user = User.objects.create_user(
      username='user1',
      password='password'
    )

    self.award = Awards.objects.create(
      code='AWD004',
      name='Fourth Prize',
      active=True,
      deleted=False
    )

    self.contest = Contests.objects.create(
      code='CON004',
      name='Contest 4',
      description='Yet another contest',
      start_date=timezone.now(),
      end_date=timezone.now() + timezone.timedelta(days=5),
      daily_awards_available=20,
      award=self.award,
      active=True,
      deleted=False
    )

    self.user_profile = Users.objects.create(
      user_id=self.user,
      token=uuid.uuid4(),
      active=True,
      deleted=False
    )

    self.user_profile.contests.add(self.contest)

  def test_user_creation(self):

    self.assertEqual(self.user_profile.user_id, self.user)
    self.assertTrue(self.user_profile.active)
    self.assertIn(self.contest, self.user_profile.contests.all())
