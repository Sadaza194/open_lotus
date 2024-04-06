from django.shortcuts import render
from .forms import CreateQuestionForm

# Create your views here.

def create_question(request, *args, **kwargs):
    form = CreateQuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateQuestionForm()
    context = {
        'form': form
    }
    return render(request, "create_question.html", context)