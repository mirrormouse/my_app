from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.
SOUND=(
    ("0","終了音"),
    ("1","開始音"),
    ("2","音声なし"),
)
def fig(i):
    i=str(i)
    if not i:
        return "00"
    if i is None:
        return "00"
    elif len(i)==0:
        return "00"
    elif len(i)==1:
        return "0"+str(i)
    else:
        return str(i)

def good_title(t):
    if not t:
        return "タイマー"
    elif len(t)==0:
        return "タイマー"
    else:
        return t


class Timer(models.Model):
    title=models.CharField(max_length=100,default='Timer',null=True,blank=True)
    hour = models.PositiveIntegerField(null=True,blank=True)
    min = models.PositiveIntegerField(null=True,blank=True)
    sec = models.PositiveIntegerField(null=True,blank=True)
    sound=models.CharField(choices=SOUND,max_length=100,default=0)
    def __str__(self):
        return str(self.id)+"_"+str(fig(self.hour))+"_"+str(fig(self.min))+"_"+str(fig(self.sec))+"_"+str(self.sound)+"_"+str(good_title(self.title))

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
