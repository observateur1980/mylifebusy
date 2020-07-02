from django.shortcuts import render
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, get_user_model, logout
from django.urls import reverse

User = get_user_model()

# Create your views here.


def user_login(request, *args, **kwargs):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		user_obj = form.cleaned_data.get('user_obj')
		login(request, user_obj)
		# return HttpResponseRedirect(reverse('losgatos:mainpage'))
	return render(request, 'account/login.html', {'form' : form})



def user_logout(request):
	logout(request)
	return HttpResponseRedirect('login')

