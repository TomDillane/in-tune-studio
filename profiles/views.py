from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from checkout.models import Order


# user profile, user must be logged in
@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    # updates profile if form good
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
        # handles form issues
        else:
            messages.error(request, 'Please review form details!')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


# order history of user
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past order.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
