from django.test import TestCase, Client
from django.urls import reverse
from games.models import Year, Genre, Platform, Publisher, Game

class TestFilterSearch(TestCase):
  def setUp(self):
    self.client=Client()
    
    self.platform1=Platform.objects.create(platform_name='Wii', url='https://test_wii_url')
    self.platform2=Platform.objects.create(platform_name='2600', url='https://test_2600_url')
    
    self.year1=Year.objects.create(year_no='2023')
    self.year2=Year.objects.create(year_no='2022')

    self.genre1=Genre.objects.create(genre_name='Racing',genre_description='racing testing description')
    self.genre2=Genre.objects.create(genre_name='RPG',genre_description='RPG testing description')

    self.publisher1=Publisher.objects.create(publisher_name='20th Century Fox Video Games')
    self.publisher2=Publisher.objects.create(publisher_name='Zoo Games')

    self.game1=Game.objects.create(
      rank=111,
      name='Pokemon',
      platform=self.platform1,
      year=self.year1,
      genre=self.genre1,
      publisher=self.publisher1,
      na_sales=4.3,
      eu_sales=5.9,
      jp_sales=7.9,
      other_sales=3.77,
      global_sales=21.87,
    )
    self.game2=Game.objects.create(
      rank=112,
      name='Pokemon2',
      platform=self.platform2,
      year=self.year2,
      genre=self.genre2,
      publisher=self.publisher2,
      na_sales=1.3,
      eu_sales=5.55,
      jp_sales=7.8,
      other_sales=3.78,
      global_sales=18.43,
    )

  def test_filter_search(self):
    response=self.client.post(reverse('gamefilter'),{'plfilter': self.platform1.platform_name, 'gfilter': self.genre1.genre_name, 'yfilter': self.year1.year_no, 'pufilter': self.publisher1.publisher_name})
    response=self.client.post(reverse('gamefilter'),{'plfilter': self.platform2.platform_name, 'gfilter': self.genre2.genre_name, 'yfilter': self.year2.year_no, 'pufilter': self.publisher2.publisher_name})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Pokemon")
    self.assertContains(response, "Pokemon2")
   