from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from django.contrib.auth.models import Group
from django.http import HttpRequest

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Professions, UserProfile, Users


class UserProfileInline(TabularInline):
    model = UserProfile
    extra = 0
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профиль'
    can_delete = False


@admin.register(Users)
class CustomUserAdmin(ModelAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'is_superuser', 'is_active',)
    list_filter = ('email', 'is_superuser', 'is_active',)
    search_fields = ('email', 'full_name')
    ordering = ('email',)
    readonly_fields = ('password', 'date_joined', 'last_login')
    exclude = ('groups', 'user_permissions')
    inlines = (UserProfileInline,)

    def get_readonly_fields(self, *args, **kwargs):
        request: HttpRequest = args[0]
        last = request.path.split('/')[-2]
        new_fields = super().get_readonly_fields(*args, **kwargs)
        if last == 'change':
            return new_fields
        return new_fields[1:]


@admin.register(Professions)
class ProfessionsAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)


admin.site.unregister(Group)
