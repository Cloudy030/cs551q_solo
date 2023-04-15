from django.urls import path
from . import views

urlpatterns=[
  path('',views.index, name='index'),
  path('year',views.year, name='year'),
  path('genre',views.genre, name='genre'),
  path('platform',views.platform, name='platform'),
  path('publisher',views.publisher, name='publisher'),
  path('gamedetail/<int:id>',views.gamedetail, name='gamedetail'),
  path('gamefilter',views.gamefilter, name='gamefilter'),
  path('year/<int:id>',views.yeargame, name='yeargame'),
  path('genre/<int:id>',views.genregame, name='genregame'),
  path('platform/<int:id>',views.platformgame, name='platformgame'),
  path('publisher/<int:id>',views.pugame, name='pugame'),
]