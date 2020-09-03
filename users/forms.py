from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	email = forms.CharField(widget=forms.EmailInput(attrs = {}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']