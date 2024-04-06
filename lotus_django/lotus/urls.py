from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("login", views.login, name="login"),

    path("settings", views.settings, name="settings"),

    path("journal", views.journal, name="journal"),

    path("questions", views.questions, name="questions"),

    path("memories", views.memories, name="memories")


    path('create_memories/', include('memories.urls')),
    path("questions/", include('questions.urls'))
]