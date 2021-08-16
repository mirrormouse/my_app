
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

def index(request):
    return HttpResponse("Hello")







"""
class HelloView(TemplateView):
    def __init__(self):
        self.params={
            'title':'Hello',
            'result':None,
            'form':HelloForm(),
        }
    def get(self,request):
        return render(request,'hello\index.html',self.params)
    def post(self,request):
        ch=request.POST.getlist('choice')
        result='<ol class="list-group"><b>selected:</b>'
        for item in ch:
            result+='<li class="list-group-item">'+item+'</li>'
        result +='</ol>'
        self.params['result']=result
        self.params['form']=HelloForm(request.POST)
        return render(request,'hello\index.html',self.params)
"""

        


# Create your views here.

