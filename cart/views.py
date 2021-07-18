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
    

    # print(request.session['cart'])
    return redirect(redirect_url)

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    print("Cart", cart)
    # print(cart[item_id]['items_by_date'])
    # print('Request is ', request)
    # print('item_date is', item_date)
    date = request.POST.get('date-booked')
    # print(date)
    # datedict = list(cart[item_id]['items_by_date'].keys())

    
    if date in cart[item_id]['items_by_date'].values():
        print(date)
        print(cart[item_id]['items_by_date'].values())
        del cart[item_id]['items_by_date'][date]
        print(cart)


        """
        print(cart[item_id]['items_by_date'].values())
        del dictom[date]

        # del cart[item_id]['items_by_date'][key]
        
        """

        """
        if not cart[item_id]['items_by_date']:
                    cart.pop(item_id)

    """


    """
    if date in cart[item_id]['items_by_date'].values():
        del cart[item_id]['items_by_date'][1]
        if not cart[item_id]['items_by_date']:
                    cart.pop(item_id)
    """


    # print(cart.items())
    """
    for k, v in cart.items():
        # print(k)
        # print(v)
        for g, t in v.items():
            print(t)
            if date in t:
                del cart[item_id]['items_by_date'][date]
                if not cart[item_id]['items_by_date']:
                    cart.pop(item_id)
    """
    """
    for date in cart.items():
        
        del cart[item_id]['items_by_date'][date]
        if not cart[item_id]['items_by_date']:
            cart.pop(item_id)
    """
    # del cart[item_id]['items_by_date']['07/15/2021']


    """
    if item_id in list(cart.keys()):
        for t in cart[item_id]['items_by_date'].values():
            for k, v in t():
                print(k)
    """
    
    # for item_id in list(cart.keys()):
    # for key, date in cart.items():
        # for a, b in date:
        # print(date)
    # for key, date in cart.items():
        # date = cart[item_id][date]
        # if date:
        # del cart[item_id][date]
        # if not cart[item_id]['items_by_date']:
            # cart.pop(item_id)
        
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


    
    """
    cart = request.session.get('cart', {})
    date = request.POST.get('date')
    cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    """