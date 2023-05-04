from behave import fixture, use_fixture
import os, urllib
import django
from django import db
from django.test import Client
from django.shortcuts import resolve_url
from django.test import selenium
from django.test.testcases import TestCase
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase, TransactionTestCase
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
django.setup()

# Use the chrome driver specific to your version of Chrome browser and put it in ./driver directory
# the driver needs to have the full file path, so use one of these options to pass full path to driver
# CHROME_DRIVER = os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver')
current_dir = os.path.dirname(os.path.realpath(__file__))
CHROME_DRIVER = os.path.join(current_dir, '/driver/chromedriver') #have / before driver
# if put the driver out of the features folder use 'driver/chromedriver'
chrome_options = Options() # other such as firefox / safari
# comment out the line below if you want to see the browser launch for tests
# possibly add time.sleep() if required
# chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless") # run in terminal not in new webpage (looks good to open in webpage but it is slower)
# try remove headless later to see if that work
# chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
# chrome_options.add_argument("--disable-dev-shm-usage")

'''
sudo apt uninstall -h
(from prof)
sudo apt remove chromium-browser
for in chromium-browser in codio not in local google chrome
sudo apt-get update
sudo apt-get install -y chromium-browser
HOOK-ERROR in before_all: SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 112
Current browser version is 111.0.5563.64 with binary path /usr/bin/chromium-browser
WebDriverException: Message: Service chromedriver unexpectedly exited. Status code was: 127
https://community.atlassian.com/t5/Bitbucket-questions/Chromedriver-unexpectedly-exits-during-pipeline-run/qaq-p/1962260

Exception WebDriverException: Message: unknown error: Chrome failed to start: crashed.
  (chrome not reachable)
  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)

HOOK-ERROR in after_all: SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 113
Current browser version is 112.0.5615.49 with binary path /usr/bin/chromium-browser
'''

# add our browser to the context object so that it can be used in all steps
def before_all(context):
  use_fixture(django_test_runner, context)
  browser = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER)
  # browser = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager("112.0.5615.49").install())
  browser.set_page_load_timeout(time_to_wait=200) #if tests take longer to load put larger number here
  # browser.get('https://www.google.nl/')
  context.browser = browser

def before_scenario(context, scenario):
  context.test = TransactionTestCase()
  context.test.setUpClass()
  context.test.client=Client()
  use_fixture(django_test_case, context)

def after_scenario(context, scenario):
  context.test.tearDownClass()
  db.connections.close_all()
  del context.test

def after_all(context):
  context.browser = webdriver.Chrome()
  # https://stackoverflow.com/questions/41846466/attributeerror-context-object-has-no-attribute-browser
  context.browser.quit()

@fixture
def django_test_runner(context):
  context.test_runner = DiscoverRunner()
  context.test_runner.setup_test_environment()
  context.old_db_config = context.test_runner.setup_databases()
  yield
  context.test_runner.teardown_databases(context.old_db_config)
  context.test_runner.teardown_test_environment()

@fixture
def django_test_case(context):
  context.test_case = LiveServerTestCase
  context.test_case.setUpClass()
  yield
  context.test_case.tearDownClass()
  del context.test_case