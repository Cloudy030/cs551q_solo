from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Year, Genre, Platform, Publisher, Game

# Create your views here.
def index(request):
    # years=Year.objects.all()
    # countries=Country.objects.all()
    #for the 2 drop down filters
    return render(request, 'emission/index.html')#, {'years':years, 'countries':countries})