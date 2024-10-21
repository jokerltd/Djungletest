from django.db import models

# Create your models here.

from awards.models import Awards

class Contests(models.Model):

  code = models.CharField(max_length=10)
  name = models.CharField(max_length=100)
  description = models.TextField()
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  daily_awards_available = models.IntegerField(default=24)
  award = models.ForeignKey(Awards, related_name="Contests_Awards", on_delete=models.PROTECT)
  active = models.BooleanField(default=True) #Set default to False if user registration need an operator approval
  deleted = models.BooleanField(default=False)

  class Meta:

    managed = True
    db_table = "contests"
