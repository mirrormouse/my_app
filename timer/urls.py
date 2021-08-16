from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns=[
    #r''のrはルートディレクトリ。''は任意の正規表現。
    path('', views.index, name='index'),
]