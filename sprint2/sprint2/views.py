from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def home(request):
    return HttpResponse("Bienvenido a Widmy!!!")

def healthCheck(request):
    return HttpResponse('ok')