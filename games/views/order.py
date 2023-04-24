from django.shortcuts import render, get_object_or_404
from games.models import LineItem, Order
from django.contrib.auth.models import User

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'games/shop/order_list.html', {'orders' : orders})

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    customer = order.customer
    user = get_object_or_404(User, id=customer.pk)
    line_items = LineItem.objects.filter(order_id=order.id)
    return render(request, 'games/shop/order_detail.html', {'order' : order, 'user': user, 'line_items': line_items})
