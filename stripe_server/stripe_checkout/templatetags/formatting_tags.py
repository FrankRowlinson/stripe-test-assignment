from django import template


register = template.Library()


@register.filter(name="cents_to_dollars")
def cents_to_dollars(value):
    value = value / 100
    return f"{value:0,.2f}"