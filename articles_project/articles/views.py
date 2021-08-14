from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_view(request, article_id=None):
	return HttpResponse(f'Article {article_id} page')


@login_required(login_url='login_page')
def acticle_create_view(request):
	return HttpResponse(f'Article create page')


@login_required(login_url='login_page')
def article_edit_view(request, article_id=None):
	return HttpResponse(f'Article {article_id} edit page')

