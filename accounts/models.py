from django.db import models

# Create your models here.
from django import forms


class Reg(models.Model):
    name=models.CharField(max_length=70)
    username=models.CharField(max_length=30)
    designation=models.CharField(max_length=20)
    email=models.EmailField(max_length=200)
    gender=models.CharField(max_length=10)
    password= models.CharField(max_length=50)
    confirm_password= models.CharField(max_length=50)