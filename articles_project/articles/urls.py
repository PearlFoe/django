from django.urls import path

from . import views

urlpatterns = [
    path('<int:article_id>/', views.article_view, name='article_page'),
    path('new/', views.acticle_create_view, name='article_create_page'),
    path('edit/<int:article_id>/', views.article_edit_view, name='article_edit_page'),
]
