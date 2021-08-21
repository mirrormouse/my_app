from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

SOUND=(
    ("0","終了音"),
    ("1","開始音"),
    ("2","音声なし"),
)

class Timer(models.Model):
    title=models.CharField(max_length=100,default='Timer',null=True,blank=True)
    hour = models.PositiveIntegerField(null=True,blank=True)
    min = models.PositiveIntegerField(null=True,blank=True)
    sec = models.PositiveIntegerField(null=True,blank=True)
    sound=models.CharField(choices=SOUND,max_length=100,default=0)
    def __str__(self):
        return self.title


