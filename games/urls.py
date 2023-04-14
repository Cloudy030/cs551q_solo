from django.urls import path
from . import views

urlpatterns=[
  path('',views.index, name='index'),
  path('year',views.year, name='year'),
  path('genre',views.genre, name='genre'),
  path('platform',views.platform, name='platform'),
  path('publisher',views.publisher, name='publisher'),
  path('gamedetail/<int:id>',views.gamedetail, name='gamedetail'),
  path('gamefilter',views.gamefilter, name='gamefilter')
]