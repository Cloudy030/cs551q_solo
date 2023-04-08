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
      url='https://tse1.mm.bing.net/th?id=OIP.CtiRaE9ucOFqtZGzjkR0BQHaHa&pid=Api'
      )
    platform1=Platform.objects.get()

    Year.objects.create(year_no='2023')
    year1=Year.objects.get()

    Genre.objects.create(genre_name='Racing')
    genre1=Genre.objects.get()

    Publisher.objects.create(publisher_name='20th Century Fox Video Games')
    publisher1=Publisher.objects.get()

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
    )
    # Game.objects.create(
    #   rank=112,
    #   name='Pokemon2',
    #   platform='PC',
    #   year='2022',
    #   genre='Racing',
    #   publisher='Zoo Games',
    #   na_sales=1.3,
    #   eu_sales=5.55,
    #   jp_sales=7.8,
    #   other_sales=3.78,
    #   global_sales=18.43,
    # )

  def test_game(self):
    game=Game.objects.get(id=1)
    self.assertEqual(game.rank,111)
    games=Game.objects.all()
    self.assertEqual(games.count(),1)