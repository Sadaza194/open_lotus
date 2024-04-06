from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = NewUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your profile is updated successfully!')
            return redirect("home")
        else:
            form = NewUserForm(request.POST or None)
            context = {"form": form}
            messages.success(request, 'invalid password!')
            templates = "register.html"
            return render(request, templates, context)
    form = NewUserForm
    context = {"form": form}
    templates = "register.html"
    return render(request, templates, context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "invalid username or password")
        else:
            messages.error(request, "invalid credential")
    form = AuthenticationForm()
    context = {"form": form}
    templates = "login.html"
    return render(request, templates, context)


def logout_request(request):
    logout(request)
    messages.error(request, "Logout successfully")
    return redirect("login")


# Create your views here.
@login_required(login_url='login/')
def home(response):
    return render(response, "home.html", {})

# def base(response):
#     # page = page + ".html"
#     return render(response, "index.html", {})

#def login(response):
    #return render(response, "lotus/login.html", {})

@login_required(login_url='login/')
def settings(response):
    return render(response, "lotus/settings.html", {})

@login_required(login_url='login/')
def questions(response):
    return render(response, "lotus/questions.html", {})

@login_required(login_url='login/')
class MemoriesForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-input-memories'}))

@login_required(login_url='login/')
def memories(request):
    form = MemoriesForm()
    return render(request, "lotus/memories.html", {'form': form})


