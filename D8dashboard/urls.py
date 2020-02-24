
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^upload$', views.file_upload, name='file_upload'),
    url(r'^download$', views.file_download, name='file_download'),
    url(r'^another$', views.another_world, name='another_world'),
    url(r'^dbdashboard$', views.database_dashboard, name='database_dashboard'),
]



