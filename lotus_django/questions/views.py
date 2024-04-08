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
    is_admin = response.user.is_superuser
    context = {
        "admin": is_admin
    }
    return render(response, "questionsBase.html", context)


@login_required(login_url='login/')
def answer_likert_question(request, *args, **kwargs):
    # Load all likert questions
    likert_questions = Question.objects.all().filter(type='likert')

    # Get the current question index from the session
    current_index = request.session.get('current_likert_index', 0)

    # Get the current question
    current_question = likert_questions[current_index] if current_index < len(likert_questions) else None

    if request.method == 'POST':
        form = AnswerLikertQuestionForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = current_question
            answer.date = timezone.now()
            answer.save()
            messages.success(request, 'Likert answer saved!')

            # Increment the current question index
            current_index += 1
            request.session['current_likert_index'] = current_index

            # Redirect to the same view to load the next question
            return redirect('answer_likert_question')

    # Create a new form for the current question
    form = AnswerLikertQuestionForm()

    context = {
        'form': form,
        'likert_question': current_question
    }

    return render(request, 'answerLikertQuestion.html', context)

@login_required(login_url='login/')
def answer_text_question(request, *args, **kwargs):
    # Load all text questions
    text_questions = Question.objects.all().filter(type='text')

    # Get the current question index from the session
    current_index = request.session.get('current_text_index', 0)

    # Get the current question
    current_question = text_questions[current_index] if current_index < len(text_questions) else None

    if request.method == 'POST':
        form = AnswerTextQuestionForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = current_question
            answer.date = timezone.now()
            answer.save()
            messages.success(request, 'Text answer saved!')

            # Increment the current question index
            current_index += 1
            request.session['current_text_index'] = current_index

            # Redirect to the same view to load the next question
            return redirect('answer_text_question')

    # Create a new form for the current question
    form = AnswerTextQuestionForm()

    context = {
        'form': form,
        'text_question': current_question
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