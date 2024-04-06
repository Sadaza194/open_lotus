from django.urls import path, include
from .views import create_memories

urlpatterns = [
    path('',create_memories,name='create_memories'),

]