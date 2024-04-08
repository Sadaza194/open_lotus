from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.utils import timezone
from .forms import JournalForm
from django.contrib.auth.decorators import login_required
from journal.models import Journal





# Create your views here.

@login_required(login_url='login/')
def journal_base(request, *args, **kwargs):
    is_admin = request.user.is_superuser
    context = {
        "admin": is_admin
    }
    return render(request, 'journalBase.html', context)

@login_required(login_url='login/')
def view_journals(request, *args, **kwargs):
    user_journals = Journal.objects.all().filter(user=request.user)
    context = {
        "journals":user_journals
    }
    return render(request, 'viewJournals.html', context)

@login_required(login_url='login/')
def create_journal(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.date = timezone.now()
            journal.save()
            messages.success(request, 'Journal saved!')
            return redirect('home')
    else:
        form = JournalForm()
    return render(request, 'createJournal.html', {'form': form})