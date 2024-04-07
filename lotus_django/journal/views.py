from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from journal.models import Journal
from .forms import JournalForm
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='login/')
def journal(request):
    form = JournalForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = JournalForm()
    context = {
        'form': form
    }
    return render(request, "journal.html", context)


# from django.contrib.auth import get_user_model
# User = get_user_model()

# @login_required(login_url='login/')
# def journal(request):
#     if request.method == 'POST':
#         form = JournalForm(request.POST or None)
#         if form.is_valid():
#             journal = form.save(commit=False)
#             if request.user.is_authenticated:  # Check if the user is authenticated
#                 user = User.objects.get(username=request.user.username)
#                 entry = Entry.objects.create(user=user, is_journal=True)
#                 journal.entry = entry
#                 journal.save()
#                 return redirect('home')
#     else:
#         form = JournalForm()
#     context = {
#         'form': form
#     }
#     return render(request, "journal.html", context)