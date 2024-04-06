from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("settings/", views.settings, name="settings"),

    path("questions/", views.questions, name="questions"),

]