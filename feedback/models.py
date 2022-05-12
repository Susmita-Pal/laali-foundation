from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Rating(models.Model):
    rating=models.IntegerField(default=0)
    text=models.TextField(default=""),
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ]

def __str__(self):
    return str(self.pk)