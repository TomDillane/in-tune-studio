from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from products.models import Product
from checkout.models import OrderLineItem


# view to return cart
def view_cart(request):

    return render(request, 'cart/cart.html')


# add to cart function
def add_to_cart(request, item_id):

    reserve = request.POST.get('date')
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # check if room and date already exist in another order
    if reserve and item_id:
        order_line_date = OrderLineItem.objects.filter(
            room_date=reserve,
            product=item_id
        )
    else:
        return redirect(redirect_url)

    # if in another order, prevent booking
    if order_line_date:
        messages.info(
            request, f'{product.name} has already been reserved for this date! \
                     Please try another date!')
        return redirect(redirect_url)

    # checks item and date, prevents bookding if already in cart
    if item_id in list(cart.keys()):
        if reserve in cart[item_id]['items_by_date'].values():
            cart[item_id]['items_by_date'][reserve] = reserve
            messages.info(request, f'You already have \
                            {product.name} booked for {reserve}!')

        # if not in cart, adds to cart
        else:
            cart[item_id]['items_by_date'][reserve] = reserve
            messages.success(request, f'{product.name} for {reserve} added \
                                to your order!')
    # if cart no cart, creates cart and adds item and date to cart
    else:
        cart[item_id] = {'items_by_date': {reserve: reserve}}
        messages.success(request, f'Added {product.name} to your order!')

    request.session['cart'] = cart

    return redirect(redirect_url)


# remove item from cart
def remove_from_cart(request, item_id):

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        reserve = request.POST.get('date-booked')

        # looks for date in cart with item id and deletes date
        if reserve in cart[item_id]['items_by_date'].values():
            del cart[item_id]['items_by_date'][reserve]
            messages.success(request, f'{product.name} booked for \
                                {reserve} removed from your order!')

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
