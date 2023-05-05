from django.test import TestCase, Client
from games.models import Year, Genre, Platform, Publisher, Game

# Create your tests here.

# class YearModelTestCase(TestCase):
#   @classmethod
# # setup test data for year
#   def setUpYearTestData(cls):
#     Year.objects.create(year_no = '2023')
#     # year_obj=Year.objects.get(year_no='2023')

#   def test_year(self):
#     year=Year.objects.get(year_no='2023')
#     self.assertEqual(year.year_no,2023)


  # def setup(self):
  #   year_no = Year.objects.create(year_no='2023')

  #   # self.assertIsInstance(year_no, Year)
  #   # self.assertEqual(year.year_no, '2023')

  # def test_year_creation(self):
  #   self.assertTrue(isinstance(year_no, Year))
  #   self.assertEqual(year_no, '2023')

  # def test_year_str_representation(self):
  #   self.assertEqual(str(year_no), '2023')

# class GenreModelTestCase(TestCase):
  
#   def setup(self):
#     genre_name=Genre.objects.create(genre_name="Racing")

#     self.assertIsInstance(genre_name, Genre)
#     self.assertEqual(genre.genre_name, 'Racing')

# PlatformModelTestCase
# class PlatformModelTestCase(TestCase):
#   @classmethod
#   def setup(self):
#     platform_name=Platform.objects.create(platform_name="Wii")

#     self.assertIsInstance(platform_name, platform)
#     self.assertEqual(platform.platform_name, 'Wii')
# PublisherModelTestCase
# GameModelTestCase

class GameModelTestCase(TestCase):
  @classmethod
  def setUpTestData(cls):
    Platform.objects.create(
      platform_name='Wii',
      url='https://test_wii_url'
      )
    platform1=Platform.objects.get(platform_name='Wii')
    Platform.objects.create(
      platform_name='2600',
      url='https://test_2600_url'
      )
    platform2=Platform.objects.get(platform_name='2600')

    Year.objects.create(year_no='2023')
    year1=Year.objects.get(year_no='2023')
    Year.objects.create(year_no='2022')
    year2=Year.objects.get(year_no='2022')

    Genre.objects.create(
      genre_name='Racing',
      genre_description='racing testing description'
      )
    genre1=Genre.objects.get(genre_name='Racing')
    Genre.objects.create(
      genre_name='RPG',
      genre_description='RPG testing description'
      )
    genre2=Genre.objects.get(genre_name='RPG')

    Publisher.objects.create(publisher_name='20th Century Fox Video Games')
    publisher1=Publisher.objects.get(publisher_name='20th Century Fox Video Games')
    Publisher.objects.create(publisher_name='Zoo Games')
    publisher2=Publisher.objects.get(publisher_name='Zoo Games')

    Game.objects.create(
      rank=111,
      name='Pokemon',
      platform=platform1,
      year=year1,
      genre=genre1,
      publisher=publisher1,
      na_sales=4.3,
      eu_sales=5.9,
      jp_sales=7.9,
      other_sales=3.77,
      global_sales=21.87,
      price=34.23,
    )
    Game.objects.create(
      rank=112,
      name='Pokemon2',
      platform=platform2,
      year=year2,
      genre=genre2,
      publisher=publisher2,
      na_sales=1.3,
      eu_sales=5.55,
      jp_sales=7.8,
      other_sales=3.78,
      global_sales=18.43,
      price=20.33,
    )

  def test_game(self):
    game=Game.objects.get(id=1)
    self.assertEqual(game.rank,111)
    games=Game.objects.all()
    self.assertEqual(games.count(),2)

# class CartModelTestCase(TestCase):
# @classmethod
# def setUpTestData(cls):