from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect


def logout_required_obj(func):
    def wrapper(self_obj: object, request: HttpRequest, *args, **kwargs):
        if not request.user.is_anonymous:
            messages.info(request, 'Вы уже вошли в систему')
            return redirect('courses:home')
        return func(self_obj, request, *args, **kwargs)
    return wrapper


def login_required_obj(func):
    def wrapper(self_obj: object, request: HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse('Ты не логинился')
        return func(self_obj, request, *args, **kwargs)
    return wrapper
