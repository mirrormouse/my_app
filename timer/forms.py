from django import forms
from .models import SOUND, Timer
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
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
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