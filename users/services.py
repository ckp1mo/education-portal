import stripe
from users.models import Payment


def get_pay(amount, user):
    stripe.api_key = "sk_test_51OnM35CY5oj99qGal0hpnvPtKv5C9GhMaXPh3OL9oHuVm5jDYfb8rbk9NW4RFODBJePzJRWzJTb8zOANWQYzaQxQ00vpYpTDYL"

    prod = stripe.Product.create(name="Top course")
    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount,
        recurring={"interval": "month"},
        product=prod.get('id'),
    )
    payment_link = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": price.get('id'), "quantity": 2}],
        mode="subscription",
    )

    payment = Payment.objects.create(
        user=user.id,
        payment=price.get('unit_amount'),
        stripe_id=payment_link.get('url')
    )
    return payment
