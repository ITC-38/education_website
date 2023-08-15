from django.db import models


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
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class ObjectiveFeatures(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )

    class Meta:
        verbose_name = 'Objective feature'
        verbose_name_plural = 'Objective features'


class Levels(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )

    slug = models.SlugField(
        unique=True
    )

    class Meta:
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'
