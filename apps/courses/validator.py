from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_discount_percent(discount: int):
    if discount > 100:
        raise ValidationError(_("Discount can't be greater than 100"))
