from django.contrib import admin
from .models import Goal
# Register your models here.
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'goal', 'writer')
    list_display_links = ('id', 'goal')
    list_filter = ('writer',)
    list_perpage = 25

    def get_ordering(self, request):
        return ['id']

admin.site.register(Goal, GoalAdmin)
