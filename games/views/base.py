from django.shortcuts import render, get_object_or_404
from games.models import Year, Genre, Platform, Publisher, Game
from games.forms import BasketAddProductForm
from decimal import Decimal
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

def compare(request):

    games=Game.objects.all()
        # filter function
    g1=request.POST.get('gamec1')
    print('game1: ',g1,request)
    g2=request.POST.get('gamec2')
    print('game2: ',g2,request)

    if g1==None:
      # show data for Wii Sports if no filter requirements are given
      g1="1"
    if g2==None:
      g2="2"
    else:
      g1=g1
      g2=g2

    # game1=Game.objects.filter(name=g1)
    # print('game1: ',game1)
    # game2=Game.objects.filter(name=g2)
    # print('game2: ',game2)

    sources=Game.objects.filter(rank=g1)
    game1=sources
    print('game1: ',game1)
    # filter get the game
    sources_temp=[]
    for source in sources:
      sname1=source.name
      sources_temp.append(source.na_sales)
      sources_temp.append(source.eu_sales)
      sources_temp.append(source.jp_sales)
      sources_temp.append(source.other_sales)
      sources_temp.append(source.global_sales)
    sources_list1=json.dumps(sources_temp)
    # sname1=game1.name
    # print(sources)
    # print(sources_temp)
    # print(sname1)

    sources=Game.objects.filter(rank=g2)
    game2=sources
    print('game2: ',game2)
    # filter get the game
    sources_temp=[]
    for source in sources:
      sname2=source.name
      sources_temp.append(source.na_sales)
      sources_temp.append(source.eu_sales)
      sources_temp.append(source.jp_sales)
      sources_temp.append(source.other_sales)
      sources_temp.append(source.global_sales)
    sources_list2=json.dumps(sources_temp)
    # sname2=g2
    # print(sources)
    # print(sources_temp)

    return render(request, 'games/base/compare.html',{'sources_list':sources_list1,'sources_list2':sources_list2, 'games':games, 'sname':sname1, 'sname2':sname2, 'game1':game1, 'game2':game2})