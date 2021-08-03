from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect

from django.core.exceptions import ObjectDoesNotExist

from .forms import LoginForm, RegisterFrom
from .models import User
import os

def login(request):
	message = None

	if request.method == 'POST':
		l_form = LoginForm(request.POST)

		if l_form.is_valid():
			try:
				user = User.objects.get(
					email=l_form.cleaned_data['login']
				)
			except ObjectDoesNotExist:
				message = 'Invalid login'
				return render(request, 'users/login.html', {'form': l_form, 'message': message})

			user.check_password(l_form.cleaned_data['password'])

			request.session['session_id'] = os.urandom(20).hex()
			request.session.modified = True

			message = 'Logged in'
			return render(request, 'users/login.html', {'form': l_form, 'message': message})
	else:
		l_form = LoginForm()
		return render(request, 'users/login.html', {'form': l_form, 'message': message})

def logout(request):
	return HttpResponse('Logged out')

def register(request):
	message = None

	if request.method == 'POST':
		r_form = RegisterFrom(request.POST)

		if r_form.is_valid():
			try:
				user = User.objects.get(
					email=r_form.cleaned_data['login']
				)
			except ObjectDoesNotExist:
				message = 'Invalid login'
				return render(request, 'users/login.html', {'form': r_form, 'message': message})

			user.check_password(r_form.cleaned_data['password'])

			request.session['session_id'] = os.urandom(20).hex()
			request.session.modified = True

			message = 'Logged in'
			#return redirect(f'users/{user.id}/', permanent=True)
			return render(request, 'users/login.html', {'form': r_form, 'message': message})
	else:
		r_form = RegisterFrom()
		return render(request, 'users/login.html', {'form': r_form, 'message': message})

def user_page_view(request, user_id=None):
	return HttpResponse(f'User {user_id} page')