from django.db import models


class News(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    preview_url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name
