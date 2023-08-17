from django.http import HttpRequest, HttpResponse


def logout_required_obj(func):
    def wrapper(self_obj: object, request: HttpRequest, *args, **kwargs):
        if not request.user.is_anonymous:
            return HttpResponse('Ты уже логинился')
        return func(self_obj, request, *args, **kwargs)
    return wrapper
