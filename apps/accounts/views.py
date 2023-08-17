from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from . import forms as acc_forms
from .models import Users
from .utils import logout_required_obj


class AuthPage(View):
    template_path: str = 'accounts/pages/auth.html'

    @logout_required_obj
    def get(self, request: HttpRequest) -> HttpResponse:
        signup_form = acc_forms.SignupForm()
        login_form = acc_forms.LoginForm()
        return render(
            request, self.template_path,
            context={
                'title': 'Регистрация/Вход',
                'signup_form': signup_form,
                'login_form': login_form,
            }
        )


class LoginView(View):

    @logout_required_obj
    def post(self, request: HttpRequest) -> HttpResponse:
        login_form = acc_forms.LoginForm(request.POST)
        if not login_form.is_valid():
            errors_list = login_form.errors.values()
            for error_lst in errors_list:
                messages.error(request, error_lst[0])
            return redirect('accounts:auth_page')
        user = authenticate(**login_form.cleaned_data)
        if not user:
            messages.info(request, 'Неверный email или пароль')
            return redirect('accounts:auth_page')
        login(request, user)
        messages.success(request, 'Вы успешно вошли на свой аккаунт')
        return redirect('accounts:auth_page')


class SignupView(View):

    @logout_required_obj
    def post(self, request: HttpRequest) -> HttpResponse:
        signup_form = acc_forms.SignupForm(request.POST)
        if not signup_form.is_valid():
            errors_list = signup_form.errors.values()
            for error_lst in errors_list:
                messages.error(request, error_lst[0])
            return redirect('accounts:auth_page')
        password1 = signup_form.cleaned_data.get('password')
        password2 = signup_form.cleaned_data.get('password2')
        if password1 != password2:
            messages.info(request, 'Пароли не совпадают')
            return redirect('accounts:auth_page')
        user: Users = signup_form.save(commit=False)
        user.set_password(password1)
        user.save()
        messages.success(
            request,
            'Вы успешно зарегистрировались, теперь войдите в систему'
        )
        return redirect('accounts:auth_page')
