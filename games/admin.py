from django.contrib import admin
from .models import Year, Genre, Platform, Publisher, Game,  Cart, Customer, LineItem, Order

# Register your models here.

class GameAdmin(admin.ModelAdmin):
  list_display=("rank", "name", "platform", "year", "genre", "publisher", "na_sales", "eu_sales", "jp_sales", "other_sales", "global_sales",)
class GenreAdmin(admin.ModelAdmin):
  list_display=("genre_name", "genre_description",)
class PlatformAdmin(admin.ModelAdmin):
  list_display=("platform_name", "url",)
class PublisherAdmin(admin.ModelAdmin):
  list_display=("publisher_name",)
class CustomerAdmin(admin.ModelAdmin):
  list_display=("user", "created_date",)
class LineItemAdmin(admin.ModelAdmin):
  list_display=("quantity", "game","cart","order","created_date",)
class OrderAdmin(admin.ModelAdmin):
  list_display=("customer", "created_date",)

admin.site.register(Game, GameAdmin)
admin.site.register(Genre)
admin.site.register(Year)
admin.site.register(Platform)
admin.site.register(Publisher)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(LineItem)
admin.site.register(Order)
