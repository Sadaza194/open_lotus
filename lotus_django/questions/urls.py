from django.urls import path
from . import views

urlpatterns = [
    path("", views.questions, name="questions"),
    path('create_question/', views.create_question, name="create_question"),

]