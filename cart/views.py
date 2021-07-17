from django.shortcuts import render, redirect, reverse
from collections import Counter

# Create your views here.


def view_cart(request):
    """ View to return the cart items """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add items to cart """

    date = request.POST.get('date')
    qty = 0
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})


    if item_id in list(cart.keys()):
        if date in cart[item_id]['items_by_date'].values():
            cart[item_id]['items_by_date'][date] = date

        else:
            cart[item_id]['items_by_date'][date] = date
    else:
        cart[item_id] = {'items_by_date': {date: date}}

    request.session['cart'] = cart
    

    print(request.session['cart'])
    return redirect(redirect_url)

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    for item_id in list(cart.keys()):
        for date in list(cart[item_id]['items_by_date'].values()):
            # date = cart[item_id]['items_by_date'][date]
            cart.pop(date)
            if not cart[item_id]['items_by_date']:
                cart.pop(item_id)
            print(date)
    

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

    



    """
    cart = request.session.get('cart', {})
    date = request.POST.get('date')
    cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    """