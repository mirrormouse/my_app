
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import TimerCreateForm, SetForm, TitleForm, UserCreateForm, LoginForm,TimerSetForm,HomeTimerCreateForm
from .forms import TimerSelectForm
from django import forms
from .models import Timer,TimerSet,HomeTimer
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from urllib.parse import urlencode

@login_required(login_url='/timer/login')
def index_redirect(request):
    return redirect(to='/timer/1')

def get_timer(timer_id):
    obj=TimerSet.objects.filter(id=timer_id)
    obj=str(obj)
    #print(obj)
    obj_list=obj.split(" ",4)
    timer_set=obj_list[3]
    timer_title=obj_list[4]
    timer_title=timer_title[:-3]
    #print(obj_list)
    setid_list=timer_set.split("_",-1)
    data=[]
    del setid_list[-1]
    #print(setid_list)
    cnt=0
    for val in setid_list:
        val=int(val)
        #print(val)
        cnt+=1
        timer_obj=Timer.objects.filter(id=val)
        timer_obj_list=str(timer_obj).split("_",5)
        obj_hour=timer_obj_list[1]
        obj_min=timer_obj_list[2]
        obj_sec=timer_obj_list[3]
        obj_sound=timer_obj_list[4]
        obj_title=timer_obj_list[5]
        temp={'title':obj_title[:-3],'hour':obj_hour,'min':obj_min,'sec':obj_sec,'sound':obj_sound}
        data.append(temp)
        #print(data)
    return data, cnt, timer_title

@login_required(login_url='/timer/login')
def use_redirect(request):
    params={
        'TimerSelectForm':TimerSelectForm(request.user)
    }
    return render(request,'timer/use_menu.html',params)

@login_required(login_url='/timer/login')
def use(request):
    TimerCreateFormSet=forms.modelformset_factory(
        Timer,
        form=TimerCreateForm,
        extra=1,
    )
    params={
        'TitleForm':TitleForm(initial={'title':'Title','hour':'時','min':'分','sec':'秒','sound':'Sound'}),
        'TimerForm':TimerCreateFormSet(
            initial=[{'title':'Timer','hour':'00','min':'00','sec':'00'}],
            ),
        'num':1,
        'plus':2,
        'minus':0,
        'ids':0,
        'title':'',
        'TimerSelectForm':TimerSelectForm(request.user),
        #'args':{'title':'Timer','hour':1,'min':0,'sec':0},
    }
    if (request.method=='POST'):
        print(request.POST)
        if 'clear' in request.POST:
            pass
        elif 'choice' in request.POST:
            timer_id=request.POST['groups']
            data,cnt,timer_title=get_timer(timer_id)
            params['title']=timer_title
            modelformset=forms.modelformset_factory(
                Timer,
                form=TimerCreateForm,
                extra=cnt,
            )
            params['num']=cnt
            params['plus']=cnt+1
            params['minus']=cnt-1
            formset_request=modelformset(queryset=Timer.objects.none(),initial=data)
            #print(formset_request.errors)
            params['TimerForm']=formset_request
            params['title']=timer_title
            id=int(timer_id)
            timerselect=TimerSelectForm(request.user,initial={'groups':id})
            params['TimerSelectForm']=timerselect
        return render(request,'timer/use.html',params)
    else:
        try:
            data,cnt,timer_title=get_timer(1)
            modelformset=forms.modelformset_factory(
                Timer,
                form=TimerCreateForm,
                extra=cnt,
            )
            formset_request=modelformset(queryset=Timer.objects.none(),initial=data)
            #print(formset_request.errors)
            params['TimerForm']=formset_request
            params['num']=cnt
            params['plus']=cnt+1
            params['minus']=cnt-1
            params['title']=timer_title
            return render(request,'timer/use.html',params)
        except:
            return render(request,'timer/use_menu.html',params)


@login_required(login_url='/timer/login')
def edit_redirect(request):
    try:
        try:
            id=request.POST['groups']
        except:
            obj=TimerSet.objects.all().first()
            obj_list=str(obj).split(" ",2)
            #print(obj_list)
            id=int(obj_list[0])
        
        #print("good")
        data,cnt,timer_title=get_timer(id)
        ur='/timer/edit/'+str(id)+'/'+str(cnt)
        return redirect(to=ur)
    except:
        return redirect(to='/timer/use_redirect')

@login_required(login_url='/timer/login')
def edit(request,id,num):
    TimerCreateFormSet=forms.modelformset_factory(
        Timer,
        form=TimerCreateForm,
        extra=num
    )
    old_data,cnt,timer_title=get_timer(id)
    params={
        'TimerSetForm':TimerSetForm(initial={'title':timer_title}),
        'TitleForm':TitleForm(initial={'title':'Title','hour':'時','min':'分','sec':'秒','sound':'Sound'}),
        'TimerForm':TimerCreateFormSet(
            initial=[{'title':'Timer','hour':'00','min':'00','sec':'00'}],
            ),
        'num':num,
        'plus':num+1,
        'minus':num-1,
        'id':id,
        'title':'',
        'test':'OK',
        'TimerSelectForm':TimerSelectForm(request.user),
        #'args':{'title':'Timer','hour':1,'min':0,'sec':0},
    }


    if(request.method=='POST'):
        if 'save' in request.POST:
            old_set=TimerSet.objects.filter(id=id)
            old_set.delete()
            modelformset=forms.modelformset_factory(
                Timer,
                form=TimerCreateForm,
                extra=0,
            )
            formset_request=modelformset(request.POST,queryset=Timer.objects.none())
            formset_request.save()
            data=formset_request.cleaned_data
            #print(data)
            setstring=""
            for i in range(num):
                obj=Timer.objects.filter(title=data[i]['title'])\
                                .filter(hour=data[i]['hour'])\
                                .filter(min=data[i]['min'])\
                                .filter(sec=data[i]['sec'])\
                                .filter(sound=data[i]['sound']).first()
                obj_list=str(obj).split("_",-1)
                setstring+=str(obj_list[0])+"_"
            print(setstring)
            maintitle=request.POST['title']
            #print(request.user)
            #print(maintitle)
            TimerObject=TimerSet(user=request.user,title=maintitle,set=setstring)
            TimerObject.save()
            params['data']=data
            params['TimerForm']=formset_request
            return redirect(to='/timer/use')
        else:
            modelformset=forms.modelformset_factory(
                Timer,
                form=TimerCreateForm,
                extra=0,
            )
            #print(request.POST)
            formset_request=modelformset(request.POST,queryset=Timer.objects.none())
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
                formset=FormSet(queryset=Timer.objects.none(),initial=data)
                params['TimerForm']=formset
        return render(request,'timer/edit.html',params)
    modelformset=forms.modelformset_factory(
        Timer,
        form=TimerCreateForm,
        extra=cnt,
    )
    timerselect=TimerSelectForm(request.user,initial={'groups':id})
    params['TimerSelectForm']=timerselect
    formset_request=modelformset(queryset=Timer.objects.none(),initial=old_data)
    params['TimerForm']=formset_request
    #print(formset_request.errors)
    params['num']=cnt
    params['plus']=cnt+1
    params['minus']=cnt-1
    params['title']=timer_title
    return render(request,'timer/edit.html',params)

#    except:
#        return redirect(to='/timer/use_redirect')

@login_required(login_url='/timer/login')
def index(request,num=1):
    TimerCreateFormSet=forms.modelformset_factory(
        Timer,
        form=TimerCreateForm,
        extra=1,
    )
    if(num>=10000):
        plus=num
    else:
        plus=num+1
    params={
        'TimerSetForm':TimerSetForm(),
        'TitleForm':TitleForm(initial={'title':'Title','hour':'時','min':'分','sec':'秒','sound':'Sound'}),
        'TimerForm':TimerCreateFormSet(queryset=Timer.objects.none(),
            initial=[{'title':'Timer','hour':'00','min':'00','sec':'00'}],
            ),
        'num':num,
        'plus':plus,
        'minus':num-1,
        'data':[],
        #'args':{'title':'Timer','hour':1,'min':0,'sec':0},
    }
    if (request.method=='POST'):
        if 'clear' in request.POST:
            pass
        elif 'save' in request.POST:
            modelformset=forms.modelformset_factory(
                Timer,
                form=TimerCreateForm,
                extra=0,
            )
            formset_request=modelformset(request.POST,queryset=Timer.objects.none())
            formset_request.save()
            data=formset_request.cleaned_data
            setstring=""
            for i in range(num):
                obj=Timer.objects.filter(title=data[i]['title'])\
                                .filter(hour=data[i]['hour'])\
                                .filter(min=data[i]['min'])\
                                .filter(sec=data[i]['sec'])\
                                .filter(sound=data[i]['sound']).first()
                obj_list=str(obj).split("_",-1)
                setstring+=str(obj_list[0])+"_"
            print(setstring)
            maintitle=request.POST['title']
            #print(request.user)
            #print(maintitle)
            TimerObject=TimerSet(user=request.user,title=maintitle,set=setstring)
            TimerObject.save()
            params['data']=data
            params['TimerForm']=formset_request
            return redirect(to='/timer/use')
        else:
            maintitle=request.POST['title']
            params['TimerSetForm']=TimerSetForm(initial={'title':maintitle})
            modelformset=forms.modelformset_factory(
                Timer,
                form=TimerCreateForm,
                extra=0,
            )
            #print(request.POST)
            formset_request=modelformset(request.POST,queryset=Timer.objects.none())
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
                formset=FormSet(queryset=Timer.objects.none(),initial=data)
                params['TimerForm']=formset
    return render(request,'timer/menu.html',params)



def timer_redirect(request):
    return redirect(to='/timer/main/1')



def show(request):
    data=Timer.objects.all()
    params={
        'data':data
    }
    return render(request,'timer/show.html',params)

def timer(request,num=1):
    TimerCreateFormSet=forms.modelformset_factory(
        Timer,
        form=TimerCreateForm,
        extra=1,
    )
    params={
        'TitleForm':TitleForm(initial={'title':'Title','hour':'時','min':'分','sec':'秒','sound':'Sound'}),
        'TimerForm':TimerCreateFormSet(
            queryset=Timer.objects.none(),
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
            formset_request=modelformset(request.POST,queryset=Timer.objects.none())
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
                params['TimerForm']=FormSet(initial=data,queryset=Timer.objects.none())
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

class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        params={
            'form':form,
        }
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='/timer')
        return render(request, 'timer/create.html', params)

    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        params={
            'form':form,
        }
        return  render(request, 'timer/create.html', params)

class Account_login(View):
    def post(self,request,*args,**kwargs):
        form=LoginForm(data=request.POST)
        params={
            'form':form,
        }
        if form.is_valid():
            username=form.cleaned_data.get('username')
            user=User.objects.get(username=username)
            login(request,user)
            return redirect(to='/timer')
        return render(request,'timer/login.html',params)
    
    def get(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        params={
            'form':form,
        }
        return render(request,'timer/login.html',params)

class Account_logout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        redirect(to='timer/main')
        form=LoginForm()
        params={
            'form':form,
        }
        return render(request,'timer/login.html',params)




account_login=Account_login.as_view()
create_account = Create_account.as_view()
account_logout=Account_logout.as_view()



        


# Create your views here.
