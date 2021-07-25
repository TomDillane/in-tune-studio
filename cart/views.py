from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Product
from checkout.models import OrderLineItem

# Create your views here.


def view_cart(request):
    """ View to return the cart items """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add items to cart """

    date = request.POST.get('date')
    product = get_object_or_404(Product, pk=item_id)
    qty = 0
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    
    order_line_date = OrderLineItem.objects.filter(room_date=date)
    room_date = OrderLineItem.objects.filter(product=product)
    # order_line_date = get_object_or_404(OrderLineItem, room_date=date)
    print(order_line_date)
    print(room_date)
    
    
    if order_line_date and room_date:
        messages.info(request, f'This room has already been reserved for this date! Please try another date!')
        return redirect(redirect_url)											


    if item_id in list(cart.keys()):
        if date in cart[item_id]['items_by_date'].values():
            cart[item_id]['items_by_date'][date] = date
            messages.info(request, f'You already have {product.name} booked for {date}!')

        else:
            cart[item_id]['items_by_date'][date] = date
            messages.success(request, f'{product.name} for {date} added to your order!')
    else:
        cart[item_id] = {'items_by_date': {date: date}}
        messages.success(request, f'Added {product.name} to your order!')

    request.session['cart'] = cart
    

    return redirect(redirect_url)

def remove_from_cart(request, item_id):
    """ Add items to cart """

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        date = request.POST.get('date-booked')
    

        if date in cart[item_id]['items_by_date'].values():
            del cart[item_id]['items_by_date'][date]
            messages.success(request, f'{product.name} booked for {date} removed from your order!')


        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return  HttpResponse(status=500)
