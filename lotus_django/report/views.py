from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_report(request):
    return render(request, 'report.html', {'name': 'Your Name Here'})