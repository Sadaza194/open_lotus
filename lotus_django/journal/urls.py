from django.urls import path, include
from . import views
# from lotus_django.views import home

urlpatterns = [
    path("", views.journal_base, name="journal_base"),
    path('view/', views.view_journals ,name='view_journals'),
    path('create/', views.create_journal ,name='create_journal'),


]