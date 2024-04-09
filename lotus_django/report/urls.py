from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_response),
    path('results/', views.show_report),
    path('home_test/', views.test_home)
]