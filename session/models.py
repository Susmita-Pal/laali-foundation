from django.db import models

# Create your models here.
from django import forms


class Session_det(models.Model):
    link=models.URLField()
    title=models.CharField(max_length=200)
    datee=models.CharField(max_length=30)
    timee=models.CharField(max_length=10)
    class Sess (models.IntegerChoices):
        STUDENT= 1
        MENTOR = 2
        COLLABORATOR = 3
        ADMIN = 4
    sessby = models.IntegerField(choices=Sess.choices)