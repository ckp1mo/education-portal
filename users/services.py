import stripe
from django.conf import settings
from users.models import Payment


def get_pay(amount, user, course):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    prod = stripe.Product.create(name=course.title)
    price = stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product=prod.get('id'),
    )
    payment_link = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )

    payment = Payment.objects.create(
        user=user,
        payment=price.get('unit_amount'),
        stripe_id=payment_link.get('url'),
        course=course
    )
    return payment
