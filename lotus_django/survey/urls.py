from django.urls import path
from .views import FragenBeantwortenView, FragenListView

urlpatterns = [
    path('fragen/beantworten/', FragenBeantwortenView.as_view(), name='fragen_beantworten'),
    path('fragen/liste/', FragenListView.as_view(), name='fragen_liste'),
]