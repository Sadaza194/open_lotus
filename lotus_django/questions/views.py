from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateQuestionForm, AnswerLikertQuestionForm, AnswerTextQuestionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from questions.models import LikertAnswer, TextAnswer

# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def create_question(request, *args, **kwargs):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST or None)
        if form.is_valid():
            question = form.save(commit=False)
            question.creator = request.user
            question.save()
            messages.success(request, 'Question saved!')
            return redirect('create_question')
    else:
        form = CreateQuestionForm()
    return render(request, 'createQuestion.html', {'form': form})


@login_required(login_url='login/')
def questionsBase(response):
    return render(response, "questionsBase.html", {})


@login_required(login_url='login/')
def answer_question(request, *args, **kwargs):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST or None)
        if form.is_valid():
            question = form.save(commit=False)
            question.creator = request.user
            question.save()
            messages.success(request, 'Question saved!')
            return redirect('create_question')
    else:
        form = CreateQuestionForm()
    return render(request, 'createQuestion.html', {'form': form})

@login_required(login_url='login/')
def view_answers(request, *args, **kwargs):
    text_answers = TextAnswer.objects.all().filter(user=request.user)
    likert_answers = LikertAnswer.objects.all().filter(user=request.user)
    
    context = {
        "text":text_answers,
        "likert":likert_answers
    }
    return render(request, 'viewAnswers.html', context)