import datetime

from django.template.loader_tags import register
from juntagrico.templatetags.juntagrico import widgets


@register.simple_tag
def assignment_progress(member, future=None, start=None, end=None, subscription=None):
    sub = subscription or member.subscription_current
    if sub is not None and sub.activation_date.year < 2026:
        today = datetime.date.today()
        if today < datetime.date(2026, 5, 1):
            start = datetime.date(2025, 5, 1)
            end = datetime.date(2026, 4, 30)
        elif today < datetime.date(2027, 1, 1):
            start = datetime.date(2026, 5, 1)
            end = datetime.date(2026, 12, 1)
    return widgets.assignment_progress(member, future, start, end, subscription)
