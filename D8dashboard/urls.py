
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	# Homepage 
    url(r'^$', views.index, name='home'),
    # File Operation
        # Upload
    url(r'^upload$', views.file_upload, name='file_upload'),
    url(r'^upload/file$', views.upload_8Dfile, name='upload_8D'),
    url(r'^upload/result$', views.upload_result, name='upload_result'),
        # Download
    url(r'^download$', views.file_download, name='file_download'),
    url(r'^download/search$', views.file_search, name='file_search'),
    url(r'^download/fileid(\d+)/$', views.download_8Dtemplate, name='download_8Dtemplate'),
        # Create New Ticket
    url(r'^add/ticket$', views.add_ticket, name='add_ticket'),
    # Dashboard
    url(r'^dbdashboard$', views.database_dashboard, name='database_dashboard'),
    # Search and Result
    url(r'^search$', views.search, name='search'),	
    url(r'^search/result$', views.result, name='result'),
    url(r'^index$', views.index_result, name='index_result'),
]



