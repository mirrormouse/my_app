from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns=[
    #r''のrはルートディレクトリ。''は任意の正規表現。
    path('', views.index, name='index'),
    path('main', views.timer, name='timer'),
    path('main/<int:num>', views.timer, name='timer'),
    path('login', views.account_login, name='login'),
    path('logout',views.account_logout, name="logout"),
    path('create',views.create_account,name='create_account'),
]