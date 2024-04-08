from django.urls import path
from . import views

urlpatterns = [
    path("", views.questionsBase, name="questionsBase"),
    path('create_question/', views.create_question, name="create_question"),
    path("answer/", views.questionsBase, name="questionsBase"),
    path("view_answers/", views.view_answers, name="view_answers"),
    

]