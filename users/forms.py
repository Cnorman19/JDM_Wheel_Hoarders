from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from sell.models import Sell


class UserRegisterForm(UserCreationForm):
	
	email = forms.CharField(widget=forms.EmailInput(attrs = {}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

	email = forms.CharField(widget=forms.EmailInput(attrs = {}))

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['image']

class NewSalePostForm(forms.ModelForm):

	class Meta:
		model = Sell
		fields = ['name', 'description', 'diameter']