from django.shortcuts import render
from .models import Memory
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login/')
def create_memories(request):
    # gets the elements of the answer according to the name in the html
    if request.method == 'POST':
        memory_text = request.POST.get('memory_text')
        emotion = request.POST.get('emotion')
        memory_date = date.today()
        new_memory = Memory(emotion=emotion, text=memory_text, date=memory_date)
        new_memory.save()
        messages.success(request, 'Memory saved!')
        return render(request, 'createMemories.html')
    else:
        return render(request, 'createMemories.html')