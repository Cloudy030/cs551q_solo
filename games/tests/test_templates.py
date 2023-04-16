from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):

  def test_index_view(self):
    url=reverse('index')
    response=self.client.get(url)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Top 3000 Video Games")
    self.assertContains(response, "Search")

  def test_filter_view(self):
    url=reverse('gamefilter')
    response=self.client.get(url)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Top 3000 Video Games")
    self.assertContains(response, "Search")

  def test_genre_view(self):
    url=reverse('genre')
    response=self.client.get(url)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Genre")

  def test_platform_view(self):
    url=reverse('platform')
    response=self.client.get(url)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Platform")

  def test_publisher_view(self):
    url=reverse('publisher')
    response=self.client.get(url)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Publisher")

  def test_year_view(self):
    url=reverse('year')
    response=self.client.get(url)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Year")
