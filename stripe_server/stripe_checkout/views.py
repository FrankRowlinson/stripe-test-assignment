from django.views.generic import DetailView
from django.http import JsonResponse
from django.shortcuts import render

# бизнес-логику спрятал сюда
from .services import *


from django.conf import settings

import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout_session(request, pk):
    # Создается сессия с товаром, который не был инициализирован в stripe dashboard
    checkout_session = get_checkout_session(request, pk)
    return JsonResponse({"session_id": checkout_session.id})


def success(request):
    context = {
        'sessid': request.GET['session_id'],
    }
    return render(request, 'stripe_checkout/success.html', context=context)


def cancel(request):
    return render(request, 'stripe_checkout/cancel.html')


class ItemDetailView(DetailView):
    model = Item
    template_name = "stripe_checkout/item.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['public_key'] = settings.STRIPE_PUBLIC_KEY
        return context
