from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your profile is updated successfully!')
            return redirect("index/")
        else:
            form = NewUserForm(request.POST)
            context = {"form": form}
            messages.success(request, 'invalid password!')
            templates = "register.html"
            return render(request, templates, context)
    form = NewUserForm
    context = {"form": form}
    templates = "register.html"
    return render(request, templates, context)


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index/")
            else:
                messages.error(request, "inavlid username or password")
        else:
            messages.error(request, "invalid credential")
    form = AuthenticationForm()
    context = {"form": form}
    templates = "login.html"
    return render(request, templates, context)


def logout_request(request):
    logout(request)
    messages.error(request, "Logout successfully")
    return redirect("signin")
