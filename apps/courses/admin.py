from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Languages, ObjectiveFeatures, Levels, Category, InnerCategory, Topics, Requirement


@admin.register(Languages)
class LanguagesAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(ObjectiveFeatures)
class ObjectiveFeaturesAdmin(ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Levels)
class LevelsAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(InnerCategory)
class InnerCategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Topics)
class TopicsAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)
    search_fields = ('name',)
    autocomplete_fields = ('category', 'inner_category',)


@admin.register(Requirement)
class RequirementAdmin(ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    autocomplete_fields = ('topic',)
