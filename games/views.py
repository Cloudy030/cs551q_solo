from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from games.models import Year, Genre, Platform, Publisher, Game,  Cart, Customer, LineItem, Order
from games.forms import SignUpForm, BasketAddProductForm, GameForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
import json


# Create your views here.
def index(request):

    # show every data in table
    games=Game.objects.all()

    # for 4 dropdown search bar
    platforms=Platform.objects.all()
    years=Year.objects.all()
    genres=Genre.objects.all()
    publishers=Publisher.objects.all()

    content=games
    # print(game.publisher.id)

    return render(request, 'games/base/game_full_list.html', {'games':games, 'platforms':platforms, 'years':years, 'genres':genres, 'publishers':publishers})

def gamefilter(request):

    # base before every filter
    games=Game.objects.all()

    # for drop down search bar
    platforms=Platform.objects.all()
    years=Year.objects.all()
    genres=Genre.objects.all()
    publishers=Publisher.objects.all()

    # filter function
    pl=request.POST.get('plfilter')
    print('platform: ',pl,request)
    y=request.POST.get('yfilter')
    print('year: ',y,request)
    g=request.POST.get('gfilter')
    print('genre: ',g,request)
    pu=request.POST.get('pufilter')
    print('publisher: ',pu,request)

    # 0 filter
    if pl==None and y==None and g==None and pu==None:
        filgame=games
        # show all data rows if no filter requirements are given

    # 1 filter
    elif y==None and g==None and pu==None:
        filgame=Game.objects.filter(platform__platform_name=pl)
            # https://stackoverflow.com/questions/67988454/field-id-expected-a-number-but-got
    elif pl==None and g==None and pu==None:
        filgame=Game.objects.filter(year__year_no=y)
    elif pl==None and y==None and pu==None:
        filgame=Game.objects.filter(genre__genre_name=g)
    elif pl==None and y==None and g==None:
        filgame=Game.objects.filter(publisher__publisher_name=pu)

    # 2 filter
    elif g==None and pu==None:
        filgame=Game.objects.filter(platform__platform_name=pl).filter(year__year_no=y)
    elif y==None and pu==None:
        filgame=Game.objects.filter(platform__platform_name=pl).filter(genre__genre_name=g)
    elif y==None and g==None:
        filgame=Game.objects.filter(platform__platform_name=pl).filter(publisher__publisher_name=pu)
    
    elif pl==None and pu==None:
        filgame=Game.objects.filter(year__year_no=y).filter(genre__genre_name=g)
    elif pl==None and g==None:
        filgame=Game.objects.filter(year__year_no=y).filter(publisher__publisher_name=pu)

    elif pl==None and y==None:
        filgame=Game.objects.filter(genre__genre_name=g).filter(publisher__publisher_name=pu)

    # 3 filter
    elif pl==None:
        filgame=Game.objects.filter(year__year_no=y).filter(genre__genre_name=g).filter(publisher__publisher_name=pu)
    elif y==None:
        filgame=Game.objects.filter(platform__platform_name=pl).filter(genre__genre_name=g).filter(publisher__publisher_name=pu)
    elif g==None:
        filgame=Game.objects.filter(platform__platform_name=pl).filter(year__year_no=y).filter(publisher__publisher_name=pu)
    elif pu==None:
        filgame=Game.objects.filter(platform__platform_name=pl).filter(year__year_no=y).filter(genre__genre_name=g)
    
    # 4 filter
    else:
        filgame=Game.objects.filter(platform__platform_name=pl).filter(year__year_no=y).filter(genre__genre_name=g).filter(publisher__publisher_name=pu)
    
    return render(request, 'games/base/game_filter_list.html', {'filgame':filgame, 'games':games, 'platforms':platforms, 'years':years, 'genres':genres, 'publishers':publishers})

def year(request):
    years=Year.objects.all()
    return render(request, 'games/base/year.html', {'years':years})

def yeargame(request,id):
    # games=Game.objects.all()
    # years.Year.objects.all()
    year=get_object_or_404(Year,id=id)
    games=Game.objects.filter(year__id=id)
    return render(request, 'games/base/year_game.html', {'year': year, 'games':games})

def genre(request):
    genres=Genre.objects.all()
    return render(request, 'games/base/genre.html', {'genres':genres})

def genregame(request,id):
    # games=Game.objects.all()
    # genres=Genre.objects.all()
    genre=get_object_or_404(Genre,id=id)
    games=Game.objects.filter(genre__id=id)
    return render(request, 'games/base/genre_game.html', {'genre':genre, 'games':games})

def platform(request):
    platforms=Platform.objects.all()
    return render(request, 'games/base/platform.html', {'platforms':platforms})

def platformgame(request,id):
    # game=get_object_or_404(Game,id=id)
    # publishers=Publisher.objects.all()
    platform=get_object_or_404(Platform,id=id)
    games=Game.objects.filter(platform__id=id)
    return render(request, 'games/base/platform_game.html', {'platform':platform, 'games':games})

def publisher(request):
    publishers=Publisher.objects.all()
    return render(request, 'games/base/publisher.html', {'publishers':publishers})

def pugame(request,id):
    # games=Game.objects.all()
    # publishers=Publisher.objects.all()
    publisher=get_object_or_404(Publisher,id=id)
    games=Game.objects.filter(publisher__id=id)
    print("publisher: ",id, request)
    return render(request, 'games/base/publisher_game.html', {'publisher':publisher, 'games':games})

def gamedetail(request,id):
    # games=Game.objects.all()
    game=get_object_or_404(Game,id=id)
    basket_product_form=BasketAddProductForm()
    return render(request, 'games/base/game_detail.html', {'game':game, 'basket_product_form':basket_product_form})

# def game_list(request):
#     games=Game.obejcts.all()
#     deleted=request.session.get('deleted', 'empty')
#     request.session['deleted']='hello'

#     return render(request, 'index.html', {'games': games, 'deleted': deleted})

# def game_delete(request, id):
#     game=get_object_or_404(Game, id=id)
#     deleted=request.session.get('deleted', 'empty')
#     request.session['deleted']=game.name
#     game.delete()
#     return redirect('index')

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
        
        games=Game.objects.all()
            # filter function
        g=request.POST.get('gamef')
        print('game: ',g,request)

        # # 0 filter
        # if pl==None and y==None and g==None and pu==None:
        #     filgame=games
        #     # show all data rows if no filter requirements are given

        # 1 filter
        if g==None:
            # show data for Wii Sports if no filter requirements are given
            sources=Game.objects.filter(name="Wii Sports")
            sources_temp=[]
            for source in sources:
                # sources_temp.append(source.name)
                sources_temp.append(source.na_sales)
                sources_temp.append(source.eu_sales)
                sources_temp.append(source.jp_sales)
                sources_temp.append(source.other_sales)
                sources_temp.append(source.global_sales)
            sources_list=json.dumps(sources_temp) # convert to json
            print(sources)
            print(sources_temp)

        else:
            sources=Game.objects.filter(name=g)
            # filter get the game
            sources_temp=[]
            for source in sources:
                # sources_temp.append(source.name)
                sources_temp.append(source.na_sales)
                sources_temp.append(source.eu_sales)
                sources_temp.append(source.jp_sales)
                sources_temp.append(source.other_sales)
                sources_temp.append(source.global_sales)
            sources_list=json.dumps(sources_temp)
            print(sources)
            print(sources_temp)

        # sources=Game.objects.filter(name='Wii Sports')
        # sources_temp=[]
        # for source in sources:
        #     # sources_temp.append(source.name)
        #     sources_temp.append(source.na_sales)
        #     sources_temp.append(source.eu_sales)
        #     sources_temp.append(source.jp_sales)
        #     sources_temp.append(source.other_sales)
        #     sources_temp.append(source.global_sales)
        # sources_list=json.dumps(sources_temp)
        # print(sources)
        # print(sources_temp)

        return render(request, 'games/shop/dashboard.html',{'sources_list':sources_list, 'sources':sources, 'games':games})
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
    request.session['deleted'] = 'thanks for your purchase'
    return redirect('index' )

def purchase(request):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket(request)
        
        return render(request, 'games/shop/purchase.html', {'basket': basket, 'user': user})
    else:
        return redirect('login')

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

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'games/shop/order_list.html', {'orders' : orders})

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    customer = order.customer
    user = get_object_or_404(User, id=customer.pk)
    line_items = LineItem.objects.filter(order_id=order.id)
    return render(request, 'games/shop/order_detail.html', {'order' : order, 'user': user, 'line_items': line_items})


# def game_list(request):
#     games = Game.objects.all()    
#     return render(request, 'games/game_list.html', {'games' : games })

def game_detail(request, id):
    game = get_object_or_404(Game, id=id)
    basket_product_form = BasketAddProductForm()
    return render(request, 'games/shop/games_detail.html', {'game' : game, 'basket_product_form': basket_product_form })

# def game_new(request):
#     if request.method=="POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             game = form.save(commit=False)
#             game.created_date = timezone.now()
#             game.save()
#             return redirect('shop:games_detail', id=game.id)
#     else:
#         form = ProductForm()
#     return render(request, 'shop/product_edit.html', {'form': form})

# def product_edit(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method=="POST":
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.created_date = timezone.now()
#             product.save()
#             return redirect('shop:product_detail', id=product.id)
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'shop/product_edit.html', {'form': form})

# def product_delete(request, id):
#     product = get_object_or_404(Product, id=id)
#     deleted = request.session.get('deleted', 'empty')
#     request.session['deleted'] = product.name
#     product.delete()
#     return redirect('shop:product_list' )

class Basket(object):
    # a data transfer object to shift items from cart to page
    # inspired by Django 3 by Example (2020) by Antonio Mele
    # https://github.com/PacktPublishing/Django-3-by-Example/
    
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            # save an empty basket in the session
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        """
        Iterate over the items in the basket and get the products
        from the database.
        """
        print(f'basket: { self.basket }')
        game_ids = self.basket.keys()
        # get the product objects and add them to the basket
        games = Game.objects.filter(id__in=game_ids)

        basket = self.basket.copy()
        for game in games:
            basket[str(game.id)]['game'] = game
            basket[str(game.id)]['game_id'] = game.id

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the basket.
        """
        return sum(item['quantity'] for item in self.basket.values())

    def add(self, game, quantity=1, override_quantity=False):
        """
        Add a product to the basket or update its quantity.
        """
        game_id = str(game.id)
        if game_id not in self.basket:
            self.basket[game_id] = {'quantity': 0,
                                    'price': str(game.price)}
        if override_quantity:
            self.basket[game_id]['quantity'] = quantity
        else:
            self.basket[game_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, game):
        """
        Remove a product from the basket.
        """
        game_id = str(game.id)
        if game_id in self.basket:
            del self.basket[game_id]
            self.save()

    def clear(self):
        # remove basket from session
        del self.session[settings.BASKET_SESSION_ID]
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())


@require_POST
def basket_add(request, id):
    basket = Basket(request)
    game = get_object_or_404(Game, id=id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(game=game,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('basket_detail')

@require_POST
def basket_remove(request, id):
    basket = Basket(request)
    game = get_object_or_404(Game, id=id)
    basket.remove(game)
    return redirect('basket_detail')

def basket_detail(request):
    basket = Basket(request)
    for item in basket:
        item['update_quantity_form'] = BasketAddProductForm(initial={'quantity': item['quantity'],
                                                                   'override': True})
    return render(request, 'games/shop/basket.html', {'basket': basket})
