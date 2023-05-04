from django.urls import path, include
from django.contrib import admin
import django.contrib.auth.urls
from . import views
from games.views import base, basket, customer, shop, order
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns=[
  path('',views.base.index, name='index'),
  path('year',views.base.year, name='year'),
  path('genre',views.base.genre, name='genre'),
  path('platform',views.base.platform, name='platform'),
  path('publisher',views.base.publisher, name='publisher'),
  path('gamedetail/<int:id>',views.base.gamedetail, name='gamedetail'),
  path('gamefilter',views.base.gamefilter, name='gamefilter'),
  path('year/<int:id>',views.base.yeargame, name='yeargame'),
  path('genre/<int:id>',views.base.genregame, name='genregame'),
  path('platform/<int:id>',views.base.platformgame, name='platformgame'),
  path('publisher/<int:id>',views.base.pugame, name='pugame'),
  path('compare',views.base.compare, name='compare'),
  # path('search/', SearchResult.as_view(), name="search_results"),

  # path('', views.products.product_list, name='product_list'),
  path('accounts/', include('django.contrib.auth.urls')),
  # https://stackoverflow.com/questions/64744543/product-list-got-an-unexpected-keyword-argument-product-id
  path('basket_add/<int:id>/', views.basket.basket_add, name ='basket_add'),
  path('basket_remove/<int:id>/', views.basket.basket_remove, name ='basket_remove'),
  path('basket_detail/', views.basket.basket_detail, name ='basket_detail'),
  path('signup/', views.shop.signup, name='signup'),
  path('dashboard/', views.shop.dashboard, name='dashboard'),
  path('customer_list', views.customer.customer_list, name='customer_list'),
  path('customer/<int:id>/', views.customer.customer_detail, name= 'customer_detail'),
  path('order_list/', views.order.order_list, name='order_list'),
  path('order/<int:id>/', views.order.order_detail, name= 'order_detail'),
  path('payment/', views.shop.payment, name ='payment'),
  # path('product_list/', views.products.product_list, name='product_list'),
  # path('product/<int:id>/', views.products.product_detail, name= 'product_detail'),
  # path('product_new/', views.products.product_new, name= 'product_new'),
  # path('product/<int:id>/edit/', views.products.product_edit, name= 'product_edit'),
  # path('product/<int:id>/delete/', views.products.product_delete, name= 'product_delete'),
  path('purchase/', views.shop.purchase, name ='purchase'),
]
#  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)