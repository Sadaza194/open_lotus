from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login/')
class JournalForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-input'}))

@login_required(login_url='login/')
def journal(request):
    form = JournalForm()
    return render(request, 'journal.html', {'form': form})