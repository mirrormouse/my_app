from django import forms

class AdderForm(forms.Form):
    num1=forms.IntegerField(label='数字１',min_value=0,max_value=9999)
    num2=forms.IntegerField(label='数字２',min_value=0,max_value=9999)
