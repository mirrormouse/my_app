from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns=[
    #r''のrはルートディレクトリ。''は任意の正規表現。
    path('', views.index_redirect, name='index_redirect'),
    path('<int:num>', views.index, name='index'),
    path('use_redirect', views.use_redirect, name='use_redirect'),
    path('use', views.use, name='use'),
    path('main', views.timer_redirect, name='timer_redirect'),
    path('main/<int:num>', views.timer, name='timer'),
    path('login', views.account_login, name='login'),
    path('logout',views.account_logout, name="logout"),
    path('create',views.create_account,name='create_account'),
    path('list',views.show,name='show'),
    path('edit/<int:id>/<int:num>',views.edit,name='edit'),
    path('edit',views.edit_redirect,name='edit'),
]