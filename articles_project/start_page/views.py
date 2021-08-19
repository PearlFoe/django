from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from articles.models import Article

def index(request):
	articles = Article.objects.all()
	paginator = Paginator(articles, 12) # Show 12 contacts per page.

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	page_range = _get_page_range(page_number, page_obj)

	return render(request, 'start_page/index.html', {'page_obj': page_obj, 'page_range':page_range})


def _get_page_range(current_page, page_obj):
	page_range = []
	
	if not current_page:
		current_page = 1

	if current_page - page_obj.start_index() > 4:
		for page_number in range(current_page - 3, current_page):
			page_range.append(page_number)
	else:
		for page_number in range(page_obj.start_index(), current_page):
			page_range.append(page_number)

	if page_obj.end_index() - current_page > 4:
		for page_number in range(current_page, current_page + 3):
			page_range.append(page_number)
	else:
		for page_number in range(current_page, page_obj.end_index()):
			page_range.append(page_number)

	return page_range