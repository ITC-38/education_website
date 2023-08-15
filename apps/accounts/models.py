from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.accounts.managers import UserManager


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'email', unique=True
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    is_staff = models.BooleanField(_('staff status'), default=False)
    full_name = models.CharField(
        _('Full name'), blank=True,
        null=True, max_length=64
    )
    date_joined = models.DateTimeField(
        _('Joined date'), default=timezone.now
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Professions(models.Model):

    name = models.CharField(
        _('Profession name'),
        max_length=64,
        unique=True
    )
    slug = models.SlugField(
        'URL',
        unique=True
    )

    class Meta:
        verbose_name = _('Profession')
        verbose_name_plural = _('Professions')


class UserProfile(models.Model):

    user = models.ForeignKey(
        Users, verbose_name=_('User'),
        related_name='user_profile',
        on_delete=models.CASCADE, unique=True
    )
    avatar = models.ImageField(
        _('Avatar'),
        upload_to='photos/avatars/users'
    )
    profession = models.ForeignKey(
        Professions, verbose_name=_('User profession'),
        related_name='profession_users', on_delete=models.SET_NULL,
        null=True, blank=True
    )
