from django.shortcuts import render, redirect
from collections import Counter

# Create your views here.


def view_cart(request):
    """ View to return the cart items """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add items to cart """

    date = request.POST.get('date')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    # cart[item_id] = date
    
    if item_id in list(cart.keys()):
        #cart[item_id]['items_by_date'][bookdate] += date
        if date in cart[item_id]['items_by_date'].keys():
            cart[item_id]['items_by_date'][date] = date
        else:
            cart[item_id]['items_by_date'][date] = date
    else:
        cart[item_id] = {'items_by_date': {date: date}}

    request.session['cart'] = cart

    # count = {k: Counter(k) for k, v in request.session['cart'].items()}


    print(request.session['cart'])
    # print(count)
    return redirect(redirect_url)
