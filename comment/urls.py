from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:blog_id>', views.comment, name='comment')
]
