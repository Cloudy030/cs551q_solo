from django.test import Client, TestCase
from django.urls import reverse
from games.models import Year, Genre, Platform, Publisher, Game
# from django.contrib.auth.models import User

class TestGamesViews(TestCase):
  fixtures =['games_test']

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

  # def test_customer_list_view(self):
  #   user = User.objects.get(username="staff1")
  #   print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',Customer.objects.get(user=user))
    # # username=self.customer_user.username
    # # self.client.login(username='wewewes', password='st1234')
    # self.client.login(username=self.st.username, password='st1234')
    # # url=reverse('customer_list')
    # # response=self.client.get(url)
    # response = self.client.get('/customer_list')
    # # print(url)
    # print('+++++++++++++++++++++',response)
    # print('+++++++++++++++',response.context)
    # self.assertEqual(response.status_code,200)
    # self.assertContains(response, "Their username is")
    # self.assertContains(response, "and they live at")
    # self.assertContains(response, ". You can reach them at ")

  # def test_dashboard_view(self):
  #   url=reverse('dashboard')
  #   response=self.client.get(url)
  #   self.assertEqual(response.status_code,200)
  #   self.assertContains(response, "Account numbers")

  # def test_order_list_view(self):
  #   url=reverse('order_list')
  #   response=self.client.get(url)
  #   self.assertEqual(response.status_code,200)
  #   self.assertContains(response, "Order List")

  # def test_purchase_view(self):
  #   url=reverse('purchase')
  #   response=self.client.get(url)
  #   self.assertEqual(response.status_code,200)
  #   self.assertContains(response, "The total for all of video game(s) is: ")



  # def test__view(self):
  #   url=reverse('')
  #   response=self.client.get(url)
  #   self.assertEqual(response.status_code,200)
  #   self.assertContains(response, "")

  # def test__view(self):
  #   url=reverse('')
  #   response=self.client.get(url)
  #   self.assertEqual(response.status_code,200)
  #   self.assertContains(response, "")
    
  # def test__view(self):
  #   url=reverse('')
  #   response=self.client.get(url)
  #   self.assertEqual(response.status_code,200)
  #   self.assertContains(response, "")

