from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('blogs/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('comments/', include('comment.urls')),
    path('addgoal/', include('goal.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
