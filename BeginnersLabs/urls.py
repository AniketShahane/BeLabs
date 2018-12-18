from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('blogs/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]
