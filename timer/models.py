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
        return str(self.id)+"_"+str(self.hour)+"_"+str(self.min)+"_"+str(self.sec)+"_"+str(self.sound)+"_"+str(self.title)

class HomeTimer(models.Model):
    title=models.CharField(max_length=100,default='Timer',null=True,blank=True)
    hour = models.PositiveIntegerField(null=True,blank=True)
    min = models.PositiveIntegerField(null=True,blank=True)
    sec = models.PositiveIntegerField(null=True,blank=True)
    sound=models.CharField(choices=SOUND,max_length=100,default=0)
    def __str__(self):
        return str(self.id)

class TimerSet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,default='タイトル',null=True,blank=True)
    set=models.CharField(max_length=1000000,default="")
    def __str__(self):
        return str(self.id)+" "+str(self.set)+" "+str(self.title)
