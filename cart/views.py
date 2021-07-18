from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

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


    if item_id in list(cart.keys()):
        if date in cart[item_id]['items_by_date'].values():
            cart[item_id]['items_by_date'][date] = date
            messages.success(request, f'Added {product.name} to your order!')

        else:
            cart[item_id]['items_by_date'][date] = date
            messages.success(request, f'Added {product.name} to your order!')
    else:
        cart[item_id] = {'items_by_date': {date: date}}
        messages.success(request, f'Added {product.name} to your order!')

    request.session['cart'] = cart
    

    return redirect(redirect_url)

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    print("Cart", cart)
    date = request.POST.get('date-booked')
    

    if date in cart[item_id]['items_by_date'].values():
        print(date)
        print(cart[item_id]['items_by_date'].values())
        del cart[item_id]['items_by_date'][date]
        print(cart)


    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
