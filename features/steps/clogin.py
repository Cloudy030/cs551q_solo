import urllib
from urllib.parse import urljoin
from behave import given, when, then
from games.models import Year, Genre, Platform, Publisher, Game

@given(u'we are not login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we are not login')


@when(u'go to basket page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When go to basket page')


@then(u'we see Log In button')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we see Log In button')

@given(u'we are in login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we are in login page')


@when(u'input wrong credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When input wrong credentials')


@then(u'we see "Your username and password didn\'t match. Please try again."')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we see "Your username and password didn\'t match. Please try again."')

@when(u'input correct credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When input correct credentials')


@then(u'we go to index page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we go to index page')


@given(u'we are already login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we are already login')


@when(u'we go to basket page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we go to basket page')


@then(u'we see "Welcome back, " with our first name on the basket page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we see "Welcome back, " with our first name on the basket page')