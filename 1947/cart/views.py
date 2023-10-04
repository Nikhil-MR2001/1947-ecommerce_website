from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import CartItem
# Create your views here.

from item.models import Item

def cart(request):
    user = request.user
    item = CartItem.objects.filter(user=user)
    # category = CartItem.type_of

    total_price = 0

    for cart_item in item:
        cart_item.subtotal = cart_item.product.price * cart_item.quantity
        total_price += cart_item.subtotal

    return render(request, './cart/cart.html', {'items' : item, 'total_price' : total_price})

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=item)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/')
def remove_from_cart(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()
    return redirect('/')