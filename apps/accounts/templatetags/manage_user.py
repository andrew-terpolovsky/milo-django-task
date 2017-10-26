import datetime

from django import template

register = template.Library()


@register.simple_tag
def bizz_fuzz(num):
    """
    BizzFuzz template tag.
    :param num: Integer
    :return: String or number depends on multiples conditions.
    """
    output = ''
    if num % 3 == 0:
        output += 'Bizz'
    if num % 5 == 0:
        output += 'Fuzz'
    return output or num


@register.simple_tag
def allowed(b):
    """
    Template tag check if user older when 13.
    :param b: user birthday: datetime.date variable
    :return: String option ('allowed', 'blocked')
    """
    if not isinstance(b, datetime.date):
        return None
    today = datetime.date.today()
    print(today.year - b.year - ((today.month, today.day) < (b.month, b.day)) > 13)
    return 'allowed' if today.year - b.year - ((today.month, today.day) < (b.month, b.day)) > 13 else 'blocked'
