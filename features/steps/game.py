import urllib
from urllib.parse import urljoin
from behave import given, when, then
from games.models import Year, Genre, Platform, Publisher, Game

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

###

# @given(u'we have Super Mario World in basket')
# def step_impl(context):
#   print(Game.objects.all())
#   base_url = urllib.request.url2pathname(context.test_case.live_server_url)
#   print('*****************',base_url,'**********************')
#   # open_url = urljoin(base_url,'')
#   open_url = urljoin(base_url,'/basket_detail')
#   context.browser.get(open_url)
#   print('-----------------',open_url,'--------------------')
#   print(context.browser.page_source)
#   assert 'Super Mario World' in context.browser.page_source

# @when(u'we change quantity to two')
# def step_impl(context):
#   print(context.browser.page_source)
#   quantity_option = context.browser.find_element('name', 'quantity')
#   quantity_option.send_keys(2)


# @then(u'total price is 100.6')
# def step_impl(context):
#   assert '100.6' in context.browser.page_source

# ###


# @given(u'we are not login and press the purchase button')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we are not login and press the purchase button')


# @when(u'we input registered account credentials')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When we input registered account credentials')

# @then(u'we go to index page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then we go to index page')

# ###

# @given(u'we have two Super Mario World in basket')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we have two Super Mario World in basket')


# @when(u'we press purchase button')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When we press purchase button')


# @then(u'we go to purchase page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then we go to purchase page')

# ###

# @given(u'we go to purchase page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we go to purchase page')


# @when(u'we input card type and number and press payment button')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When we input card type and number and press payment button')

# @then(u'we go to index page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then we go to index page')