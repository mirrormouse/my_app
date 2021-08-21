
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import TimerCreateForm, SetForm,TitleForm
from django import forms
from .models import Timer

def index(request):
    params={
        'title':'time'
    }
    return render(request,'timer/index.html',params)

def timer(request,num=1):
    TimerCreateFormSet=forms.modelformset_factory(
        Timer,
        form=TimerCreateForm,
        extra=1,
    )
    params={
        'TitleForm':TitleForm(initial={'title':'Title','hour':'Hour','min':'Minute','sec':'Second','sound':'Sound'}),
        'TimerForm':TimerCreateFormSet(
            initial=[{'title':'Timer','hour':'00','min':'00','sec':'00'}],
            ),
        'num':num,
        'plus':num+1,
        'minus':num-1,
        #'args':{'title':'Timer','hour':1,'min':0,'sec':0},
    }
    if (request.method=='POST'):
        if 'clear' in request.POST:
            pass
        else:
            modelformset=forms.modelformset_factory(
                Timer,
                form=TimerCreateForm,
                extra=int(num),
            )
            formset_request=modelformset(request.POST)
            #print(formset_request.errors)
            if formset_request.is_valid():
                data=formset_request.cleaned_data
                for i in range(num+1):
                    plus_str='plus_'+str(i)
                    minus_str='minus_'+str(i)
                    change_str='change_'+str(i)
                    if plus_str in request.POST:
                        temp={'title':'Timer','hour':'00','min':'00','sec':'00'}
                        data.insert(i,temp)
                    if minus_str in request.POST and num>1:
                        del data[i-1]
                    if change_str in request.POST:
                        data[i],data[i-1]=data[i-1],data[i]

                
                for i in range (num+1):
                    try:
                        hour=data[i]['hour']
                        min=data[i]['min']
                        sec=data[i]['sec']
                        data[i]['hour']=setfig(hour)
                        data[i]['min']=setfig(min)
                        data[i]['sec']=setfig(sec)
                    except:
                        pass
                
                FormSet=forms.modelformset_factory(
                    Timer,
                    form=TimerCreateForm,
                    extra=num,
                )
                params['TimerForm']=FormSet(initial=data)
    return render(request,'timer/timer.html',params)

def setfig(num):
    num=int(num)
    #print(num)
    if(num==0):
        res='00'
    elif(num<10):
        res=str('0'+str(num))
    else:
        res=str(num)
    #print(res)
    return res





        


# Create your views here.

