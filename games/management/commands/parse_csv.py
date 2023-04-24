import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DatabaseError
import random
import decimal
from datetime import datetime

from games.models import Year, Genre, Platform, Publisher, Game

class Command(BaseCommand):
  help='Load data from csv'

  def handle(self, *args, **options):
    Year.objects.all().delete()
    Genre.objects.all().delete()
    Platform.objects.all().delete()
    Publisher.objects.all().delete()
    Game.objects.all().delete()

    Cart.objects.all().delete()
    LineItem.objects.all().delete()
    Order.objects.all().delete()
    Customer.objects.all().delete()
    User.objects.all().delete()
    print('tables dropped successfully')

    # open year.csv data files to parse them into the database
    # year table
    try:
      base_dir = Path(__file__).resolve().parent.parent.parent.parent
      with open(str(base_dir) + '/data/year.csv', newline='') as f:
        reader=csv.reader(f, delimiter=",")
        next(reader) # skip header line
        for row in reader:
          print(row)

          year=Year.objects.create(
            year_no=row[0],
          )
          year.save()
      print('Year Table Parsed Successfully')
    except FileNotFoundError:
      raise CommandError('year.csv file not found')
    
    # open genre.csv data files to parse them into the database
    # genre table
    try:
      base_dir = Path(__file__).resolve().parent.parent.parent.parent
      with open(str(base_dir) + '/data/genre.csv', newline='') as f:
        reader=csv.reader(f, delimiter=",")
        next(reader) # skip header line
        for row in reader:
          print(row)

          genre=Genre.objects.create(
            genre_name=row[0],
            genre_description=row[1],
          )
          genre.save()
      print('Genre Table Parsed Successfully')
    except FileNotFoundError:
      raise CommandError('genre.csv file not found')

    # open platform.csv data files to parse them into the database
    # platform table
    try:
      base_dir = Path(__file__).resolve().parent.parent.parent.parent
      with open(str(base_dir) + '/data/platform.csv', newline='') as f:
        reader=csv.reader(f, delimiter=",")
        next(reader) # skip header line
        for row in reader:
          print(row)

          platform=Platform.objects.create(
            platform_name=row[0],
            url=row[1],
          )
          platform.save()
      print('Platform Table Parsed Successfully')
    except FileNotFoundError:
      raise CommandError('platform.csv file not found')

    # open publisher.csv data files to parse them into the database
    # publisher table
    try:
      base_dir = Path(__file__).resolve().parent.parent.parent.parent
      with open(str(base_dir) + '/data/publisher.csv', newline='') as f:
        reader=csv.reader(f, delimiter=",")
        next(reader) # skip header line
        for row in reader:
          print(row)

          publisher=Publisher.objects.create(
            publisher_name=row[0],
          )
          publisher.save()
      print('Publisher Table Parsed Successfully')
    except FileNotFoundError:
      raise CommandError('publisher.csv file not found')

    # open game.csv data files to parse them into the database
    # game table
    try:
      base_dir = Path(__file__).resolve().parent.parent.parent.parent
      with open(str(base_dir) + '/data/vgsales_edited.csv', newline='') as f:
        reader=csv.reader(f, delimiter=",")
        next(reader) # skip header line
        for row in reader:
          print(row)
        
          try:
            game=Game.objects.create(
              rank=int(row[0]),
              name=row[1],
              platform=Platform.objects.filter(platform_name=row[2]).first(),
              year=Year.objects.filter(year_no=row[3]).first(),
              genre=Genre.objects.filter(genre_name=row[4]).first(),
              publisher=Publisher.objects.filter(publisher_name=row[5]).first(),
              na_sales=float(row[6]),
              eu_sales=float(row[7]),
              jp_sales=float(row[8]),
              other_sales=float(row[9]),
              global_sales =float(row[10]),
              price= int( decimal.Decimal(random.randrange(3000,9999))/100),
            )
            game.save()
          except (ValueError, DatabaseError) as error:
            print(f"Error parsing row {row}: {error}")

      print('Game Table Parsed Successfully')
    except FileNotFoundError:
      raise CommandError('vgsales_edited.csv file not found')

    print("data parsed successfully")
