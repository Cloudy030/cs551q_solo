import urllib
from urllib.parse import urljoin
from behave import given, when, then

# @given(u'we want to add Super Mario World to basket')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given we want to add Super Mario World to basket')


# @when(u'we click add to basket button')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When we click add to basket button')


# @then(u'it succeds')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then it succeds')

@given(u'we want to add Super Mario World to basket')
def user_on_gamedetailpage(context):
  base_url = 'https://wheelpioneer-bananashock-8000.codio-box.uk'
  '''
  only work if the server is alreay already running
  '''
  # base_url = urllib.request.url2pathname(context.test_case.live_server_url)
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