from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    name = models.CharField(_("News name"), max_length=200)
    description = models.TextField(
        _("News description"),
        blank=True
    )
    created_date = models.DateTimeField(
        _("Created date name "),
        auto_now_add=True
    )
    preview = models.ImageField(
        _("Preview"),
        upload_to='images/news/previews'
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
        verbose_name = _('News')
        verbose_name_plural = _('News')
