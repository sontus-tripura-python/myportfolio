from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about_list, name='about_list'),
    path('portfolio/', views.portfolio, name='portfolio'),

]
