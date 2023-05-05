from django.test import Client, TestCase
from django.urls import reverse
from games.models import Year, Genre, Platform, Publisher, Game

# Create your tests here.
# use the line below for debugging so that you can see what is on the page
#  print(response.content)

class GameViewsTests(TestCase):
  fixtures =['games_test.json']
  # @classmethod
  # def setUpTestData(cls):
  #   Platform.objects.create(
  #     platform_name='Wii',
  #     url='https://test_wii_url'
  #     )
  #   platform1=Platform.objects.get(platform_name='Wii')
  #   Platform.objects.create(
  #     platform_name='2600',
  #     url='https://test_2600_url'
  #     )
  #   platform2=Platform.objects.get(platform_name='2600')

  #   Year.objects.create(year_no='2023')
  #   year1=Year.objects.get(year_no='2023')
  #   Year.objects.create(year_no='2022')
  #   year2=Year.objects.get(year_no='2022')

  #   Genre.objects.create(
  #     genre_name='Racing',
  #     genre_description='racing testing description'
  #     )
  #   genre1=Genre.objects.get(genre_name='Racing')
  #   Genre.objects.create(
  #     genre_name='RPG',
  #     genre_description='RPG testing description'
  #     )
  #   genre2=Genre.objects.get(genre_name='RPG')

  #   Publisher.objects.create(publisher_name='20th Century Fox Video Games')
  #   publisher1=Publisher.objects.get(publisher_name='20th Century Fox Video Games')
  #   Publisher.objects.create(publisher_name='Zoo Games')
  #   publisher2=Publisher.objects.get(publisher_name='Zoo Games')

  #   Game.objects.create(
  #     rank=111,
  #     name='Pokemon',
  #     platform=platform1,
  #     year=year1,
  #     genre=genre1,
  #     publisher=publisher1,
  #     na_sales=4.3,
  #     eu_sales=5.9,
  #     jp_sales=7.9,
  #     other_sales=3.77,
  #     global_sales=21.87,
  #     price=34.23,
  #   )
  #   Game.objects.create(
  #     rank=112,
  #     name='Pokemon2',
  #     platform=platform2,
  #     year=year2,
  #     genre=genre2,
  #     publisher=publisher2,
  #     na_sales=1.3,
  #     eu_sales=5.55,
  #     jp_sales=7.8,
  #     other_sales=3.78,
  #     global_sales=18.43,
  #     price=20.33,
  #   )

  def test_game(self):
    game=Game.objects.get(id=15002)
    self.assertEqual(game.rank,2)
    games=Game.objects.all()
    self.assertEqual(games.count(),3000)
            

  def test_index(self):
      client = Client
      response = self.client.get('')
      # print("response: ~~~~~~~~~~~",response.content,"~~~~~~~~~~~~~~~~")
      self.assertEqual(response.status_code,200)
      self.assertContains(response, "Top 3000 Video Games")
      self.assertContains(response, "Video Game Name")
      self.assertContains(response, "Gran Turismo 3: A-Spec")
      self.assertContains(response, "DC")
      self.assertContains(response, "2012")
      self.assertContains(response, "Role-Playing")
      self.assertContains(response, "ChunSoft")