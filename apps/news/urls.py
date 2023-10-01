from django.urls import path

from apps.news.views import NewsPage


app_name = 'news'
urlpatterns = [
    path('', NewsPage.as_view(), name='home')
]
