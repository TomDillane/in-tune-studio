from django.shortcuts import render
from .models import Product

# Create your views here.

def studio_products(request):
    """ View to return products offered by the studio """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)
