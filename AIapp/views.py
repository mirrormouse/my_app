from django.shortcuts import render
from django.http import HttpResponse
from tensorflow.keras.models import load_model
# Create your views here.
def index(request):
    model = load_model("model/my_model.h5")
    return HttpResponse('OK!')