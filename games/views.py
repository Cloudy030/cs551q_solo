from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Year, Genre, Platform, Publisher, Game

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
    # print(games)

    return render(request, 'games/index.html', {'content':content, 'games':games, 'platforms':platforms, 'years':years, 'genres':genres, 'publishers':publishers})

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
    
    return render(request, 'games/game_filter.html', {'filgame':filgame, 'games':games, 'platforms':platforms, 'years':years, 'genres':genres, 'publishers':publishers})

def year(request):
    years=Year.objects.all()
    return render(request, 'games/year.html', {'years':years})

def yeargame(request,id):
    games=Game.objects.all()
    years.Year.objects.all()
    return render(request, 'games/year_game.html', {'years': years, 'games':games})

def genre(request):
    genres=Genre.objects.all()
    return render(request, 'games/genre.html', {'genres':genres})

def genregame(request,id):
    # games=Game.objects.all()
    # genres=Genre.objects.all()
    genre=get_object_or_404(Genre,id=id)
    games=Game.objects.filter(genre__id=id)
    return render(request, 'games/genre_game.html', {'genre':genre, 'games':games})

def platform(request):
    platforms=Platform.objects.all()
    return render(request, 'games/platform.html', {'platforms':platforms})

def platformgame(request,id):
    # game=get_object_or_404(Game,id=id)
    # publishers=Publisher.objects.all()
    platform=get_object_or_404(Platform,id=id)
    games=Game.objects.filter(platform__id=id)
    return render(request, 'games/platform_game.html', {'platform':platform, 'games':games})

def publisher(request):
    publishers=Publisher.objects.all()
    return render(request, 'games/publisher.html', {'publishers':publishers})

def pugame(request,id):
    # games=Game.objects.all()
    # publishers=Publisher.objects.all()
    publisher=get_object_or_404(Publisher,id=id)
    games=Game.objects.filter(publisher__id=id)
    print("publisher: ",id, request)
    return render(request, 'games/publisher_game.html', {'publisher':publisher, 'games':games})

def gamedetail(request,id):
    # games=Game.objects.all()
    game=get_object_or_404(Game,id=id)
    return render(request, 'games/game_detail.html', {'game':game})