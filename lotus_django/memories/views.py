from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone
from .forms import MemoryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
    
@login_required(login_url='login/')
def create_memories(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.date = timezone.now()
            memory.save()
            messages.success(request, 'Memory saved!')
            return redirect('home')
    else:
        form = MemoryForm()
    return render(request, 'createMemories.html', {'form': form})