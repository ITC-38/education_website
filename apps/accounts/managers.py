from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import check_password, make_password


class UserManager(BaseUserManager):

    def create_user(self, email: str, password: str, **other_fields):
        valid_email = self.normalize_email(email)
        password_hash = make_password(password)
        model = self.model(
            email=valid_email, password=password_hash,
            **other_fields
        )
        model.save()
        return model

    def create_superuser(self, email: str, password: str, **other_fields):
        model = self.create_user(
            email, password, is_superuser=True, is_staff=True, **other_fields
        )
        return model
