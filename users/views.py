from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm , UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from friendship.models import Friend, Follow, Block , FriendshipRequest

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')

	else:
		form = UserRegisterForm()


	return render(request, 'users/register.html', {'form' : form })


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, 
												 instance = request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.profile)

	context = {

		'u_form' : u_form,
		'p_form' : p_form
	}
	
	return render(request, 'users/profile.html', context)

@login_required
def sendFriendRequest(request):
	
	if request.method == 'GET':
		other_user = User.objects.get(pk=1)
		Friend.objects.add_friend(
	    request.user,                               # The sender
	    other_user,                                 # The recipient
	    message='Hi! I would like to add you')      # This message is optional

@login_required
def acceptFriendRequest():
	friend_request = FriendshipRequest.objects.get(to_user=1)
	friend_request.accept()

@login_required
def declineFriendRequest():
	friend_request = FriendshipRequest.objects.get(to_user=1)
	friend_request.reject()
