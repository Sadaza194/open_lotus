from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.show_report)
]