import urllib
from urllib.parse import urljoin
from behave import given, when, then
from games.models import Year, Genre, Platform, Publisher, Game, Customer
from django.contrib.auth.models import User


@given(u'we want to add Super Mario World to basket')
def user_on_gamedetailpage(context):

  year,_=Year.objects.get_or_create(year_no='2000')
  genre,_=Genre.objects.get_or_create(genre_name='Action', genre_description='test description for Action')
  platform,_=Platform.objects.get_or_create(platform_name='PC', url='https://tse1.mm.bing.net/th?id=OIP.FgBGMlSrG14nR-JQZbWUaQHaEJ&pid=Api')
  publisher,_=Publisher.objects.get_or_create(publisher_name='Nintendo')
  game,_=Game.objects.get_or_create(id='9019', rank='20', name='Super Mario World', platform=platform, year=year, genre=genre, publisher=publisher,
  na_sales='1.1', eu_sales='2.2', jp_sales='3.3', other_sales='4.4', global_sales='11', price='50.3')

  print(Game.objects.all())

  # base_url = 'https://wheelpioneer-bananashock-8000.codio-box.uk'
  '''
  only work if the server is alreay already running
  '''
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  # open_url = urljoin(base_url,'')
  open_url = urljoin(base_url,'/gamedetail/9019')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')
  
@when(u'we click add to basket button')
def user_click_add_to_basket_button(context):
  # use print(context.browser.page_source) to aid debugging
  # only prints page source if there is an error in the step
  print(context.browser.page_source)
  quantity_option = context.browser.find_element('name', 'quantity')
  quantity_option.send_keys(3)
  # price_textfield = context.browser.find_element('name','price')
  # price_textfield.send_keys(3)
  # context.browser.find_element('name','submit').click()

@then(u'it succeds')
def game_add_in_basket(context):
  assert 'Super Mario World' in context.browser.page_source

# @then(u'we change quantity to two')
# def change_quantity_to_two(context):
#   print(context.browser.page_source)
#   quantity_option = context.browser.find_element('game', 'quantity')
#   quantity_option.send_keys(2)
#   context.browser.find_element('game','submit').click()

# @then(u'total price is 100.6')
# def total_price_change(context):
#   assert '100.6' in context.browser.page_source

###

@given(u'we have Super Mario World in basket')
def have_games_in_basket(context):
  print(Game.objects.all())
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  # open_url = urljoin(base_url,'')
  open_url1 = urljoin(base_url,'/gamedetail/9019')
  context.browser.get(open_url1)
  quantity_option = context.browser.find_element('name', 'quantity')
  quantity_option.send_keys(3)
  print(context.browser.page_source)
  open_url = urljoin(base_url,'/basket_detail')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')
  print(context.browser.page_source)
  # assert 'Super Mario World' in context.browser.page_source

@when(u'we change quantity to two')
def change_quantity(context):
  print(context.browser.page_source)
  quantity_option = context.browser.find_element('game', 'quantity')
  quantity_option.send_keys(2)
  context.browser.find_element('game','submit').click()


@then(u'total price is 100.6')
def view_total(context):
  assert '100.6' in context.browser.page_source

###


@given(u'we are not login and press the purchase button')
def not_login_adn_press_purchase(context):

  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  # open_url = urljoin(base_url,'')
  open_url = urljoin(base_url,'/basket_detail')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')
  link = driver.find_element_by_link_text('Purchase')
  link.click()
  
@when(u'we are directed to login page')
def login_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/accounts/login')
  Assert.assertEquals(URL, open_url );
  assert 'Login' in context.browser.page_source


@then(u'we input registered account credentials')
def input_login_credentials (context):
    
  # self.st=User.objects.create_user(username='stest')
  #   # self.st.set_password('testpwd')
  #   # self.st.save()
  #   # Customer.objects.get_or_create(user=self.st, user_id=511, user_type="Staff", address='test address')

  user,_=User.objects.create_user(
    first_name='af1',
    last_name='al1',
    username='at',
    email='at@b.com',
    password='at1234'
  )
  a1=User.object.get(username='at')
  customer,_=Customer.objects.get_or_create(
    user_id='500',
    user=a1,
    user_type='Admin',
    address="test address",
    created_date="2023-05-05 08:46:38.856800+00:00"
  )

  print(Customer.objects.all())
  
  username_textfield = context.browser.find_element('Login', 'username')
  username_textfield.send_keys('at')
  pwd_textfield = context.browser.find_element('Login','password')
  pwd_textfield.send_keys('at1234')
  context.browser.find_element('Login','submit').click()


@then(u'we go to index page')
def index_page(context):
  URL = driver.current_url();
  open_url1 = urljoin(base_url)
  Assert.assertEquals(URL, open_url1 );
  assert 'Top 3000 Video Games' in context.browser.page_source

###

@given(u'we have two Super Mario World in basket')
def two_super_mario_world_in_basket(context):
  print(Game.objects.all())
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  # open_url = urljoin(base_url,'')
  open_url1 = urljoin(base_url,'/gamedetail/9019')
  context.browser.get(open_url1)
  quantity_option = context.browser.find_element('name', 'quantity')
  quantity_option.send_keys(2)
  print(context.browser.page_source)
  open_url = urljoin(base_url,'/basket_detail')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')
  print(context.browser.page_source)
  # assert 'Super Mario World' in context.browser.page_source

@when(u'we press continue shopping button')
def press_purchase(context):
  link = driver.find_element_by_link_text('Continue Shopping')
  link.click()

@then(u'we go to index page')
def index_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url)
  Assert.assertEquals(URL, open_url );
  assert 'Top 3000 Video Games' in context.browser.page_source

###

@given(u'we have two Super Mario World in basket')
def two_super_mario_world_in_basket(context):
  print(Game.objects.all())
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  # open_url = urljoin(base_url,'')
  open_url1 = urljoin(base_url,'/gamedetail/9019')
  context.browser.get(open_url1)
  quantity_option = context.browser.find_element('name', 'quantity')
  quantity_option.send_keys(2)
  print(context.browser.page_source)
  open_url = urljoin(base_url,'/basket_detail')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')
  print(context.browser.page_source)
  # assert 'Super Mario World' in context.browser.page_source

@when(u'we press purchase button')
def press_purchase(context):
  link = driver.find_element_by_link_text('Purchase')
  link.click()

@then(u'we go to purchase page')
def platform_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/purchase')
  Assert.assertEquals(URL, open_url );
  assert 'You have these in your basket:' in context.browser.page_source

###

@given(u'we go to purchase page')
def print(Game.objects.all())
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  # open_url = urljoin(base_url,'')
  open_url1 = urljoin(base_url,'/gamedetail/9019')
  context.browser.get(open_url1)
  quantity_option = context.browser.find_element('name', 'quantity')
  quantity_option.send_keys(2)
  print(context.browser.page_source)
  open_url = urljoin(base_url,'/basket_detail')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')
  print(context.browser.page_source)
  # assert 'Super Mario World' in context.browser.page_source
  link = driver.find_element_by_link_text('Purchase')
  link.click()
  open_url2 = urljoin(base_url,'/purchase')
  context.browser.get(open_url2)
  print('-----------------',open_url2,'--------------------')
  print(context.browser.page_source)

@when(u'we input card type and number and press payment button')
def purchase_order(context):
  name_textfield = context.browser.find_element('payment', 'payment')
  name_textfield.send_keys('test')
  price_textfield = context.browser.find_element('payment','total')
  price_textfield.send_keys(30)
  context.browser.find_element('payment','submit').click()


@then(u'we go to index page')
def index_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url)
  Assert.assertEquals(URL, open_url );
  assert 'Top 3000 Video Games' in context.browser.page_source