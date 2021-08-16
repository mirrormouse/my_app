
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import TimerCreateForm, SetForm
from django import forms


def index(request):
    params={
        'title':'time'
    }
    return render(request,'timer/index.html',params)

def timer(request):
    TimerCreateFormSet=forms.formset_factory(
        form=TimerCreateForm,
        extra=1,
    )
    params={
        'SetForm':SetForm(),
        'TimerForm':TimerCreateFormSet(),
        'num':"1"
    }
    if (request.method=='POST'):
        number=request.POST['number']
        num=int(number)
        if 'plus' in request.POST:
            params['num']=int(number)+1
            num=int(number)+1
        elif 'minus' in request.POST:
            params['num']=max(int(number)-1,1)
            num=max(int(number)-1,1)
        params['TimerForm']=forms.formset_factory(
            form=TimerCreateForm,
            extra=int(num),
        )
        cp=request.POST.copy()
        cp['number']=num
        request.POST=cp
        params['SetForm']=SetForm(request.POST)
    return render(request,'timer/timer.html',params)
    





        


# Create your views here.

