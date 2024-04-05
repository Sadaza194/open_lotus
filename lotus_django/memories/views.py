from django.shortcuts import render
from .models import Memory
from django.contrib import messages
from datetime import date
# Create your views here.

def create_memories(request):
    if request.method == 'POST':
        memory_text = request.POST.get('memory_text')
        emotion = request.POST.get('emotion')
        memory_date = date.today()
        new_memory = Memory(emotion=emotion, text=memory_text, date=memory_date)
        new_memory.save()
        # memory saved
        messages.success(request, 'Memory saved!')
        return render(request, 'createMemories.html') # goes  back to the template, replace with a messag
    else:
        return render(request, 'createMemories.html')