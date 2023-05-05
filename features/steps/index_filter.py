import urllib
from urllib.parse import urljoin
from behave import given, when, then
from games.models import Year, Genre, Platform, Publisher, Game

@given(u'we have one filter parameter')
def index_1filter(context):

  year,_=Year.objects.get_or_create(year_no='2000')
  genre,_=Genre.objects.get_or_create(genre_name='Action', genre_description='test description for Action')
  platform,_=Platform.objects.get_or_create(platform_name='PC', url='https://tse1.mm.bing.net/th?id=OIP.FgBGMlSrG14nR-JQZbWUaQHaEJ&pid=Api')
  publisher,_=Publisher.objects.get_or_create(publisher_name='Nintendo')
  game,_=Game.objects.get_or_create(id='9019', rank='20', name='Super Mario World', platform=platform, year=year, genre=genre, publisher=publisher,
  na_sales='1.1', eu_sales='2.2', jp_sales='3.3', other_sales='4.4', global_sales='11', price='50.3')

  print(Game.objects.all())

  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)
  platform = context.browser.find_element('plfilter', 'platform_name')
  platform.send_keys('PC')
  # context.browser.find_element('name','submit').click()

@when(u'press Search')
def press_Search(context):
  link = driver.find_element_by_link_text('Search')
  link.click()

@then(u'we see Super Mario World in result table')
def see_super_mario_world_in_result(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/gamefilter')
  Assert.assertEquals(URL, open_url );
  assert 'Super Mario World' in context.browser.page_source
###

@given(u'we have two filter parameter')
def index_2filter(context):

  # year,_=Year.objects.get_or_create(year_no='2000')
  # genre,_=Genre.objects.get_or_create(genre_name='Action', genre_description='test description for Action')
  # platform,_=Platform.objects.get_or_create(platform_name='PC', url='https://tse1.mm.bing.net/th?id=OIP.FgBGMlSrG14nR-JQZbWUaQHaEJ&pid=Api')
  # publisher,_=Publisher.objects.get_or_create(publisher_name='Nintendo')
  # game,_=Game.objects.get_or_create(id='9019', rank='20', name='Super Mario World', platform=platform, year=year, genre=genre, publisher=publisher,
  # na_sales='1.1', eu_sales='2.2', jp_sales='3.3', other_sales='4.4', global_sales='11', price='50.3')

  print(Game.objects.all())

  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)
  platform = context.browser.find_element('plfilter', 'platform_name')
  platform.send_keys('PC')
  year = context.browser.find_element('yfilter', 'year_no')
  year.send_keys('2000')
  # context.browser.find_element('name','submit').click()

@when(u'press Search')
def press_Search(context):
  link = driver.find_element_by_link_text('Search')
  link.click()

@then(u'we see Super Mario World in result table')
def see_super_mario_world_in_result(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/gamefilter')
  Assert.assertEquals(URL, open_url );
  assert 'Super Mario World' in context.browser.page_source

###

@given(u'we have three filter parameter')
def index_3filter(context):

  # year,_=Year.objects.get_or_create(year_no='2000')
  # genre,_=Genre.objects.get_or_create(genre_name='Action', genre_description='test description for Action')
  # platform,_=Platform.objects.get_or_create(platform_name='PC', url='https://tse1.mm.bing.net/th?id=OIP.FgBGMlSrG14nR-JQZbWUaQHaEJ&pid=Api')
  # publisher,_=Publisher.objects.get_or_create(publisher_name='Nintendo')
  # game,_=Game.objects.get_or_create(id='9019', rank='20', name='Super Mario World', platform=platform, year=year, genre=genre, publisher=publisher,
  # na_sales='1.1', eu_sales='2.2', jp_sales='3.3', other_sales='4.4', global_sales='11', price='50.3')

  print(Game.objects.all())

  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)
  platform = context.browser.find_element('plfilter', 'platform_name')
  platform.send_keys('PC')
  year = context.browser.find_element('yfilter', 'year_no')
  year.send_keys('2000')
  publisher = context.browser.find_element('pufilter', 'publisher_name')
  publisher.send_keys('Nintendo')
  # context.browser.find_element('name','submit').click()

@when(u'press Search')
def press_Search(context):
  link = driver.find_element_by_link_text('Search')
  link.click()

@then(u'we see Super Mario World in result table')
def see_super_mario_world_in_result(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/gamefilter')
  Assert.assertEquals(URL, open_url );
  assert 'Super Mario World' in context.browser.page_source

###

@given(u'we have four filter parameter')
def index_4filter(context):

  year,_=Year.objects.get_or_create(year_no='2000')
  genre,_=Genre.objects.get_or_create(genre_name='Action', genre_description='test description for Action')
  platform,_=Platform.objects.get_or_create(platform_name='PC', url='https://tse1.mm.bing.net/th?id=OIP.FgBGMlSrG14nR-JQZbWUaQHaEJ&pid=Api')
  publisher,_=Publisher.objects.get_or_create(publisher_name='Nintendo')
  game,_=Game.objects.get_or_create(id='9019', rank='20', name='Super Mario World', platform=platform, year=year, genre=genre, publisher=publisher,
  na_sales='1.1', eu_sales='2.2', jp_sales='3.3', other_sales='4.4', global_sales='11', price='50.3')

  print(Game.objects.all())

  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)
  platform = context.browser.find_element('plfilter', 'platform_name')
  platform.send_keys('PC')
  year = context.browser.find_element('yfilter', 'year_no')
  year.send_keys('2000')
  publisher = context.browser.find_element('pufilter', 'publisher_name')
  publisher.send_keys('Nintendo')
  genre = context.browser.find_element('gfilter', 'genre_name')
  genre.send_keys('Action')
  # context.browser.find_element('name','submit').click()

@when(u'press Search')
def press_Search(context):
  link = driver.find_element_by_link_text('Search')
  link.click()

@then(u'we see Super Mario World in result table')
def see_super_mario_world_in_result(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/gamefilter')
  Assert.assertEquals(URL, open_url );
  assert 'Super Mario World' in context.browser.page_source