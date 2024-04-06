"""lotus_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import register, signin, logout_request
from questions.views import create_question

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("lotus.urls")),
    # path('report/', include('report.urls')),
    # path('journal/', include('journal.urls')),

    path('index/', include("lotus.urls")),
    path('report/', include('report.urls')),
    path('register/', register, name='register'),
    path('', signin, name='signin'),
    path('logout',logout_request,name='logout'),
    path("questions/", include('questions.urls'))
]
