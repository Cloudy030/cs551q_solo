import urllib
from urllib.parse import urljoin
from behave import given, when, then
from games.models import Year, Genre, Platform, Publisher, Game, Customer
from django.contrib.auth.models import User


@given(u'we are not login')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)


@when(u'go to basket page')
def press_basket(context):
  link = driver.find_element_by_link_text('Shop')
  link.click()

@then(u'we see Log In button')
def login_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/basket_detail')
  Assert.assertEquals(URL, open_url );
  assert 'Log In' in context.browser.page_source

###

@given(u'we are in login page')
def login_page(context):

  user,_=User.objects.create_user(
    first_name='cf1',
    last_name='cl1',
    username='ct',
    email='ct@b.com',
    password='ct1234'
  )
  c1=User.object.get(username='ct')
  customer,_=Customer.objects.get_or_create(
    user_id='502',
    user=c1,
    user_type='Customer',
    address="test address",
    created_date="2023-05-05 08:46:38.856800+00:00"
  )

  print(Customer.objects.all())

  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  # open_url = urljoin(base_url,'')
  open_url = urljoin(base_url,'/accounts/login')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')

@when(u'input wrong credentials')
def wrong_credentials(context):
  username_textfield = context.browser.find_element('Login', 'username')
  username_textfield.send_keys('ct')
  pwd_textfield = context.browser.find_element('Login','password')
  pwd_textfield.send_keys('5555')
  context.browser.find_element('Login','submit').click()


@then(u'we see "Your username and password didn\'t match. Please try again."')
def not_match(context):
  assert 'Your username and password didn't match. Please try again.' in context.browser.page_source

###

@given(u'we are in login page')
def login_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  # open_url = urljoin(base_url,'')
  open_url = urljoin(base_url,'/accounts/login')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')

@when(u'input correct credentials')
def correct_credentials(context):

  print(Customer.objects.all())

  username_textfield = context.browser.find_element('Login', 'username')
  username_textfield.send_keys('ct')
  pwd_textfield = context.browser.find_element('Login','password')
  pwd_textfield.send_keys('ct1234')
  context.browser.find_element('Login','submit').click()


@then(u'we go to index page')
def index_page(context):
  URL = driver.current_url();
  open_url1 = urljoin(base_url)
  Assert.assertEquals(URL, open_url1 );
  assert 'Top 3000 Video Games' in context.browser.page_source

###

@given(u'we are already login')
def login_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  # open_url = urljoin(base_url,'')
  open_url = urljoin(base_url,'/accounts/login')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')
  
  print(Customer.objects.all())

  username_textfield = context.browser.find_element('Login', 'username')
  username_textfield.send_keys('ct')
  pwd_textfield = context.browser.find_element('Login','password')
  pwd_textfield.send_keys('ct1234')
  context.browser.find_element('Login','submit').click()

@when(u'we go to basket page')
def press_basket(context):
  link = driver.find_element_by_link_text('Shop')
  link.click()

@then(u'we see "Welcome back, " with our first name on the basket page')
def basket_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/basket_detail')
  Assert.assertEquals(URL, open_url );
  assert 'Welcome back, ' in context.browser.page_source

###
@given(u'we are in customer account')
def login_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  # open_url = urljoin(base_url,'')
  open_url = urljoin(base_url,'/accounts/login')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')
  
  print(Customer.objects.all())

  username_textfield = context.browser.find_element('Login', 'username')
  username_textfield.send_keys('ct')
  pwd_textfield = context.browser.find_element('Login','password')
  pwd_textfield.send_keys('ct1234')
  context.browser.find_element('Login','submit').click()


@when(u'we go to basket page')
def press_basket(context):
  link = driver.find_element_by_link_text('Shop')
  link.click()

@then(u'we see "Basket", "Log Out", "Purchase", "Continue shopping"')
def basket_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/basket_detail')
  Assert.assertEquals(URL, open_url );
  assert 'Basket' in context.browser.page_source
  assert 'Log Out' in context.browser.page_source
  assert 'Purchase' in context.browser.page_source
  assert 'Continue shopping' in context.browser.page_source