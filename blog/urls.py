from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('search/', views.search, name='search'),
    path('<int:blog_id>', views.blog, name='blog'),
]
