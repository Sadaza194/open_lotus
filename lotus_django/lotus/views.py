from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def base(response):
    # page = page + ".html"
    return render(response, "base.html", {})

def page(response, page):
    page = page + ".html"
    return render(response, "home.html", {})