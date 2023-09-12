from django.urls import path
from . import views

app_name: str = 'courses'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
