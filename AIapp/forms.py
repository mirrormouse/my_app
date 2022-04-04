from django import forms

class AdderForm(forms.Form):
    num1=forms.IntegerField(label='num1')
    num2=forms.IntegerField(label='num2')
