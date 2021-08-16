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

class SetForm(forms.Form):
    number=forms.IntegerField(label='number',\
        widget=forms.NumberInput(attrs={'class':'form-control'}))

