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
  open_url = urljoin(base_url,'/genre')
  Assert.assertEquals(URL, open_url );
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
def platform_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/platform')
  Assert.assertEquals(URL, open_url );
  assert 'Platform' in context.browser.page_source

###
@given(u'we are on index page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)

@when(u'press publisher on navigation bar')
def press_publisher(context):
  link = driver.find_element_by_link_text('Publisher')
  link.click()

@then(u'we go to publisher page')
def publisher_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/publisher')
  Assert.assertEquals(URL, open_url);
  assert 'Publisher' in context.browser.page_source

###
@given(u'we are on index page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)

@when(u'press year on navigation bar')
def press_year(context):
  link = driver.find_element_by_link_text('Year')
  link.click()

@then(u'we go to year page')
def year_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/year')
  Assert.assertEquals(URL, open_url);
  assert 'Year' in context.browser.page_source

###

@given(u'we are on index page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)

@when(u'press comparision on navigation bar')
def press_comparision(context):
  link = driver.find_element_by_link_text('Comparison')
  link.click()

@then(u'we go to compare page')
def platform_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/compare')
  Assert.assertEquals(URL, open_url );
  assert 'Video Games Details Comparision' in context.browser.page_source

###

@given(u'we are on index page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)

@when(u'press Super Mario World in table')
def press_game_name(context):
  link = driver.find_element_by_link_text('Super Mario World')
  link.click()

@then(u'we go to Super Mario World detail page')
def gamedetail_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/gamedetail/15019')
  Assert.assertEquals(URL, open_url );
  assert 'Super Mario World' in context.browser.page_source

###

@given(u'we are on index page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)


@when(u'press Wii in table')
def press_wii(context):
  link = driver.find_element_by_link_text('Wii')
  link.click()

@then(u'we go to Wii detail page')
def wii_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/platform/396')
  Assert.assertEquals(URL, open_url );
  assert 'Wii' in context.browser.page_source

###
@given(u'we are on index page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)

@when(u'press 2006 in table')
def press_2006(context):
  link = driver.find_element_by_link_text('2006')
  link.click()

@then(u'we go to 2006 game page')
def 2006_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/year/635')
  Assert.assertEquals(URL, open_url );
  assert '2006' in context.browser.page_source

###
@given(u'we are on index page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)

@when(u'press Puzzle in table')
def press_puzzle(context):
  link = driver.find_element_by_link_text('Puzzle')
  link.click()

@then(u'we go to Puzzle detail page')
def puzzle_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/genre/186')
  Assert.assertEquals(URL, open_url );
  assert 'PlatfPuzzle games emphasis on problem-solving include logic, pattern recognition, sequence solving, spatial recognition and word completion.orm' in context.browser.page_source

###
@given(u'we are on index page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)


@when(u'press Nitendo in table')
def press_nitendo(context):
  link = driver.find_element_by_link_text('Nitendo')
  link.click()

@then(u'we go to Nitendo detail page')
def nintendo_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/publisher/2118')
  Assert.assertEquals(URL, open_url );
  assert 'Nitendo' in context.browser.page_source