from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='home'),
    path('home/', views.home, name='home'),
    path('atletas/', views.atletas, name='atletas'),
    path('info/', views.info, name='info'),
    path('login/', views.acceder, name='login'),
    path('register/', views.register, name='register'),
    path('exit/', views.salir, name='exit'),

]
