from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from collections import Counter


def cart_contents(request):

    cart_items = []
    total = 0
    date = 0
    qty = 0
    count = 0
    num = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        for date, qty in item_data['items_by_date'].items():
            product = get_object_or_404(Product, pk=item_id)
            line_total = product.price
            total += line_total
            count = Counter(item_id)
            qty = 1

            cart_items.append({
                'item_id': item_id,
                'date': date,
                'product': product,
                'item_price': line_total,
            })
            # print(cart_items)


    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'grand_total': grand_total,
    }

    return context