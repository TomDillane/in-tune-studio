from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Product
from .forms import ProductForm


def studio_products(request):
    """ View to return products offered by the studio """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View to return specific product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a room to studio options """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Room added to studio!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Please review the form detail.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit details of a room """
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Please review the form detail.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """ Delete a room """
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Room removed!')
    return redirect(reverse('products'))
