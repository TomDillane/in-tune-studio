from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ View to return the cart items """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add items to the cart """

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    
    cart[item_id] = item_id

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)