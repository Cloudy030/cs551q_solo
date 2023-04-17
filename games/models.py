try:
  from django.conf import settings
  from django.db import models
  from django.utils import timezone
  from django.contrib.auth.models import User
  from django.db.models.signals import post_save
  from django.dispatch import receiver

except ImportError as error:
  print("Error importing Module: ", error)

# Create your models here.

class Year(models.Model):
  # model for year with only year from year.csv with autogenerated id
  # id=models.BigAutoField(primary_key=True)
  year_no=models.TextField()
  # cannot use models.IntegerField because of N/A in year field

  def __str__(self):
    return f'{self.year_no}'

class Genre(models.Model):
  # model for genre with only genre from genre.csv with autogenerated id
  # id=models.BigAutoField(primary_key=True)
  genre_name=models.TextField()
  genre_description=models.TextField()

  def __str__(self):
    return f'{self.genre_name, self.genre_description}'

class Platform(models.Model):
  # model for platform of game release from platform.csv with autogenerated id
  # id=models.BigAutoField(primary_key=True)
  platform_name=models.TextField()
  url=models.TextField()

  def __str__(self):
    return f'{self.platform_name,self.url}'
    
class Publisher(models.Model):
  # model for publisher of game release from publisher.csv with autogenerated id
  # id=models.BigAutoField(primary_key=True)
  publisher_name=models.TextField()

  def __str__(self):
    return f'{self.publisher_name}'

class Game(models.Model):
  # model for video game sales from vgsales_edited.csv with autogenerated id
  # id=models.BigAutoField(primary_key=True)
  rank=models.IntegerField()
    # sales rank from top 1 to 3000, lost 654th
  name=models.TextField()
    # name of video game
  platform=models.ForeignKey('Platform', on_delete=models.CASCADE, null=True)
  year=models.ForeignKey('Year', on_delete=models.CASCADE, null=True)
  genre=models.ForeignKey('Genre', on_delete=models.CASCADE, null=True)
  publisher=models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
  na_sales=models.FloatField()
    # sales in north america (in millions)
  eu_sales=models.FloatField()
    # sales in europe (in millions)
  jp_sales=models.FloatField()
    # sales in japan (in millions)
  other_sales=models.FloatField()
    # sales in rest of the world (in millions)
  global_sales=models.FloatField()
    # total worldwide sales (in millions)

  def __str__(self):
    return f'{self.rank}, {self.name}, {self.platform}, {self.year}, {self.genre}, {self.publisher}, {self.na_sales}, {self.eu_sales}, {self.jp_sales}, {self.other_sales}, {self.global_sales}'

class Cart(models.Model):
  game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='carts')
  quantity = models.IntegerField()
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.game},{self.quantity},{self.created_date}'

# switch customer to user so that we can use Django's componenents
# https://blog.crunchydata.com/blog/extending-djangos-user-model-with-onetoonefield 
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone

class Customer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
  address = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.user.email}, {self.address}'

  class Meta:
    db_table = 'customer'

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Customer.objects.create(user=instance)
  
  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.customer.save()

class LineItem(models.Model):
  quantity = models.IntegerField()
  game = models.ForeignKey('Game', on_delete=models.CASCADE)
  cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
  order = models.ForeignKey('Order', on_delete=models.CASCADE)
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.quantity},{self.game},{self.cart},{self.order},{self.created_date}'

class Order(models.Model):
  customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.customer},{self.created_date}'

# class Product(models.Model):
#   game=models.ForeignKey('Game', on_delete=models.CASCADE, null=True)
#   # name = models.CharField(max_length=200, db_index=True)
#   # use decimal instead of float to avoid rounding errors
#   # always use decimal for money values
#   # price = models.DecimalField(max_digits=4, decimal_places=2) 
#   # created_date = models.DateTimeField(auto_now_add=True)

#   def __str__(self):
#     return f'{self.game}'#,{self.price},{self.created_date}'