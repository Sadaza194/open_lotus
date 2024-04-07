from django.urls import path, include
from .views import memories_base, create_memory, view_memories

urlpatterns = [
    path('', memories_base ,name='memories_base'),
    path('view/', view_memories ,name='view_memories'),
    path('create/', create_memory ,name='create_memory'),
]