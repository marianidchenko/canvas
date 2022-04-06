from django import template

register = template.Library()


@register.filter(name="truncatesmart")
def truncatesmart(value, limit=150):
    try:
        limit = int(limit)
    except ValueError:
        return value
    if len(value) <= limit:
        return value
    value = value[:limit]
    words = value.split(' ')[:-1]
    return ' '.join(words) + '...'


@register.filter
def multiply(value, arg):
    return f"{(value * arg):.2f}"
