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


class Category(models.Model):
    name = models.CharField(
        _('Category name'),
        max_length=64,
        unique=True
    )

    slug = models.SlugField(
        'URL',
        unique=True
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class InnerCategory(models.Model):
    name = models.CharField(
        _('Inner category name'),
        max_length=64,
        unique=True
    )

    slug = models.SlugField(
        'URL',
        unique=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='inner_categories'
    )

    class Meta:
        verbose_name = _('Inner category')
        verbose_name_plural = _('Inner categories')


class Topics(models.Model):
    name = models.CharField(
        _('Topic name'),
        max_length=64,
        unique=True
    )

    slug = models.SlugField(
        'URL',
        unique=True
    )

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')


class Requirement(models.Model):
    name = models.CharField(
        _('Requirement name'),
        max_length=64,
        unique=True
    )

    class Meta:
        verbose_name = _('Requirement')
        verbose_name_plural = _('Requirements')
