from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    preview = models.ImageField(upload_to='images/news/previews')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
        verbose_name = _('News')
        verbose_name_plural = _('News')
