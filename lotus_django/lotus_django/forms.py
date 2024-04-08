from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import DateInput

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'buttonLogin'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'buttonLogin'}))



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'buttonLogin'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'buttonLogin'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'buttonLogin'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'buttonLogin'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user