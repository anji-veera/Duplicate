from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    eligibility = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class BangaloreJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    eligibility = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    eligibility = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
