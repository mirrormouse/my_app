from django import forms
from .models import Timer
from django.contrib.auth.models import User

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