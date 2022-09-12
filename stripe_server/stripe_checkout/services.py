from .models import Item
import stripe
from django.conf import settings
from django.urls import reverse


stripe.api_key = settings.STRIPE_SECRET_KEY


def get_checkout_session(request, item_id):
    item = Item.objects.get(pk=item_id)
    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                        'unit_amount': item.price
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('cancel')),
        )
    return checkout_session