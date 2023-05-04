from django.shortcuts import redirect, render, get_object_or_404
from games.models import Game, Cart, Customer, LineItem, Order
from games.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from games.views.basket import Basket
import json

def signup(request):
  form = SignUpForm(request.POST)
  if form.is_valid():
    user = form.save()
    user.refresh_from_db()
    user.customer.first_name = form.cleaned_data.get('first_name')
    user.customer.last_name = form.cleaned_data.get('last_name')
    user.customer.address = form.cleaned_data.get('address')
    user.save()
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password= password)
    login(request, user)
    return redirect('/')
  return render(request, 'games/shop/signup.html', {'form': form})

@login_required
def dashboard(request):
  user = request.user
  if user.is_authenticated & user.is_staff:
    # a=Customer.objects.all()
    # a=Model.
    # print(a)
    #https://stackoverflow.com/questions/15635790/how-to-count-the-number-of-rows-in-a-database-table-in-django
    an=Customer.objects.filter(user_type ="Admin").count()
    print('*************',an,"***********************")
    sn=Customer.objects.filter(user_type ="Staff").count()
    print('---------------',sn,"-----------------")
    cn=Customer.objects.filter(user_type ="Customer").count()
    print('============',cn,"=============")
    
    return render(request, 'games/shop/dashboard.html',{'an':an, 'sn':sn, 'cn':cn})
  else:
    return redirect('login')

# save order, clear basket and thank customer
def payment(request):
  basket = Basket(request)
  user = request.user
  customer = get_object_or_404(Customer, user_id=user.id)
  order = Order.objects.create(customer=customer)
  order.refresh_from_db()
  for item in basket:
    game_item = get_object_or_404(Game, id=item['game_id'])
    cart = Cart.objects.create(game = game_item, quantity=item['quantity'])
    cart.refresh_from_db()
    line_item = LineItem.objects.create(quantity=item['quantity'], game=game_item, cart=cart,  order = order)
  
  basket.clear()
  request.session['deleted'] = 'Thank you for your purchase'
  return redirect('index')

def purchase(request):
  if request.user.is_authenticated:
    user = request.user
    basket = Basket(request)
      
    return render(request, 'games/shop/purchase.html', {'basket': basket, 'user': user})
  else:
    return redirect('login')