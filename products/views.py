from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


# studio room options
def studio_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


# move into specific room to book
def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


#  owner can add new room
@login_required
def add_product(request):
    # checks if user is owner
    if not request.user.is_superuser:
        messages.error(request, 'Reserved for In Tune Studio use!')
        return redirect(reverse('home'))

    # if form good, adds room
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Room added to studio!')
            return redirect(reverse('product_detail', args=[product.id]))
        # handles if form error
        else:
            messages.error(request, 'Please review the form detail.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# owner can update room detail
@login_required
def edit_product(request, product_id):
    # checks if user is owner
    if not request.user.is_superuser:
        messages.error(request, 'Reserved for In Tune Studio use!')
        return redirect(reverse('home'))

    # allows update if form is good
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        # handles if form error
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


# owner can update room detail
@login_required
def delete_product(request, product_id):
    # checks if user is owner
    if not request.user.is_superuser:
        messages.error(request, 'Reserved for In Tune Studio use!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Room removed!')
    return redirect(reverse('products'))
