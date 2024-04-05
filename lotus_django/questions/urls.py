from django.urls import path
from . import views

urlpatterns = [
    path('create_question/', views.create_question),

]