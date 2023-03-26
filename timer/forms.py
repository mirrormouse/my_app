from django import forms
from .models import SOUND, Timer, TimerSet,HomeTimer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



class UserCreateForm(UserCreationForm):
    def __int__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
    class Meta:
        model=User
        fields=("username","password1","password2",)

class LoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['class']='form-control'

class TimerCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title']=forms.CharField(
            label='',
            required=False,
            widget=forms.TextInput(attrs={'placeholder':'タイマー', 'class':'form-control'})
        )
        self.fields['hour']=forms.IntegerField(
            label='',
            required=False,
            widget=forms.NumberInput(attrs={'placeholder':'00', 'class':'form-control'})
        )
        self.fields['min']=forms.IntegerField(
            label='',
            required=False,
            widget=forms.NumberInput(attrs={'placeholder':'00', 'class':'form-control'})
        )
        self.fields['sec']=forms.IntegerField(
            label='',
            required=False,
            widget=forms.NumberInput(attrs={'placeholder':'00', 'class':'form-control'})
        )
        self.fields['sound']=forms.ChoiceField(
            label='',
            choices=SOUND,
            widget=forms.Select(attrs={'placeholder':'00', 'class':'form-control'})
        )
    class Meta:
        model = Timer
        fields = '__all__'
        labels={
            'title':'',
            'hour':'',
            'min':'',
            'sec':'',
            'sound':'',
        }
class HomeTimerCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = HomeTimer
        fields = '__all__'
        labels={
            'title':'',
            'hour':'',
            'min':'',
            'sec':'',
            'sound':'',
        }


class SetForm(forms.Form):
    number=forms.IntegerField(label='number',\
        widget=forms.NumberInput(attrs={'class':'form-control'}))

class TitleForm(forms.Form):
    title=forms.CharField(label='',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    hour=forms.CharField(label='',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    min=forms.CharField(label='',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    sec=forms.CharField(label='',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    sound=forms.CharField(label='',\
        widget=forms.TextInput(attrs={'class':'form-control'}))

    

class TimerSetForm(forms.Form):
    title=forms.CharField(label='',required=False,\
        widget=forms.TextInput(attrs={'placeholder':'タイトルを設定してください','class':'form-control'}))

class TimerSelectForm(forms.Form):
    def __init__(self,user,*args,**kwargs):
        super(TimerSelectForm,self).__init__(*args,**kwargs)
        self.fields['groups']=forms.ChoiceField(
            label='',
            choices=[(item.id,item.title) \
                for item in TimerSet.objects.filter(user=user)],\
                widget=forms.Select(attrs={'class':'form-control'}),
        )

"""
class TimerSetForm(forms.ModelForm):
    def __int__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['class']='form-control'
        self.fields['maintitle'].widget.attrs['class']='form-control'
        self.fields['set'].widget.attrs['class']='form-control'
    class Meta:
        model=TimerSet
        fields=['user','maintitle','set']
"""