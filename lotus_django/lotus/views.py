from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
def base(response):
    # page = page + ".html"
    return render(response, "index.html", {})

@login_required(login_url='/signin')
def page(response, page):
    page = page + ".html"
    return render(response, "home.html", {})