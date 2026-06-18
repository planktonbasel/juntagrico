from django.contrib import admin
from juntagrico.entity.subs import SubscriptionPart


class SubscriptionPartAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subscription', 'type',
                    'creation_date', 'activation_date', 'cancellation_date', 'deactivation_date']
    search_fields = ['type__name', 'type__long_name', 'type__size__name']
    autocomplete_fields = ['subscription', 'type']
    list_filter = [('type', admin.RelatedOnlyFieldListFilter)]


admin.site.register(SubscriptionPart, SubscriptionPartAdmin)
