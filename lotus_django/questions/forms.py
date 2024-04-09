from django import forms
from .models import Question, LikertAnswer, TextAnswer

class CreateQuestionForm(forms.ModelForm):
    type = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-input'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-input'}))
    frequency = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-input'}))

    class Meta:
        model = Question
        fields = [
            'type',
            'text',
            'frequency'
        ]
        
class AnswerTextQuestionForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-input'}))

    class Meta:
        model = TextAnswer
        fields = [
            'text',
        ]
        
class AnswerLikertQuestionForm(forms.ModelForm):
    likert = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        model = LikertAnswer
        fields = [
            'likert',
        ]