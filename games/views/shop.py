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
    # l=LineItem.objects.all(game)
    # print(l)
    # customer=Customer.objects.all()
    # cdate=Customer.objects.all(created_date)
    # print(customer)
    # cdate=Customer.objects.count()
    # print(cdate)
    # s=Customer.objects.staff_status()
    # print(s)
 
    games=Game.objects.all()
        # filter function
    g=request.POST.get('gamef')
    print('game: ',g,request)

    if g==None:
      # show data for Wii Sports if no filter requirements are given
      g="Wii Sports"

    else:
      g=g

    sources=Game.objects.filter(name=g)
    # filter get the game
    sources_temp=[]
    for source in sources:
      # sname.append(source.name)
      sources_temp.append(source.na_sales)
      sources_temp.append(source.eu_sales)
      sources_temp.append(source.jp_sales)
      sources_temp.append(source.other_sales)
      sources_temp.append(source.global_sales)
    sources_list=json.dumps(sources_temp)
    sname=g
    print(sources)
    print(sources_temp)

    return render(request, 'games/shop/dashboard.html',{'sources_list':sources_list, 'games':games, 'sname':sname})
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
  '''
  maybe add a message to notify has successfully pay
  '''
  request.session['deleted'] = 'thank you for your purchase'
  return redirect('index' )

def purchase(request):
  if request.user.is_authenticated:
    user = request.user
    basket = Basket(request)
      
    return render(request, 'games/shop/purchase.html', {'basket': basket, 'user': user})
  else:
    return redirect('login')