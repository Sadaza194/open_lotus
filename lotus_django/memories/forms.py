from django import forms
from memories.models import Memory

class MemoryForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-input'}))
    emotion = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-input'}))

    class Meta:
        model = Memory
        fields = [
            'text',
            'emotion'
        ]