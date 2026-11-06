from django import template

register = template.Library()

@register.filter(name='to_persian')
def to_persian(value):
    if value is None:
        return ''
    # تبدیل اعداد انگلیسی به فارسی
    english_digits = '0123456789'
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    translation_table = str.maketrans(english_digits, persian_digits)
    return str(value).translate(translation_table)