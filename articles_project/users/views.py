from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from articles.models import Article

import os

@login_required(login_url='login_page')
def user_page_view(request, user_id=None):
	user = get_object_or_404(User, id=user_id)
	articles = Article.objects.filter(author=user)

	context = {
		'articles':articles, 
		'user': user,
		'is_authenticated': request.user.is_authenticated,
		}
	return render(request, 'users/user.html', context)


@login_required(login_url='login_page')
def user_profile_edit_view(request, user_id):
	user = get_object_or_404(User, id=user_id)

	return HttpResponse(f'User {user_id} profile edit page')
