import decimal
from payments.models import PaymentPlan

PLANS = [
    PaymentPlan(name='Free Plan', key='free'),
    PaymentPlan(**{
            "stripe_plan_id": "entry-monthly",
            "name": "Entry ($9.54/month)",
            "key": 'entry',
            "description": "The entry-level monthly subscription",
            "price": 9.54,
            "interval": "month",
            "currency": "usd"
        }),
    PaymentPlan(**{
            "stripe_plan_id": "pro-monthly",
            "name": "Pro ($19.99/month)",
            "key": 'pro',
            "description": "The pro-level monthly subscription",
            "price": 19.99,
            "interval": "month",
            "currency": "usd"
        }),
    PaymentPlan(**{
            "stripe_plan_id": "premium-monthly",
            "name": "Gold ($59.99/month)",
            "key": 'premium',
            "description": "The premium-level monthly subscription",
            "price": decimal.Decimal("59.99"),
            "interval": "month",
            "currency": "usd"
        })
]