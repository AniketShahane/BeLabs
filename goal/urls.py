from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.goal, name='goal'),
    path('<int:goal_id>', views.delgoal, name='delgoal'),
]
