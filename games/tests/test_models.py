from django.test import TestCase, Client
from games.models import Year, Genre, Platform, Publisher, Game

# Create your tests here.

class YearModelTestCase(TestCase):
  def setup(self):
    self.year=Year.objects.create(year=2023)
  
  def test_year_creation(self):
    self.assertTrue(isinstance(self.year, Year))
GenreModelTestCase
PlatformModelTestCase
PublisherModelTestCase
GameModelTestCase