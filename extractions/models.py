from django.db import models


# Create your models here.

class Extractions(models.Model):

  date = models.DateTimeField(auto_now_add=True)
  contest = models.ForeignKey(
    "contests.Contests", 
    related_name="Extractions_Contests", 
    on_delete=models.PROTECT
  )
  result = models.CharField(max_length=3, choices=(('win','winner'),('los','loser')))

  class Meta:
    managed = True
    db_table = "extractions"