from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.


class Timer(models.Model):
    title=models.CharField(max_length=100,default='Timer')
    hour = models.IntegerField()
    min = models.IntegerField(validators=[MaxValueValidator(99)])
    sec = models.IntegerField(validators=[MaxValueValidator(99)])
    def __str__(self):
        return self.title


