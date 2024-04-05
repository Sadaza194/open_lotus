from django import forms

from .models import Question

class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'text',
            'type',
            'active',
            'frequency'
        ]