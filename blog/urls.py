from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('search/', views.search, name='search'),
    path('<int:blog_id>', views.blog, name='blog'),
    path('like/<int:blog_id>', views.liker, name='liker'),
    path('like2/<int:blog_id>', views.liker2, name='liker2'),
    path('addblog', views.addblog, name='addblog'),
    path('publishing', views.publishing, name="publishing")
]
