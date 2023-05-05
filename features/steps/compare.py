import urllib
from urllib.parse import urljoin
from behave import given, when, then
from games.models import Year, Genre, Platform, Publisher, Game

@given(u'we are on index page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)

@when(u'press Comparision')
def press_platform(context):
  link = driver.find_element_by_link_text('Comparision')
  link.click()

@then(u'we see Wii Sports compared to Super Mario Bros.')
def platform_page(context):
  URL = driver.current_url();
  open_url = urljoin(base_url,'/compare')
  Assert.assertEquals(URL, open_url );
  assert 'Wii Sports' in context.browser.page_source
  assert 'Super Mario Bros.' in context.browser.page_source

###

@given(u'we are on compare page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)
  open_url = urljoin(base_url,'/compare')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')

@when(u'press Search')
def press_platform(context):
  link = driver.find_element_by_link_text('Search')
  link.click()

@then(u'we see Wii Sports compared to Super Mario Bros.')
def platform_page(context):
  assert 'Wii Sports' in context.browser.page_source
  assert 'Super Mario Bros.' in context.browser.page_source

###

@given(u'we are on compare page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)
  open_url = urljoin(base_url,'/compare')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')

@when(u'choose Mario Kart Wii in first slot and press Search')
def press_platform(context):
  g1 = context.browser.find_element('compare', 'gamec1')
  g1.send_keys(3)
  link = driver.find_element_by_link_text('Search')
  link.click()

@then(u'we see Wii Sports compared to Mario Kart Wii')
def platform_page(context):
  assert 'Wii Sports' in context.browser.page_source
  assert 'Mario Kart Wii' in context.browser.page_source

###

@given(u'we are on compare page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)
  open_url = urljoin(base_url,'/compare')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')

@when(u'choose Mario Kart Wii in second slot and press Search')
def press_platform(context):
  g1 = context.browser.find_element('compare', 'gamec2')
  g1.send_keys(3)
  link = driver.find_element_by_link_text('Search')
  link.click()

@then(u'we see Mario Kart Wii compared to Super Mario Bros.')
def platform_page(context):
  assert 'Mario Kart Wii' in context.browser.page_source
  assert 'Super Mario Bros.' in context.browser.page_source

###

@given(u'we are on compare page')
def on_index_page(context):
  base_url = urllib.request.url2pathname(context.test_case.live_server_url)
  print('*****************',base_url,'**********************')
  context.browser.get(base_url)
  open_url = urljoin(base_url,'/compare')
  context.browser.get(open_url)
  print('-----------------',open_url,'--------------------')

@when(u'choose Mario Kart Wii and Wii Sports Resort and press Search')
def press_platform(context):
  g1 = context.browser.find_element('compare', 'gamec1')
  g1.send_keys(3)
  g2 = context.browser.find_element('compare', 'gamec2')
  g2.send_keys(4)
  link = driver.find_element_by_link_text('Search')
  link.click()

@then(u'we see Mario Kart Wii comparing to Wii Sports Resort')
def platform_page(context):
  assert 'Mario Kart Wii' in context.browser.page_source
  assert 'Wii Sports Resort' in context.browser.page_source