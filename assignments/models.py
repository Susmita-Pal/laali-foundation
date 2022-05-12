from django.db import models

# Create your models here.
class CreateAssgn(models.Model):
    ansRad=models.CharField(max_length=10)
    ansCheck=models.CharField(max_length=10)
    ansTextArea=models.CharField(max_length=300)
    score=models.IntegerField()