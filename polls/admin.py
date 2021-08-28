from django.contrib import admin

from .models import LogModel


@admin.register(LogModel)
class AdminModel(admin.ModelAdmin):
    list_display = ['path', 'method', 'timestamp']
    date_hierarchy = 'timestamp'
    list_filter = ['method']
    search_fields = ['path']
