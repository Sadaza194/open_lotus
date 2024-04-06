from django.urls import path
from . import views

urlpatterns = [
    path("base", views.base, name="base"),
    path("<str:page>", views.page, name="page"),

]