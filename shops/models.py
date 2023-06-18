# Create your models here.
from django.contrib.gis.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(geography=True, null=False)
    address = models.TextField()
    city = models.CharField(max_length=50)