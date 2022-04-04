from django.shortcuts import render

# Create your views here.
def index(request):
    msg=request.GET['msg']
    return HttpResoponse('you typed: "'+msg+'".')