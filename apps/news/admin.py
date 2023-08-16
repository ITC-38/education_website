from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import News


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('id', 'name', 'created_date',)
    list_display_links = ('name',)
    readonly_fields = ('created_date',)
    search_fields = ('name',)
