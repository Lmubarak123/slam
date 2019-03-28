from django.db import models

# Create your models here.
class Slam(models.Model):
    fname=models.CharField(max_length=30)
    sname=models.CharField(max_length=30)
class Slam1(models.Model):
    fname = models.CharField(max_length=30)
    sname = models.CharField(max_length=30)
