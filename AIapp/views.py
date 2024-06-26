from django.shortcuts import render
from django.http import HttpResponse
from tensorflow.keras.models import load_model
import numpy as np 
from .forms import AdderForm
# Create your views here.
model = load_model("AIapp/model/my_model.h5")

def makedata(l):
  res=[]
  for num in l:
    data=[0]
    val=num
    for i in range(5):
      data.append(val%10)
      val=val//10
    res.append(data)
  return res

def bound(a,b):
  res=[]
  for i,j in zip(a,b):
    res.append([i,j])
  return res

def calc(a,b):
    x=[a]
    y=[b]
    partx=makedata(x)
    party=makedata(y)
    train=np.array(bound(partx,party))
    ans=x+y
    z=makedata(ans)
    label=np.array(z)
    train=train.transpose(0, 2, 1)
    result=model.predict(train)
    result=result.flatten().astype(np.uint8)
    res=""
    flag=False
    for i in range(5):
        if (not flag) and (result[5-i]!=0):
            flag=True
        if flag:
            res+=str(result[5-i])
    return str(a)+'+'+str(b)+'='+str(res), str(a)+'+'+str(b)+'='+str(a+b)

def index(request):
    return HttpResponse("This is top page")

def adder(request):
    params={
        'title':'足し算ができるAI',
        'form':AdderForm(),
        'ans':'',
        'trueans':'',
    }
    if (request.method=='POST'):
        params['form']=AdderForm(request.POST)
        params['ans'],params['trueans']=calc(int(request.POST['num1']),int(request.POST['num2']))
    return render(request,'AIapp/adder.html',params)