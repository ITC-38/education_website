from django import template

register = template.Library()


@register.filter(name='calc_disc')
def calc_discount_price(price: float, discount: int) -> float:
    return price - (price / 100 * discount)
