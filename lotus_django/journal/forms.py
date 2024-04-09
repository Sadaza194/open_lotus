from django import forms
from journal.models import Journal

class JournalForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-input'}))

    class Meta:
        model = Journal
        fields = [
            'text'
            
        ]