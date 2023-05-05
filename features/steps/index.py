import urllib
from urllib.parse import urljoin
from behave import given, when, then
from selenium.webdriver.common.by import By
from games.models import Year, Genre, Platform, Publisher, Game

@given(u'we are on index page')
def on_index_page(context):
  # year,_=Year.objects.get_or_create(year_no='2000')
  # genre,_=Genre.objects.get_or_create(genre_name='Action', genre_description='test description for Action')
  # platform,_=Platform.objects.get_or_create(platform_name='PC', url='https://tse1.mm.bing.net/th?id=OIP.FgBGMlSrG14nR-JQZbWUaQHaEJ&pid=Api')
  # publisher,_=Publisher.objects.get_or_create(publisher_name='Nintendo')
  # game,_=Game.objects.get_or_create(id='9019', rank='20', name='Super Mario World', platform=platform, year=year, genre=genre, publisher=publisher,
  # na_sales='1.1', eu_sales='2.2', jp_sales='3.3', other_sales='4.4', global_sales='11', price='50.3')

  # print(Game.objects.all())

  # base_url = 'https://wheelpioneer-bananashock-8000.codio-box.uk'
  '''
  only work if the server is alreay already running
  '''
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)
  # open_url = urljoin(base_url,'')
  # open_url = urljoin(base_url,'/gamedetail/9019')
  # context.browser.get(open_url)
  # print('-----------------',open_url,'--------------------')

@when(u'press genre on navigation bar')
def press_genre(context):
  link = driver.find_element_by_link_text('Genre')
  link.click()
  # driver.find_element(By.LINK_TEXT, "Genre").click()
  # context.browser.find_element('game','submit').click()

@then(u'we go to genre page')
def genre_page(context):
  URL = driver.current_url();
  Assert.assertEquals(URL, "http://localhost:8080/genre" );
  assert 'Genre' in context.browser.page_source

###

@given(u'we are on index page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)

@when(u'press platform on navigation bar')
def press_platform(context):
  link = driver.find_element_by_link_text('Platform')
  link.click()

@then(u'we go to platform page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we go to platform page')


# ###
# @given(u'we are on index page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we are on index page')



# @when(u'press publisher on navigation bar')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When press publisher on navigation bar')


# @then(u'we go to publisher page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then we go to publisher page')
# ###
# @given(u'we are on index page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we are on index page')



# @when(u'press year on navigation bar')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When press year on navigation bar')


# @then(u'we go to year page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then we go to year page')

# ###

# @given(u'we are on index page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we are on index page')


# @when(u'press comparision on navigation bar')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When press shop on navigation bar')


# @then(u'we go to compare page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then we go to basket page')


# ###

# @given(u'we are on index page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we are on index page')


# @when(u'press Super Mario World in table')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When press Super Mario World in table')


# @then(u'we go to Super Mario World detail page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then we go to Super Mario World detail page')
# ###
# @given(u'we are on index page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we are on index page')



# @when(u'press Wii in table')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When press Wii in table')


# @then(u'we go to Wii detail page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then we go to Wii detail page')

# ###
# @given(u'we are on index page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we are on index page')


# @when(u'press 2006 in table')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When press 2006 in table')


# @then(u'we go to 2006 game page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then we go to 2006 game page')

# ###
# @given(u'we are on index page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we are on index page')


# @when(u'press Puzzle in table')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When press Puzzle in table')


# @then(u'we go to Puzzle detail page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then we go to Puzzle detail page')

# ###
# @given(u'we are on index page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we are on index page')



# @when(u'press Nitendo in table')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When press Nitendo in table')


# @then(u'we go to Nitendo detail page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then we go to Nitendo detail page')