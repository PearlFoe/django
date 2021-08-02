from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.user_page_view),
    path('login/', views.login),
    path('registration/', views.register),
]
