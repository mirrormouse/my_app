from django.urls import path
from . import views



urlpatterns=[
    #r''のrはルートディレクトリ。''は任意の正規表現。
    path('', views.index, name='index'),
    path('adder', views.adder, name='adder'),
]