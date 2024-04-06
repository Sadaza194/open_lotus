from django.urls import path, include
from . import views
from lotus_django.views import home

urlpatterns = [
    path("", views.journal, name="journal"),
    path("home/", home, name="home"),


]