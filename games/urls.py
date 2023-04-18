from django.urls import path, include
from django.contrib import admin
import django.contrib.auth.urls
from . import views

# from .views import HomePageView, SearchResultView

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
  # path('search/', SearchResult.as_view(), name="search_results"),

  # path('', views.products.product_list, name='product_list'),
  path('accounts/', include('django.contrib.auth.urls')),
  # path('basket_add/<int:product_id>/', views.basket.basket_add, name ='basket_add'),
  # path('basket_remove/<int:product_id>/', views.basket.basket_remove, name ='basket_remove'),
  # path('basket_detail/', views.basket.basket_detail, name ='basket_detail'),
  path('signup/', views.signup, name='signup'),
  path('dashboard/', views.dashboard, name='dashboard'),
  # path('customer_list', views.customers.customer_list, name='customer_list'),
  # path('customer/<int:id>/', views.customers.customer_detail, name= 'customer_detail'),
  # path('order_list/', views.orders.order_list, name='order_list'),
  # path('order/<int:id>/', views.orders.order_detail, name= 'order_detail'),
  # path('payment/', views.general.payment, name ='payment'),
  # path('product_list/', views.products.product_list, name='product_list'),
  # path('product/<int:id>/', views.products.product_detail, name= 'product_detail'),
  # path('product_new/', views.products.product_new, name= 'product_new'),
  # path('product/<int:id>/edit/', views.products.product_edit, name= 'product_edit'),
  # path('product/<int:id>/delete/', views.products.product_delete, name= 'product_delete'),
  # path('purchase/', views.general.purchase, name ='purchase'),
]