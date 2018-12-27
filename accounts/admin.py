from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_bom')
    list_display_links = ('id', 'user')
    list_editable = ('is_bom',)
    list_perpage = 25
    list_filter = ('user',)

    def get_ordering(self, request):
        return ['id']


admin.site.register(Profile, ProfileAdmin)
