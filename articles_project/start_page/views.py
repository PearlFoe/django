from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from articles.models import Article

def index(request):
	articles = Article.objects.all()
	paginator = Paginator(articles, 12) # Show 12 contacts per page.

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'start_page/index.html', {'page_obj': page_obj})
	#return HttpResponse(f'Start page')
