from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Languages, ObjectiveFeatures, Levels


@admin.register(Languages)
class LanguagesAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)


@admin.register(ObjectiveFeatures)
class ObjectiveFeaturesAdmin(ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)


@admin.register(Levels)
class LevelsAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)
