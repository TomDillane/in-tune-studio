from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from collections import Counter


def cart_contents(request):

    cart_items = []
    total = 0
    date = 0
    count = 0
    num = 0
    cart = request.session.get('cart', {})

    for item_id, date in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        count = Counter(item_id)

        for k, v in count.items():
            num = v
        item_price = product.price * num

        # product_count = 3
        cart_items.append({
            'item_id': item_id,
            'date': date,
            'product': product,
            'num': num,
            'item_price': item_price,
        })


    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'grand_total': grand_total,
    }

    return context
