from django.contrib import admin
from .models import Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'writer',)
    list_display_links = ('id', 'writer')
    list_filter = ('writer',)
    list_perpage = 25

    def get_ordering(self, request):
        return ['id']

admin.site.register(Comment, CommentAdmin)
