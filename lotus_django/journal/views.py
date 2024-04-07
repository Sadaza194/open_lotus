from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .forms import JournalForm
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def journal(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.date = timezone.now()
            journal.save()
            return redirect('home')
    else:
        form = JournalForm()
    return render(request, 'journal.html', {'form': form})