from django.shortcuts import render
from .forms import CreateQuestionForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login/')
def create_question(request, *args, **kwargs):
    form = CreateQuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateQuestionForm()
    context = {
        'form': form
    }
    return render(request, "create_question.html", context)


@login_required(login_url='login/')
def questions(response):
    return render(response, "questions.html", {})