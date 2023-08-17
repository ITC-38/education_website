from django.urls import path

from . import views as acc_v


app_name = 'accounts'
urlpatterns = [
    path('', acc_v.AuthPage.as_view(), name='auth_page'),
    path('login/', acc_v.LoginView.as_view(), name='login'),
    path('signup/', acc_v.SignupView.as_view(), name='signup'),
]
