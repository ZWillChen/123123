from django.shortcuts import render
from django.utils import timezone
from .models import Members
from .models import Issue
from .GotionBattery.TestSQL import g_instance
import datetime
import json
# Create your views here. #


def index(request):
	res = g_instance.runProcedure('QueryIssueStatus', ('', '', datetime.date(1970, 1, 1), datetime.date(2100, 1, 1)))
	pieres = g_instance.runProcedure('QueryIssueCount', ('', '', datetime.date(1970, 1, 1), datetime.date(2100, 1, 1)))

	if not isinstance(pieres, tuple):
		cntActive = int(pieres.iat[0, 2])
		cntClosed = int(pieres.iat[0, 1])
	else:
		cntActive = 0
		cntClosed = 0

	if not isinstance(res, tuple):
		lastModifiedDate = str(res.iat[len(res) - 1, 0])
		barData = []
		for col in res.columns:
			inner = []
			for c in res[col].values:
				inner.append(c)
			barData.append(inner)
		for i in range(len(barData[0])):
			barData[0][i] = barData[0][i].strftime("%m-%d-%Y")

	else:
		lastModifiedDate = datetime.date.today()
		barData = []

	return render(request, 'index.html', {'cntOpen': cntActive,
										  'cntClose': cntClosed,
										  'lastDate': lastModifiedDate,
										  'barDates': barData[0],
										  'barClosed': barData[1],
										  'barOpens': barData[2],
										  })


def index_result(request):
	# Preserve input args for next search
	lastkeyword = request.POST.get('keyword-input')
	lastname    = request.POST.get('name-input')
	laststart   = request.POST.get('start_date-input')
	lastend     = request.POST.get('end_date-input')

	# Receive submit from form
	start_date = request.POST.get('start_date-input').split('-')
	end_date = request.POST.get('end_date-input').split('-')
	keyword = request.POST.get('keyword-input')
	name = request.POST.get('name-input')

	# Query
	pieres = getActive(start_date, end_date, keyword, name)
	res = getBarData(start_date, end_date, keyword, name)
	if not res[0]:
		barData = [[], [], []]
	else:
		barData = res[0]
	return render(request, 'index_result.html', {'pieres': list(pieres),
												 'lastDate': res[1],
												 'barDates': barData[0],
												 'barClosed':  barData[1],
												 'barOpens': barData[2],
												 'lastkeyword': lastkeyword,
												 'lastname': lastname,
												 'laststart': laststart,
												 'lastend': lastend,
												 })


def file_upload(request):
	return render(request, 'upload.html', {})


def file_download(request):
	return render(request, 'download.html', {})


def search(request):	
	return render(request, 'search.html', {})


# Search Result
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
	res = g_instance.runProcedure('QueryIssue', (name, keyword, datetime.date(start_year, start_month, start_day),
		datetime.date(end_year, end_month, end_day)))
	if isinstance(res, tuple):
		emptyMsg = "No result to display"
		return render(request, 'search_result.html', {'emptyMsg' : emptyMsg,
													  'lastkeyword' : lastkeyword,
													  'lastname' : lastname,
													  'laststart' : laststart,
													  'lastend' : lastend,
													  })
	for i in range(len(res)):
		inner = []
		for j in range(1, len(res.columns[1:-1]) + 1):
			inner.append(res.iat[i, j])
		results.append(inner)

	return render(request, 'search_result.html', {'results' : results,
												  'lastkeyword' : lastkeyword,
												  'lastname' : lastname,
												  'laststart' : laststart,
												  'lastend' : lastend,
												  })


def database_dashboard(request):
	members = Members.objects.all()
	issues = Issue.objects.all()
	return render(request, 'dbhome.html', {'members' : members,
										   'issues' : issues,
										   })
	# return render(request, 'dbhome.html', {})


def page_not_found(request, exception, template_name='404.html'):
	return render(request, template_name)


def page_error(request, template_name='500.html'):
	return render(request, template_name)


# functions for using query
def getBarData(s, e, k, n):
	start_year = int(s[0])
	start_month = int(s[1])
	start_day = int(s[2])
	end_year = int(e[0])
	end_month = int(e[1])
	end_day = int(e[2])
	res = g_instance.runProcedure('QueryIssueStatus', (n, k, datetime.date(start_year, start_month, start_day),
													  datetime.date(end_year, end_month, end_day)))
	if not isinstance(res, tuple):
		lastModifiedDate = str(res.iat[len(res) - 1, 0])
		barData = []
		for col in res.columns:
			inner = []
			for c in res[col].values:
				inner.append(c)
			barData.append(inner)
		for i in range(len(barData[0])):
			barData[0][i] = barData[0][i].strftime("%m-%d-%Y")
	else:
		lastModifiedDate = datetime.date.today()
		barData = []
	return [barData, lastModifiedDate]


def getActive(s, e, k, n):
	cntActive = 0
	cntClosed = 0
	start_year = int(s[0])
	start_month = int(s[1])
	start_day = int(s[2])
	end_year = int(e[0])
	end_month = int(e[1])
	end_day = int(e[2])
	res = g_instance.runProcedure('QueryIssueCount', (n, k, datetime.date(start_year, start_month, start_day),
													  datetime.date(end_year, end_month, end_day)))
	if not isinstance(res, tuple):
		cntActive = int(res.iat[0, 2])
		cntClosed = int(res.iat[0, 1])
	return [cntActive, cntClosed]
