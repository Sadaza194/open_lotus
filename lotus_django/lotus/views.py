from django import forms
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(response):
    return render(response, "lotus/home.html", {})

def login(response):
    return render(response, "lotus/login.html", {})

def settings(response):
    return render(response, "lotus/settings.html", {})

class JournalForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-input'}))

def journal(request):
    form = JournalForm()
    return render(request, 'lotus/journal.html', {'form': form})

def questions(response):
    return render(response, "lotus/questions.html", {})

class MemoriesForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-input-memories'}))

def memories(request):
    form = MemoriesForm()
    return render(request, "lotus/memories.html", {'form': form})