from django.urls import path
from . import views

urlpatterns = [
    path("", views.questionsBase, name="questionsBase"),
    path('create_question/', views.create_question, name="create_question"),
    path("answer_likert/", views.answer_likert_question, name="answer_likert_question"),
    path("answer_text/", views.answer_text_question, name="answer_text_question"),
    path("view_answers/", views.view_answers, name="view_answers"),
    path("likert_report/", views.likert_report, name="likert_report"),
    

]