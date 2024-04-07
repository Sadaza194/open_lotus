from django.urls import path, include
from .views import create_memories, view_memories

urlpatterns = [
    path('', view_memories ,name='view_memories'),
    path('create/', create_memories ,name='create_memories'),
]