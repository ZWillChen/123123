
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	# Homepage 
    url(r'^$', views.index, name='home'),
    # File Operation
    url(r'^upload$', views.file_upload, name='file_upload'),
    url(r'^download$', views.file_download, name='file_download'),
    # Dashboard
    url(r'^dbdashboard$', views.database_dashboard, name='database_dashboard'),
    # Search and Result
    url(r'^search$', views.search, name='search'),	
    url(r'^search/result$', views.result, name='result'),
    url(r'^index$', views.index_result, name='index_result'),
]



