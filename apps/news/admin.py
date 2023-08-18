from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import News


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'show_news_preview')
    list_display_links = ('name',)
    readonly_fields = ('created_date',)
    search_fields = ('name',)

    def show_news_preview(self, obj: News):
        return mark_safe(f"<img src='{obj.preview.url}' "
                         f"style='height: 75px; width: 100px'></img>")

    show_news_preview.short_description = _('Preview')
    show_news_preview.allow_tags = True
