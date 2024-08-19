from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views import View

from apps.accounts.models import Users
from apps.courses.models import Courses, InnerCategory
from apps.news.models import News


class HomeView(View):
    template_path: str = 'courses/pages/index.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        category_slug = request.GET.get('category')
        if category_slug:
            trending_courses = Courses.objects.filter(
                category__slug=category_slug
            ).select_related('category', 'author').all()
        else:
            trending_courses = Courses.objects.select_related('category', 'author').all()
        courses_count = Courses.objects.count()
        users_count = Users.objects.count()
        return render(
            request,
            self.template_path,
            context={
                'title': _('Main Page'),
                'categories': InnerCategory.objects.all(),
                'courses_count': courses_count,
                'users_count': users_count,
                'news': News.objects.all(),
                'active_category_slug': category_slug,
                'trending_courses': trending_courses
            }
        )
