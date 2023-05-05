from django.test import Client, TestCase
from django.urls import reverse
from games.models import Year, Genre, Platform, Publisher, Game, Customer
from django.contrib.auth.models import User

class TestViews(TestCase):
  @classmethod
  def setUpTestData(cls):
    fixtures =['games']

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
      # id=1,
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
      # id=2,
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
  # @classmethod
  # def setUp(self):
  #   self.ct=User.objects.create_user(username='hahahac')
  #   self.ct.set_password('ct1234')
  #   # self.ct.
  #   self.ct.save()
  #   Customer.objects.get_or_create(
  #     user=self.ct,
  #     user_type='Customer',
  #     # email='ct@b.com',
  #     address='c test address',
  #     created_date="2023-05-04 11:56:29.432035+00:00"
  #     )

  def setUp(self):
    # user = User.objects.get(username="staff1")
    # print('~~~~~~~~~~~~~~~~~`',user,'~~~~~~~~~~`')
    self.st=User.objects.create_user(username='staff1')
    self.st.set_password('st1234')
    # self.st.email='st@b.com'
    # self.ct.
    self.st.save()
    user = User.objects.get(username="staff1")
    print(user)
    c = Customer.objects.get(user=user)
    print(c)
    # print(Customer.objects.all())
    Customer.objects.create(
      # user_id=100,
      user=self.st,
      user_type='Staff',
      # email='ct@b.com',
      address='s test address',
      created_date="2023-05-04 11:56:29.432035+00:00"
      )

  # def setUp(self):
  #   self.at=User.objects.create_user(username='bububua')
  #   self.at.set_password('at1234')
  #   # self.ct.
  #   self.at.save()
  #   Customer.objects.get_or_create(
  #     user=self.at,
  #     user_type='Admin',
  #     # email='ct@b.com',
  #     address='a test address',
  #     created_date="2023-05-04 11:56:29.432035+00:00"
  #     )
  # def setUpTestData(cls):
    # c1=User.objects.create_user(
    #   first_name="cf1",
    #   last_name="cl1",
    #   username="ct",
    #   email="ct@b.com",
    #   password='ct1234',
    #   # user_id=510,
    #   )
    # c1=User.objects.get(username="ct")
    # s1=User.objects.create_user(
    #   first_name="sf1",
    #   last_name="sl1",
    #   username="st",
    #   email="st@b.com",
    #   password='st1234',
    #   # user_id=511,
    #   )
    # s1=User.objects.get(username="st")
    # a1=User.objects.create_user(
    #   first_name="af1",
    #   last_name="al1",
    #   username="at",
    #   email="at@b.com",
    #   password='at1234',
    #   # user_id=512,
    #   )
    # a1=User.objects.get(username="at")

    # Customer.objects.get_or_create(
    # user=c1,
    # # user_id=510,
    # user_type='Customer',
    # address="c test address",
    # created_date="2023-05-04 11:56:29.432035+00:00"
    # )
    # Customer.objects.get_or_create(
    #   user=s1,
    #   # user_id=511,
    #   user_type='Staff',
    #   address="s test address",
    #   created_date="2023-05-04 11:56:29.432035+00:00"
    # )
    # Customer.objects.get_or_create(
    #   user=a1,
    #   # user_id=512,
    #   user_type='Admin',
    #   address="a test address",
    #   created_date="2023-05-04 11:56:29.432035+00:00"
    # )

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
    response = self.client.get('/gamedetail/1')
    # print('url:*****************',response)
    # print("response****************",response.content)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Add to Basket")

  def test_genre_game_view(self):
    client=Client()
    # game = Game.objects.get(id=1)
    # print('~~~~~~~~~~~~~~~~~~~~~~~',game)
    # url=self.client.post('gamedetail',{'id':'2'})
    # url=self.client.post('/gamedetail/1/')
    # response=self.client.get(url)
    response = self.client.get('/genre/1')
    # print('url:*****************',response)
    # print("response****************",response.content)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "racing testing description")
    self.assertContains(response, "Video Game Name")

  def test_year_game_view(self):
    client=Client()
    # game = Game.objects.get(id=1)
    # print('~~~~~~~~~~~~~~~~~~~~~~~',game)
    # url=self.client.post('gamedetail',{'id':'2'})
    # url=self.client.post('/gamedetail/1/')
    # response=self.client.get(url)
    response = self.client.get('/year/1')
    # print('url:*****************',response)
    # print("response****************",response.content)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "2023")
    self.assertContains(response, "Video Game Name")

  def test_platform_game_view(self):
    client=Client()
    # game = Game.objects.get(id=1)
    # print('~~~~~~~~~~~~~~~~~~~~~~~',game)
    # url=self.client.post('gamedetail',{'id':'2'})
    # url=self.client.post('/gamedetail/1/')
    # response=self.client.get(url)
    response = self.client.get('/platform/1')
    # print('url:*****************',response)
    # print("response****************",response.content)
    self.assertEqual(response.status_code,200)
    self.assertContains(response, "Wii")
    self.assertContains(response, "Video Game Name")

  def test_publisher_game_view(self):
    client=Client()
    # game = Game.objects.get(id=1)
    # print('~~~~~~~~~~~~~~~~~~~~~~~',game)
    # url=self.client.post('gamedetail',{'id':'2'})
    # url=self.client.post('/gamedetail/1/')
    # response=self.client.get(url)
    response = self.client.get('/publisher/1')
    # print('url:*****************',response)
    # print("response****************",response.content)
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

  def test_customer_list_view(self):
    user = User.objects.get(username="staff1")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',Customer.objects.get(user=user))
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

