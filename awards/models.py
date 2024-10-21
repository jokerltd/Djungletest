from django.db import models

# Create your models here.

class Awards(models.Model):

  code = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  active = models.BooleanField(default=True) #Set default to False if user registration need an operator approval
  deleted = models.BooleanField(default=False)

  class Meta:

    managed = True
    db_table = "awards"
