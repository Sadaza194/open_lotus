from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("<str:page>", views.page, name="page"),
    path('create_memories/', include('memories.urls')),
    path("questions/", include('questions.urls'))
]