import stripe

from users.models import Payment


def get_pay(amount, user):
    stripe.api_key = 'sk_test_51OnM35CY5oj99qGal0hpnvPtKv5C9GhMaXPh3OL9oHuVm5jDYfb8rbk9NW4RFODBJePzJRWzJTb8zOANWQYzaQxQ00vpYpTDYL'
    pay = stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
        automatic_payment_methods={"enabled": True}
    )

    payment = Payment.objects.create(
        user=user,
        amount=amount,
        stripe_id=pay.id
    )

    return payment
