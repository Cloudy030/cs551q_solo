from django.contrib import admin
from .models import Year, Genre, Platform, Publisher, Game,  Cart, Customer, LineItem, Order

# Register your models here.

class GameAdmin(admin.ModelAdmin):
  list_display=("rank", "name", "platform", "year", "genre", "publisher", "na_sales", "eu_sales", "jp_sales", "other_sales", "global_sales",)

admin.site.register(Game, GameAdmin)
admin.site.register(Genre)
admin.site.register(Year)
admin.site.register(Platform)
admin.site.register(Publisher)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(LineItem)
admin.site.register(Order)
