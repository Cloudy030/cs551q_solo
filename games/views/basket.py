from django.shortcuts import redirect, render, get_object_or_404
from games.models import Game
from games.forms import BasketAddProductForm
from decimal import Decimal
from django.conf import settings
from django.views.decorators.http import require_POST

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
