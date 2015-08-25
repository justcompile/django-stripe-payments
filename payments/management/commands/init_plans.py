import decimal

from django.conf import settings
from django.core.management.base import BaseCommand
from payments.models import PaymentPlan

import stripe


class Command(BaseCommand):

    help = "Make sure your Stripe account has the plans"

    def handle(self, *args, **options):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        for plan in PaymentPlan.objects.all():
            if plan.stripe_plan_id:
                price = plan.price
                if isinstance(price, decimal.Decimal):
                    amount = int(100 * price)
                else:
                    amount = int(100 * decimal.Decimal(str(price)))

                try:
                    plan_name = plan.name
                    plan_id = plan.stripe_plan_id

                    stripe.Plan.create(
                        amount=amount,
                        interval=plan.interval,
                        name=plan_name,
                        currency=plan.currency.lower(),
                        trial_period_days=plan.trial_period_days,
                        id=plan_id
                    )
                    print("Plan created for {0}".format(plan))
                except Exception as e:
                    print("{0} ({1}): {2}".format(plan_name, plan_id, e))
