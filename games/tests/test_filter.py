from django.test import TestCase, Client
from django.urls import reverse
from games.models import Year, Genre, Platform, Publisher, Game

class TestFilterSearch(TestCase):
  fixtures =['games_test.json']

  def test_filter_search1_pl(self):
    response=self.client.post(reverse('gamefilter'),{'plfilter': 'N64'})
    # response2=self.client.post(reverse('gamefilter'),{'plfilter': self.platform2.platform_name, 'gfilter': self.genre2.genre_name, 'yfilter': self.year2.year_no, 'pufilter': self.publisher2.publisher_name})
    self.assertEqual(response.status_code, 200)
    # self.assertEqual(response2.status_code, 200)
    self.assertContains(response, "Super Mario 64")
    # self.assertContains(response2, "Pokemon2")

  def test_filter_search1_g(self):
    response=self.client.post(reverse('gamefilter'),{'gfilter': 'Platform'})
    # response2=self.client.post(reverse('gamefilter'),{'plfilter': self.platform2.platform_name, 'gfilter': self.genre2.genre_name, 'yfilter': self.year2.year_no, 'pufilter': self.publisher2.publisher_name})
    self.assertEqual(response.status_code, 200)
    # self.assertEqual(response2.status_code, 200)
    self.assertContains(response, "Super Mario 64")
    # self.assertContains(response2, "Pokemon2")

  def test_filter_search1_y(self):
    response=self.client.post(reverse('gamefilter'),{'yfilter': '1996'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search1_pu(self):
    response=self.client.post(reverse('gamefilter'),{'pufilter': 'Nintendo'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search2_nogpu(self):
    response=self.client.post(reverse('gamefilter'),{'plfilter': 'N64', 'yfilter': '1996'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search2_noypu(self):
    response=self.client.post(reverse('gamefilter'),{'plfilter': 'N64', 'gfilter': 'Platform'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search2_noyg(self):
    response=self.client.post(reverse('gamefilter'),{'plfilter': 'N64', 'pufilter': 'Nintendo'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search2_noplpu(self):
    response=self.client.post(reverse('gamefilter'),{'gfilter': 'Platform', 'yfilter': '1996'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search2_noplg(self):
    response=self.client.post(reverse('gamefilter'),{'yfilter': '1996', 'pufilter': 'Nintendo'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search2_noply(self):
    response=self.client.post(reverse('gamefilter'),{'gfilter': 'Platform', 'pufilter': 'Nintendo'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search3_nopl(self):
    response=self.client.post(reverse('gamefilter'),{'gfilter': 'Platform', 'yfilter': '1996', 'pufilter': 'Nintendo'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search3_noy(self):
    response=self.client.post(reverse('gamefilter'),{'plfilter': 'N64', 'yfilter': '1996', 'pufilter': 'Nintendo'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search3_nog(self):
    response=self.client.post(reverse('gamefilter'),{'plfilter': 'N64', 'gfilter': 'Platform', 'pufilter': 'Nintendo'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search3_nopu(self):
    response=self.client.post(reverse('gamefilter'),{'plfilter': 'N64', 'gfilter': 'Platform', 'yfilter': '1996'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search4(self):
    response=self.client.post(reverse('gamefilter'),{'plfilter': 'N64', 'gfilter': 'Platform', 'yfilter': '1996', 'pufilter': 'Nintendo'})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Super Mario 64")

  def test_filter_search_rank(self):
    response=self.client.post(reverse('compare'),{'gamec1': 10})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Duck Hunt")

  def test_filter_search_rank(self):
    response=self.client.post(reverse('compare'),{'gamec2': 17})
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Grand Theft Auto V")