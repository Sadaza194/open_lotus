from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_report(request, *args, **kwargs):
    return render(request, 'report.html', {'name': 'Your Name Here'})

def test_response(request, *args, **kwargs):
    return HttpResponse("<h1>This is a test</h1>")

def test_home(request, *args, **kwargs):
    return render(request, "home.html", {})