from django.db import models
from django.utils.translation import gettext_lazy as _


class Languages(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )

    slug = models.SlugField(
        unique=True
    )

    native = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')


class ObjectiveFeatures(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )

    class Meta:
        verbose_name = _('Objective Feature')
        verbose_name_plural = _('Objective Features')


class Levels(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )

    slug = models.SlugField(
        unique=True
    )

    class Meta:
        verbose_name = _('Level')
        verbose_name_plural = _('Levels')
