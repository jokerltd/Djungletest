from django.db import models
from django.contrib.auth.models import User

import uuid


from contests.models import Contests
from awards.models import Awards
from extractions.models import Extractions
# Create your models here.


class Users(models.Model):

  user_id = models.OneToOneField(User, related_name="Users_User", on_delete=models.PROTECT)
  token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)  
  token_creation = models.DateTimeField(auto_now=True) #This is an optional field, is needed only if we set a token time duration before expire
  contests = models.ManyToManyField(Contests, related_name="Users_Contests")
  active = models.BooleanField(default=True) #Set default to False if user registration need an operator approval
  deleted = models.BooleanField(default=False)

  class Meta:

    managed = True
    db_table = "users"


class UserAwards(models.Model):
  
  user = models.ForeignKey("Users", related_name="UserAwards_Users", on_delete=models.PROTECT)
  contest = models.ForeignKey(Contests, related_name="UserAwards_Contests", on_delete=models.PROTECT)
  award = models.ForeignKey(Awards, related_name="UserAwards_Awards", on_delete=models.PROTECT)
  extractions = models.ForeignKey(Extractions, related_name="UserAwards_Extractions", on_delete=models.PROTECT)

  class Meta:

    managed = True
    db_table = "user_awards"

