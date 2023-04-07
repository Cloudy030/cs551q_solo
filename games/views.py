from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Year, Genre, Platform, Publisher, Game

# Create your views here.
def index(request):
    year=Year.objects.all()
    # countries=Country.objects.all()
    #for the 2 drop down filters
    return render(request, 'games/index.html', {'year':year})

def year(request):
    year=Year.objects.all()

    return render(request, 'games/year.html', {'year':year})

def genre(request):
    genre=Genre.objects.all()
    return render(request, 'games/genre.html', {'genre':genre})

def platform(request):
    platform=Platform.objects.all()
    return render(request, 'games/platform.html', {'platform':platform})

def publisher(request):
    publisher=Publisher.objects.all()
    return render(request, 'games/publisher.html', {'publisher':publisher})

def game(request):
    game=Game.objects.all()
    return render(request, 'games/game.html', {'game':game})