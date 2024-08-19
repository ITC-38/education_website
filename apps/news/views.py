from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext_lazy as _

from apps.news.models import News


class NewsPage(View):
    template_path: str = 'news/pages/index.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            self.template_path,
            {
                'title': _('News'),
                'news': News.objects.all()
            }
        )
