from django import template
from khayyam import JalaliDate

register = template.Library()

@register.filter(name='to_jalali')
def to_jalali(value):
    if isinstance(value, (str, int, float)):
        return value
    return JalaliDate(value).strftime('%Y/%m/%d')
