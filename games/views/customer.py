from django.shortcuts import redirect, render, get_object_or_404
from games.models import Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def customer_list(request):
    user = request.user
    if user.is_authenticated & user.is_staff:
        users = User.objects.all()
        return render(request, 'games/shop/customer_list.html', {'users' : users})
    else:
        return redirect('games:login')

@login_required
def customer_detail(request, id):
    user = get_object_or_404(User, id=id)
    orders=Order.objects.filter(customer_id=id)
    return render(request, 'games/shop/customer_detail.html', {'user' : user, 'orders' : orders})
