from _datetime import datetime
from django.shortcuts import HttpResponse

def hello_view(request):
  if request.method == 'GET':
    return HttpResponse("Hello! Its my project,hjhj ")

def current_date_view(request):
  if request.method == 'GET':
    current_date = datetime.now().strftime("%Y-%m-%d")
    return HttpResponse(f"Current date: {current_date}")
    # return HttpResponse(f'current date ')

def goodbye_view(request):
  if request.method == 'GET':
    return HttpResponse("Goodbye user!")

