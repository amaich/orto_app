from django.db import models

# Create your models here.


class Clients(models.Model):
    fullname = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.CharField(max_length=150, blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
