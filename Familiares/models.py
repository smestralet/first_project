from pyexpat import model
from django.db import models

class Familiars(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    birthday = models.CharField(max_length=30)