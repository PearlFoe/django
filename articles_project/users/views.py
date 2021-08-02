from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm
from .models import User
from .model.User import ObjectDoesNotExist

import os

def login(request):
	message = None

	if request.method == 'POST':
		l_form = LoginForm(request.POST)

		if l_form.is_valid:
			try:
				user = User.objects.get(
					email=l_form.cleaned_data.login
				)
			except ObjectDoesNotExist:
				message = 'Invalid login'
				return HttpResponse(f'Login page. {message}')

			user.check_password(l_form.cleaned_data.password)

			request.session['session_id'] = os.urandom(20).hex()
			request.session.modified = True
	else:
		l_form = LoginForm()
		return HttpResponse('Login page.')

def register(request):
	return HttpResponse('Registration page')

def user_page_view(request, user_id=None):
	return HttpResponse(f'User {user_id} page')