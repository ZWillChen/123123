from django.shortcuts import render
from django.utils import timezone
from .models import Members
from .models import Issue
from .GotionBattery.TestSQL import g_instance
import datetime
# Create your views here. #

def index(request):
    return render(request, 'index.html', {})

def file_upload(request):
	return render(request, 'upload.html', {})

def file_download(request):
	return render(request, 'download.html', {})

def search(request):	
	return render(request, 'search.html', {})

def result(request):
	# Preserve input args for next search
	lastkeyword = request.POST.get('keyword-input')
	lastname    = request.POST.get('name-input')
	laststart   = request.POST.get('start_date-input')
	lastend     = request.POST.get('end_date-input')

	# Store results in results list
	results = []
	start_date = request.POST.get('start_date-input').split('-')
	end_date = request.POST.get('end_date-input').split('-')
	start_year = int(start_date[0])
	start_month = int(start_date[1])
	start_day = int(start_date[2])
	end_year = int(end_date[0])
	end_month = int(end_date[1])
	end_day = int(end_date[2])
	keyword = request.POST.get('keyword-input')
	name = request.POST.get('name-input')
	res = g_instance.runProcedure('QueryIssue', (name, keyword, datetime.date(start_year, start_month, start_day), \
		datetime.date(end_year, end_month, end_day))) 
	if isinstance(res, tuple):
		emptyMsg = "No result to display"
		return render(request, 'search_result.html', {'emptyMsg' : emptyMsg, 'lastkeyword' : lastkeyword, 'lastname' : lastname,
		'laststart' : laststart, 'lastend' : lastend})
	for i in range(len(res)):
		inner = []
		for j in range(1, len(res.columns[1:-1]) + 1):
			inner.append(res.iat[i, j])
		results.append(inner)

	return render(request, 'search_result.html', {'results' : results, 'lastkeyword' : lastkeyword, 'lastname' : lastname,
		'laststart' : laststart, 'lastend' : lastend})

def database_dashboard(request):
	members = Members.objects.all()
	issues = Issue.objects.all()
	return render(request, 'dbhome.html', {'members' : members, 'issues' : issues})
	# return render(request, 'dbhome.html', {})