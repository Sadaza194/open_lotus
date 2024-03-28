from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def base(response):
    # page = page + ".html"
    return render(response, "lotus/base.html", {})

def page(response, page):
    page = page + ".html"
    return render(response, "lotus/home.html", {})