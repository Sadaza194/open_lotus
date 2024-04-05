from django.shortcuts import render
from .models import Memory
# Create your views here.
def create_memories(request):
    return render(request, 'createMemories.html')