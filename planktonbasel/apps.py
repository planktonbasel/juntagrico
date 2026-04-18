from datetime import date
from django.apps import AppConfig


class PlanktonBaselConfig(AppConfig):
    name = 'planktonbasel'
    verbose_name = "Plankton Basel"
    default_auto_field = 'django.db.models.AutoField'

    def ready(self):
        # override required assignment calculation for shortened business year
        from juntagrico.queryset.subscription import SubscriptionQuerySet
        original_annotate_required_assignments = SubscriptionQuerySet.annotate_required_assignments

        def annotate_required_assignments(self, start=None, end=None):
            if end == date(2027, 4, 30):
                end = date(2026, 12, 31)
            return original_annotate_required_assignments(self, start, end)

        SubscriptionQuerySet.annotate_required_assignments = annotate_required_assignments

