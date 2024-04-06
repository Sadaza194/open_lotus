from django.urls import path, include
from . import views

urlpatterns = [
    path("journal", views.journal, name="journal")


]