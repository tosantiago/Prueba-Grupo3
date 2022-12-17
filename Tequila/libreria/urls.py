from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio.html'),
    path('login.html', views.login, name='login'),
    path('inicio.html', views.inicio, name='inicio.html'),
]
