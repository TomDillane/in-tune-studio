from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ View to return the cart items """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add items to the cart """

    date = request.POST.get('date')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    
    cart[item_id] = date

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)