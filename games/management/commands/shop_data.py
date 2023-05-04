from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DatabaseError
import random
import decimal
from datetime import datetime
from django.contrib.auth.models import User
from faker import Faker

from games.models import Year, Genre, Platform, Publisher, Game, Cart, Customer, LineItem, Order

class Command(BaseCommand):
  # help='Load data from csv'

  def handle(self, *args, **options):
    # Year.objects.all().delete()
    # Genre.objects.all().delete()
    # Platform.objects.all().delete()
    # Publisher.objects.all().delete()
    # Game.objects.all().delete()

    Cart.objects.all().delete()
    LineItem.objects.all().delete()
    Order.objects.all().delete()
    Customer.objects.all().delete()
    User.objects.all().delete()
    print('shop-related tables dropped successfully')

    fake = Faker()

    # create some customers
    # we convert some values from tuples to strings
    for i in range(10):
      first_name = fake.first_name(),
      first_name = str(first_name[0])
      last_name = fake.last_name(),
      last_name = str(last_name[0])
      username = first_name + last_name,
      username = username[0]
      user = User.objects.create_user(
      username = username,
      first_name = first_name,
      last_name = last_name,
      email = fake.ascii_free_email(), 
      password = 'p@ssw0rd')
      customer = Customer.objects.get(user = user)
      customer.user_type = 'Customer'
      customer.address = fake.address(),
      customer.address = str(customer.address[0])
      customer.save()

    # first sample admin account will be required to be created by command
    first_name = "Afirst",
    first_name = str('Afirst2')
    # last_name = "Alast",
    last_name = str('Afirst2')
    username = 'admin2'
    # username = username[0]
    user = User.objects.create_user(
    username = username,
    first_name = first_name,
    last_name = last_name,
    email = str('a@b.com'),
    password = '1234')
    customer = Customer.objects.get(user = user)
    customer.user_type = 'Admin'
    customer.address = fake.address(),
    customer.address = str(customer.address[0])
    customer.save()
    print('Admin account Created Successfully')

    # sample staff account
    first_name = str('Sfirst')
    # last_name = "Alast",
    last_name = str('Sfirst')
    username = 'staff'
    # username = username[0]
    user = User.objects.create_user(
    username = username,
    first_name = first_name,
    last_name = last_name,
    email = str('s@b.com'), 
    password = '5678')
    customer = Customer.objects.get(user = user)
    customer.user_type = 'Staff'
    customer.address = fake.address(),
    customer.address = str(customer.address[0])
    customer.save()
    print('Staff account Created Successfully')

    # sample staff account
    first_name = str('Sfirst2')
    # last_name = "Alast",
    last_name = str('Sfirst2')
    username = 'staff2'
    # username = username[0]
    user = User.objects.create_user(
    username = username,
    first_name = first_name,
    last_name = last_name,
    email = str('s@b.com'), 
    password = '5678')
    customer = Customer.objects.get(user = user)
    customer.user_type = 'Staff'
    customer.address = fake.address(),
    customer.address = str(customer.address[0])
    customer.save()
    print('Staff account Created Successfully')

    # sample staff account
    first_name = str('Sfirst3')
    # last_name = "Alast",
    last_name = str('Sfirst3')
    username = 'staff3'
    # username = username[0]
    user = User.objects.create_user(
    username = username,
    first_name = first_name,
    last_name = last_name,
    email = str('s@b.com'), 
    password = '5678')
    customer = Customer.objects.get(user = user)
    customer.user_type = 'Staff'
    customer.address = fake.address(),
    customer.address = str(customer.address[0])
    customer.save()
    print('Staff account Created Successfully')

    # sample customer account
    first_name = str('Cfirst')
    # last_name = "Alast",
    last_name = str('Cfirst')
    username = 'customer'
    # username = username[0]
    user = User.objects.create_user(
    username = username,
    first_name = first_name,
    last_name = last_name,
    email = str('c@b.com'), 
    password = '7890')
    customer = Customer.objects.get(user = user)
    customer.user_type = 'Customer'
    customer.address = fake.address(),
    customer.address = str(customer.address[0])
    customer.save()
    print('Customer account Created Successfully')

    print('Customer Table Created Successfully')

    # # create some products
    # for i in range(10):
    #   product = Product.objects.create(
    #   name = fake.catch_phrase(),
    #   price = int( decimal.Decimal(random.randrange(155,899))/100),
    #   )
    #   product.save()

    # create some carts 
    games = list(Game.objects.all())
    for i in range(10):
      random_id = random.randint(1,9)
      cart = Cart.objects.create(
      game = games[random_id],
      quantity = random.randrange(1,10),
      )
      cart.save()

    print('Cart Table Created Successfully')

    # create orders from customers
    customers = Customer.objects.all()
    for customer in customers: 
      a=random.randrange(0,11)
      print('-------------',a,'--------------')
      for i in range(a): 
      # for i in range(3):
        order = Order.objects.create(
        customer = customer,
        )
        order.save()
        # print(order)

    print('Order Table Created Successfully')
          
    # attach line_items to orders
    orders = Order.objects.all()
    carts = Cart.objects.all()
    for order in orders:
      for cart in carts:
        line_item = LineItem.objects.create(
        quantity = cart.quantity,
        game = cart.game,
        cart = cart,
        order = order,
        )
        line_item.save()     

    print('Line_item Table Created Successfully')

    print("data generated successfully")
