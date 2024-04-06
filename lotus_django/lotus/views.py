from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='login/')
def home(response):
    return render(response, "home.html", {})

# def base(response):
#     # page = page + ".html"
#     return render(response, "index.html", {})

def login(response):
    return render(response, "login.html", {})

@login_required(login_url='login/')
def settings(response):
    return render(response, "settings.html", {})

@login_required(login_url='login/')
class JournalForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-input'}))

@login_required(login_url='login/')
def journal(request):
    form = JournalForm()
    return render(request, 'journal.html', {'form': form})

@login_required(login_url='login/')
def questions(response):
    return render(response, "questions.html", {})

@login_required(login_url='login/')
class MemoriesForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-input-memories'}))

@login_required(login_url='login/')
def memories(request):
    form = MemoriesForm()
    return render(request, "memories.html", {'form': form})

