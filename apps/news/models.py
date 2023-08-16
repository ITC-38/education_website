from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    preview_url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.name
