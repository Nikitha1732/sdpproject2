from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('hello2/', hello1),
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print_to_console/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('ran1/',random123,name='random123'),
    path('ran2/',RandomOtp,name='RandomOtp'),
    path('rand1/',rand1,name='rand1'),
    path('date1/', getdate1, name='getdate1'),
    path('date/', get_date, name='get_date'),
    path('time/', tzfunctioncall, name='tzfunctioncall'),
    path('form1/', formExmp, name='formExmp'),
    path('form/', registerloginfunction, name='registerloginfunction'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('pie1/', Pie, name='Pie'),
    path('hh',famousplaces,name='famousplaces'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('weather/', weather, name='weather'),
    path('login/',login,name='login'),
    path('login1/', login1, name='login1'),
    path('signup/',signup,name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('logout/', logout, name='logout'),
    path('con/', contactcall, name='contactcall'),
    path('con1/', contactmail, name='contactmail'),
]