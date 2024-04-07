from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

def login(response):
    return render(response, "login.html", {})
