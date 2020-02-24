from django.shortcuts import render
from django.utils import timezone
from .models import Members

# Create your views here.

def index(request):
    #return render(request, 'home.html', {})
    return render(request, 'index.html', {})

def file_upload(request):
	return render(request, 'upload.html', {})

def file_download(request):
	return render(request, 'download.html', {})

def another_world(request):	
	return render(request, 'another.html', {})

def database_dashboard(request):
	members = Members.objects.all()
	return render(request, 'dbhome.html', {'members' : members})
	# return render(request, 'dbhome.html', {})