from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateQuestionForm, AnswerLikertQuestionForm, AnswerTextQuestionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from questions.models import LikertAnswer, TextAnswer, Question
from django.utils import timezone

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
def answer_likert_question(request, *args, **kwargs):
    if request.method == 'POST':
        form = AnswerLikertQuestionForm(request.POST or None)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.date = timezone.now()
            answer.save()
            messages.success(request, 'Likert question saved!')
            return redirect('questionsBase')
    else:
        likert_questions = Question.objects.all().filter(type='likert')
        form = AnswerLikertQuestionForm()
        context = {
            'form': form,
            'likert_questions': likert_questions
        }
    return render(request, 'answerLikertQuestion.html', context)

@login_required(login_url='login/')
def answer_text_question(request, *args, **kwargs):
    if request.method == 'POST':
        form = AnswerTextQuestionForm(request.POST or None)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.date = timezone.now()
            answer.save()
            messages.success(request, 'Text answer saved!')
            return redirect('questionsBase')
    else:
        text_questions = Question.objects.all().filter(type='text')
        form = AnswerTextQuestionForm()
        context = {
            'form': form,
            'text_questions': text_questions
        }
    return render(request, 'answerTextQuestion.html', context)

@login_required(login_url='login/')
def view_answers(request, *args, **kwargs):
    text_answers = TextAnswer.objects.all().filter(user=request.user)
    likert_answers = LikertAnswer.objects.all().filter(user=request.user)
    
    context = {
        "text":text_answers,
        "likert":likert_answers
    }
    return render(request, 'viewAnswers.html', context)