from django.forms import ModelForm
from .models import Frage

class FragenBeantwortenForm(ModelForm):
    class Meta:
        model = Frage
        fields = ['text', 'typ', 'frequenz']
