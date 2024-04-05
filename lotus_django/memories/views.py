from django.shortcuts import render
from .models import Memory
# Create your views here.

def create_memories(request):
    if request.method == 'POST':
        memory_text = request.POST.get('memory_text')
        emotion = request.POST.get('emotion')
        date = request.POST.get('date')
        new_memory = Memory(emotion=emotion, text=memory_text, date=date)
        new_memory.save()
    else:
        return render(request, 'createMemories.html')