from django.urls import path,re_path
from django.conf.urls import include
from ticket import views

urlpatterns=[
    re_path(r'^$',views.index,name='index'),
    path("home",views.home,name="home"),
    path("visitor",views.visitor,name="visitor"),
]