from django.contrib import admin
from .models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'author')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    list_editable = ('is_published',)
    list_perpage = 25
    search_fields = ('title', 'body')

    def get_ordering(self, request):
        #This function orders the way the admin page shows the blogs
        return ['id']

admin.site.register(Blog, BlogAdmin)
