from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Year, Genre, Platform, Publisher, Game

# Create your views here.
def index(request):
    games=Game.objects.all()
    platforms=Platform.objects.all()
    years=Year.objects.all()
    genres=Genre.objects.all()
    publishers=Publisher.objects.all()
    return render(request, 'games/index.html', {'games':games, 'platforms':platforms, 'years':years, 'genres':genres, 'publishers':publishers})
    # year=Year.objects.all()
    # # countries=Country.objects.all()
    # #for the 2 drop down filters
    # return render(request, 'games/index.html', {'year':year})

def gamefilter(request):
    games=Game.objects.all()
    # for drop down search bar
    platforms=Platform.objects.all()
    pl=request.POST.get('plfilter')
    print('platform: ',pl,request)
    # if pl==None:
    return render(request, 'games/game.html', {'games':games})

def year(request):
    years=Year.objects.all()

    return render(request, 'games/year.html', {'years':years})

def genre(request):
    genres=Genre.objects.all()
    return render(request, 'games/genre.html', {'genres':genres})

def platform(request):
    platforms=Platform.objects.all()
    return render(request, 'games/platform.html', {'platforms':platforms})

def publisher(request):
    publishers=Publisher.objects.all()
    return render(request, 'games/publisher.html', {'publishers':publishers})

def gamedetail(request,id):
    # games=Game.objects.all()
    game=get_object_or_404(Game,id=id)
    return render(request, 'games/game_detail.html', {'game':game})