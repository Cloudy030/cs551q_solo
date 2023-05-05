from django.test import Client, TestCase
from django.urls import reverse
from games.models import Year, Genre, Platform, Publisher, Game#, Customer
# from django.contrib.auth.models import User

class TestGamesViews(TestCase):
  fixtures =['games_test.json']

  # def setUp(self):
  #   # self.ct=User.objects.create_user(username='ctest')
  #   # self.ct.set_password('testpwd')
  #   # self.ct.save()
  #   # Customer.objects.get_or_create(user=self.ct, user_id=510, user_type="Customer", address='test address')

  #   # self.st=User.objects.create_user(username='stest')
  #   # self.st.set_password('testpwd')
  #   # self.st.save()
  #   # Customer.objects.get_or_create(user=self.st, user_id=511, user_type="Staff", address='test address')

  #   self.at=User.objects.create(username='admin')
  #   self.at.set_password('1234')
  #   self.at.save()
  #   print('++++++++++',self.at)
  #   user =  Customer.objects.all().filter(user=self.at)
  #   print('~~~~~~~~~~~~~~',user)
  #   Customer.objects.get_or_create(user=self.at, user_type="Admin", address='test address')
  #   # Customer.objects.get_or_create(user=self.at, user_id=522, user_type="Admin", address='test address')
  #   print('@@@@@@@@@@@@@@',Customer.objects.all())
  #   self.client=Client()

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
    # print('++++++++++++++++++++',url)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Year")

  def test_gamedetail_view(self):
    client=Client()
    # game = Game.objects.get(id=1)
    # print('~~~~~~~~~~~~~~~~~~~~~~~',game)
    # url=self.client.post('gamedetail',{'id':'2'})
    # url=self.client.post('/gamedetail/1/')
    # response=self.client.get(url)
    response = self.client.get('/gamedetail/15001')
    # print('url:*****************',response)
    # print("response****************",response.content)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Add to Basket")

  def test_genre_game_view(self):
    client=Client()
    response = self.client.get('/genre/182')
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Advanture games put the player in the role of a protagonist in an interactive way, driven by exploration or puzzle-solving. This genre of games focus on story allowing to depend heavily on narrative-based literature or film.")
    self.assertContains(response, "Video Game Name")

  def test_year_game_view(self):
    client=Client()
    response = self.client.get('/year/610')
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "1981")
    self.assertContains(response, "Video Game Name")

  def test_platform_game_view(self):
    client=Client()
    response = self.client.get('/platform/377')
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "3DS")
    self.assertContains(response, "Video Game Name")

  def test_publisher_game_view(self):
    client=Client()
    response = self.client.get('/publisher/2041')
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "20th Century Fox Video Games")
    self.assertContains(response, "Video Game Name")

  def test_compare_view(self):
    url=reverse('compare')
    response=self.client.get(url)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Games Comparision")
    self.assertContains(response, "Sales Data Comparision")

  def test_basket_view(self):
    url=reverse('basket_detail')
    response=self.client.get(url)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "You have these in your basket:")

  def test_signup_view(self):
    url=reverse('signup')
    response=self.client.get(url)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Registration")
    
  def test_login_view(self):
    url=reverse('login')
    response=self.client.get(url)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Login")
    self.assertContains(response, "Please login, or ")