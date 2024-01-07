from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ProjectDetails, Team

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Your username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Your password'}))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Your username'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder': 'Your email address'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}))

class ProjectDetailsForm(forms.ModelForm):
    class Meta:
        model = ProjectDetails
        fields = ['team_name', 'project_name', 'github_link', 'project_description']

    team_name = forms.ModelChoiceField(queryset=Team.objects.all(), empty_label=None)
#    team_name = forms.ChoiceField(choices=[(team.id, team.name) for team in (Team.objects.all())])
#    team_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Team Name'}))
    project_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Project Name'}))
    github_link = forms.URLField(widget = forms.TextInput(attrs={'placeholder': 'Enter Your Github Repository Link'}))
    project_description = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter the Project description'}))