from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, FileResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from .models import Members
from .models import Issue
from .GotionBattery.TestSQL import g_instance
from .GotionBattery.BatteryDocs import DocProcess
import datetime
import json
# Create your views here. #


@cache_page(60 * 60)
def index(request):
	g_instance.connect()
	# pie chart data
	cntActive = getActive([1970, 1, 1], [2100, 1, 1], '', '')[0]
	cntClosed = getActive([1970, 1, 1], [2100, 1, 1], '', '')[1]

	# bar chart data
	lastModifiedDate = getBarData([1970, 1, 1], [2100, 1, 1], '', '')[1]
	barData = getBarData([1970, 1, 1], [2100, 1, 1], '', '')[0]

	return render(request, 'index.html', {'cntOpen': cntActive,
										  'cntClose': cntClosed,
										  'lastDate': lastModifiedDate,
										  'barDates': barData[0],
										  'barClosed': barData[1],
										  'barOpens': barData[2],
										  })


def index_result(request):
	g_instance.connect()
	# Preserve input args for next search
	laststart = request.POST.get('start_date-input')
	lastend = request.POST.get('end_date-input')

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
												 'lastkeyword': keyword,
												 'lastname': name,
												 'laststart': laststart,
												 'lastend': lastend,
												 })


def file_upload(request):
	return render(request, 'upload.html', {})


def upload_8Dfile(request):
	if request.method == "POST":
		file = request.FILES.get("file")
		with open('D8dashboard/GotionBattery/temp/tempfile.xlsx', "wb+") as destination:
			if file:
				for chunk in file.chunks():
					destination.write(chunk)
				destination.close()
			else:
				return render(request, 'upload_feedback.html', {'Error': "File does not exist: " + str(type(file))})
		xls_ins = DocProcess('D8dashboard/GotionBattery/temp/tempfile.xlsx')
		(error_code, d_list, s_list) = xls_ins.process8Dfile()
		if error_code != 0:
			error = "The upload file has errors: error code is " + str(error_code)
			return render(request, 'upload_feedback.html', {'Error': error})
		else:
			g_instance.connect()
			g_instance.upload8DTables(d_list)
			return render(request, 'upload_feedback.html', {})

	return render(request, 'upload_feedback.html', {})


def upload_result(request):
	return render(request, 'upload_feedback.html', {})


def file_download(request):
	return render(request, 'download.html', {})


def download_8Dtemplate(request):
	g_instance.connect()
	# Query file
	f = g_instance.runProcedure('DownloadFile', (1,), 0)
	if f:
		with open('D8dashboard/GotionBattery/8Ddownload.xlsx', "wb") as local_file:
			local_file.write(f[0]['file'])
			local_file.close()
		with open('D8dashboard/GotionBattery/8Ddownload.xlsx', "rb") as download_file:
			response = HttpResponse(download_file)
			response['Content-Type'] = 'application/octet-stream'
			response['Content-Disposition'] = 'attachment; filename="8Ddownload.xlsx"'
			return response
	else:
		error = "Error loading file from database - File does not exist."
		return render(request, 'download.html', {'Error': error,
												 })


def search(request):	
	return render(request, 'search.html', {})


# Search Result
def result(request):
	g_instance.connect()
	# Preserve input args for next search
	laststart   = request.POST.get('start_date-input')
	lastend     = request.POST.get('end_date-input')
	keyword = request.POST.get('keyword-input')
	name = request.POST.get('name-input')

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

	res = g_instance.runProcedure('QueryIssue', (name, keyword, datetime.date(start_year, start_month, start_day),
		datetime.date(end_year, end_month, end_day)))
	if isinstance(res, tuple):
		emptyMsg = "No result to display"
		return render(request, 'search_result.html', {'emptyMsg': emptyMsg,
													  'lastkeyword': keyword,
													  'lastname': name,
													  'laststart': laststart,
													  'lastend': lastend,
													  })
	for i in range(len(res)):
		inner = []
		for j in range(1, len(res.columns[1:-1]) + 1):
			inner.append(res.iat[i, j])
		results.append(inner)

	return render(request, 'search_result.html', {'results': results,
												  'lastkeyword': keyword,
												  'lastname': name,
												  'laststart': laststart,
												  'lastend': lastend,
												  })


@cache_page(15 * 60)
def database_dashboard(request):
	members = Members.objects.all()
	issues = Issue.objects.all()
	return render(request, 'dbhome.html', {'members': members,
										   'issues': issues,
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
