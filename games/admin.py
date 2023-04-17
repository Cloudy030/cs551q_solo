from django.contrib import admin
from .models import Year, Genre, Platform, Publisher, Game

# Register your models here.

class GameAdmin(admin.ModelAdmin):
  list_display=("rank", "name", "platform", "year", "genre", "publisher", "na_sales", "eu_sales", "jp_sales", "other_sales", "global_sales",)

admin.site.register(Game, GameAdmin)