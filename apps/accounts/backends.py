from typing import Union

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


Users = get_user_model()


class AccountsAuthBackend(BaseBackend):

    def authenticate(
        self, request, *, email=None,
        password=None, **kwargs
    ) -> Users | None:
        if any([not email, not password]):
            return
        user = self.get_user(email)
        if not user:
            return
        if all([
            user.check_password(password),
            self.user_can_authenticate(user)
        ]):
            return user

    def get_user(self, unique_field: Union[str, int]) -> Users | None:
        if isinstance(unique_field, str):
            user = Users.objects.filter(email=unique_field).first()
        else:
            user = Users.objects.filter(pk=unique_field).first()
        return user

    def user_can_authenticate(self, user) -> bool:
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, "is_active", None)
        return is_active or is_active is None
