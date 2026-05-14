import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from juntagrico.config import Config
from juntagrico.entity.subs import Subscription
from juntagrico.entity.subtypes import SubscriptionType


@login_required
def single(request, subscription_id=None):
    """
    Detail view of a subscription of a member
    """
    member = request.user.member

    if subscription_id is None:
        subscription = member.subscription_current
    else:
        subscription = Subscription.objects.filter(id=subscription_id, subscriptionmembership__member=member).first()

    if not subscription:
        return redirect('subscription-landing')

    # special count in 2026
    date_range = {}
    if subscription.activation_date.year < 2026:
        today = datetime.date.today()
        if today < datetime.date(2026, 5, 1):
            date_range = {
                'start': datetime.date(2025, 5, 1),
                'end': datetime.date(2026, 4, 30),
            }
        elif today < datetime.date(2027, 1, 1):
            date_range = {
                'start': datetime.date(2026, 5, 1),
                'end': datetime.date(2026, 12, 31),
            }

    # count assignments of subscription
    subscription = Subscription.objects.annotate_assignment_counts(
        of_member=member,
        prefix='member_',
        **date_range,
    ).annotate_assignments_progress(**date_range).get(pk=subscription)

    subscription_membership = member.subscriptionmembership_set.get(subscription=subscription)
    return render(request, 'juntagrico/my/subscription/single.html', {
        'member': member,
        'subscription': subscription,
        'subscription_membership': subscription_membership,
        'can_change_part': SubscriptionType.objects.normal().visible().count() > 1,
        'has_extra': SubscriptionType.objects.is_extra().visible().exists(),
        'unit': 'h' if Config.assignment_unit() == 'HOURS' else '',
    })
