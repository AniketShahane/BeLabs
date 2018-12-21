from django.contrib import admin
from django.contrib.auth.models import User
from .models import Message  
# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver')
    list_display_links = ('id', 'sender')
    list_filter = ('sender', 'receiver')
    list_perpage = 25 
    
    def get_ordering(self, request):
        return ['id']

admin.site.register(Message, MessageAdmin)