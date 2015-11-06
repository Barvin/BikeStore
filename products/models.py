from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500, null=False, unique=True)
    time_added = models.DateTimeField(default=datetime.datetime.now())
    image = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    price = models.FloatField(max_length=10, null=False, default=0)
    sold = models.NullBooleanField(null=True, blank=True)
    delete = models.NullBooleanField(null=True, blank=True)
