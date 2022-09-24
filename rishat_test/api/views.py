import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from items.models import Item
from .serializers import ItemSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY

YOUR_DOMAIN = 'http://178.154.192.231'


@api_view(['GET'])
def item_view(request, pk):
    """Отоброжает конкретный предмет по ID."""
    item = get_object_or_404(Item, id=pk)
    serializer = ItemSerializer(item)
    return Response(
        {
            'item': serializer.data,
            'public_key': settings.STRIPE_PUBLIC_KEY
        },
        template_name='item_page.html'
    )


@api_view(['GET'])
def item_buy(request, pk):
    """Формирование и вывод session.id"""
    item = get_object_or_404(Item, id=pk)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': item.price,
                    'product_data': {
                        'name': item.name,
                        'description': item.description[:20],
                    }
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success',
        cancel_url=YOUR_DOMAIN + '/cancel',
    )
    return JsonResponse({'id': checkout_session.id})
