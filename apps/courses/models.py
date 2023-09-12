from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.courses.utils import (
    user_course_photo_upload_path,
    user_courses_upload_path
)
from apps.courses.validator import validate_discount_percent


class Languages(models.Model):
    name = models.CharField(
        _('Language name'),
        max_length=64,
        unique=True
    )
    slug = models.SlugField(
        _('URL'),
        unique=True
    )
    native = models.BooleanField(
        _('Native'),
        default=True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')


class ObjectiveFeatures(models.Model):
    name = models.CharField(
        _('Objective Feature name'),
        max_length=64,
        unique=True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('Objective Feature')
        verbose_name_plural = _('Objective Features')


class Levels(models.Model):
    name = models.CharField(
        _('Level name'),
        max_length=64,
        unique=True
    )
    slug = models.SlugField(
        _('URL'),
        unique=True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

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
        _('URL'),
        unique=True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

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
        _('URL'),
        unique=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_('Category'),
        on_delete=models.CASCADE,
        related_name='inner_categories'
    )
    preview = models.ImageField(
        upload_to='photos/inner_categories',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('Inner category')
        verbose_name_plural = _('Inner categories')


class Requirement(models.Model):
    name = models.CharField(
        _('Requirement name'),
        max_length=64,
        unique=True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('Requirement')
        verbose_name_plural = _('Requirements')


class Courses(models.Model):
    name = models.CharField(_('Name'), max_length=128)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Author'),
        related_name='author_courses',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        _('Price'),
        max_digits=6,
        decimal_places=2
    )
    discount = models.IntegerField(
        _('Discount'), validators=[validate_discount_percent]
    )
    description = models.TextField(_('Description'))
    category = models.ForeignKey(
        InnerCategory,
        verbose_name=_('Category'),
        related_name='category_courses',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    level = models.ForeignKey(
        Levels,
        verbose_name=_('Level'),
        related_name='level_courses',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    language = models.ForeignKey(
        Languages,
        verbose_name=_('Language'),
        related_name='language_courses',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    programming_language = models.ForeignKey(
        Languages,
        verbose_name=_('programming language'),
        related_name='p_language_courses',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    preview_url = models.ImageField(
        _('Preview'),
        upload_to=user_course_photo_upload_path
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


class CourseModules(models.Model):
    name = models.CharField(_('Name'), max_length=128)
    course = models.ForeignKey(
        Courses,
        verbose_name=_('Course'),
        related_name='course_modules',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('Course module')
        verbose_name_plural = _('Courses modules')


class ModuleLessons(models.Model):
    module = models.ForeignKey(
        CourseModules,
        verbose_name=_('Module'),
        related_name='module_lessons',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        _('Name'), max_length=128
    )
    video = models.FileField(upload_to=user_courses_upload_path)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('Module lesson')
        verbose_name_plural = _('Module lessons')
