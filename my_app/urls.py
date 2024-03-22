from django.contrib import admin
from django.urls import include, path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('myfirst', views.myfirst),
    
    # path('my_app/sdcFile.html', views.sdc_view, name='sdc_html'),
   
    path('', views.sdc_file_view, name='sdc_file'),

]



