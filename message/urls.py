from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:receiver_id>', views.message, name='message'),
    path('sendmsg', views.sendmsg, name='sendmsg'),
    path('sendmsg2/<int:receiver_id>', views.sendmsg2, name='sendmsg2'),
]