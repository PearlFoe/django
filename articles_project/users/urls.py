from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.user_page_view, name='user_personal_page'),
]
