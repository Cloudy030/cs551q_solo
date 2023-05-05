from django.test import Client, TestCase
from django.urls import reverse
from games.models import Year, Genre, Platform, Publisher, Game, Customer
from django.contrib.auth.models import User
from faker import Faker

class TestLogin(TestCase):
  # fixtures =['games_test.json']

  def setUp(self):
    fake = Faker()

    first_name = "Afirst",
    first_name = str('Afirst')
    # last_name = "Alast",
    last_name = str('Afirst')
    username = 'admint'
    # username = username[0]
    user = User.objects.create_user(
    username = username,
    first_name = first_name,
    last_name = last_name,
    email = str('a@b.com'),
    password = '1234')
    customer = Customer.objects.get(user = user)
    customer.user_type = 'Admin'
    customer.address = fake.address(),
    customer.address = str(customer.address[0])
    customer.save()

    first_name = str('Sfirst')
    # last_name = "Alast",
    last_name = str('Sfirst')
    username = 'stafft'
    # username = username[0]
    user = User.objects.create_user(
    username = username,
    first_name = first_name,
    last_name = last_name,
    email = str('s@b.com'), 
    password = '1234')
    customer = Customer.objects.get(user = user)
    customer.user_type = 'Staff'
    customer.address = fake.address(),
    customer.address = str(customer.address[0])
    customer.save()

    first_name = str('Cfirst')
    # last_name = "Alast",
    last_name = str('Cfirst')
    username = 'customert'
    # username = username[0]
    user = User.objects.create_user(
    username = username,
    first_name = first_name,
    last_name = last_name,
    email = str('c@b.com'), 
    password = '1234')
    customer = Customer.objects.get(user = user)
    customer.user_type = 'Customer'
    customer.address = fake.address(),
    customer.address = str(customer.address[0])
    customer.save()

  def test_loginc(self):
    c1 = Customer.objects.get(user_id=3)
    login_url = '/accounts/login/'
    response = self.client.post(login_url, {'username': c1.user.username, 'password': '1234'})
    self.assertEqual(response.url, '/')
    self.assertEqual(response.status_code, 302)
    # print(response.url)
    self.assertRedirects(response, '/')
    # print(user)
    url=reverse('basket_detail')
    # response=self.client.get(url)
    # print(url)
    response1 = self.client.get(url)
    # print('!!!!!!',response1.content)
    # response1 = self.client.get(response.url)
    # print(response1.content)
    self.assertContains(response1, f'Welcome back, <strong>{c1.user.first_name}</strong>')

  def test_logins(self):
    s1 = Customer.objects.get(user_id=2)
    login_url = '/accounts/login/'
    response = self.client.post(login_url, {'username': s1.user.username, 'password': '1234'})
    self.assertEqual(response.url, '/')
    self.assertEqual(response.status_code, 302)
    # print(response.url)
    self.assertRedirects(response, '/')
    # print(user)
    url=reverse('basket_detail')
    # response=self.client.get(url)
    # print(url)
    response1 = self.client.get(url)
    # print('!!!!!!',response1.content)
    # response1 = self.client.get(response.url)
    # print(response1.content)
    self.assertContains(response1, f'Welcome back, <strong>{s1.user.first_name}</strong>')

  def test_logina(self):
    a1 = Customer.objects.get(user_id=1)
    login_url = '/accounts/login/'
    response = self.client.post(login_url, {'username': a1.user.username, 'password': '1234'})
    self.assertEqual(response.url, '/')
    self.assertEqual(response.status_code, 302)
    # print(response.url)
    self.assertRedirects(response, '/')
    # print(user)
    url=reverse('basket_detail')
    # response=self.client.get(url)
    # print(url)
    response1 = self.client.get(url)
    # print('!!!!!!',response1.content)
    # response1 = self.client.get(response.url)
    # print(response1.content)
    self.assertContains(response1, f'Welcome back, <strong>{a1.user.first_name}</strong>')

  def test_logout(self):
    a1 = Customer.objects.get(user_id=1)
    login_url = '/accounts/login/'
    response = self.client.post(login_url, {'username': a1.user.username, 'password': '1234'})
    self.assertEqual(response.url, '/')
    self.assertEqual(response.status_code, 302)
    # print(response.url)
    self.assertRedirects(response, '/')
    # print(user)
    url=reverse('basket_detail')
    # response=self.client.get(url)
    # print(url)
    response1 = self.client.get(url)
    # print('!!!!!!',response1.content)
    # response1 = self.client.get(response.url)
    # print(response1.content)
    self.assertContains(response1, f'Welcome back, <strong>{a1.user.first_name}</strong>')
    
    logout_url = '/accounts/logout/'
    response2 = self.client.post(logout_url)
    self.assertEqual(response2.status_code, 302)
    # print(response.url)
    self.assertRedirects(response2, '/')

    url2=reverse('basket_detail')
    # response=self.client.get(url)
    # print(url)
    response3 = self.client.get(url)
    # print('!!!!!!',response1.content)
    # response1 = self.client.get(response.url)
    # print(response1.content)
    self.assertContains(response3, 'Log In')


  # def test_customer_list_view(self):
  #   s1 = Customer.objects.get(user_id=2)
  #   login_url = '/accounts/login/'
  #   response = self.client.post(login_url, {'username': s1.user.username, 'password': '1234'})
  #   self.assertEqual(response.url, '/')
  #   self.assertEqual(response.status_code, 302)
  #   self.assertRedirects(response, '/')
  #   url=reverse('basket_detail')
  #   response = self.client.get(url)
  #   self.assertContains(response, f'Welcome back, <strong>{s1.user.first_name}</strong>')
    
  #   response1 = self.client.get(reverse('customer_list'))
  #   # url1=reverse('customer_list')
  #   # response1=self.client.get(url1)
  #   # print('~~~~~~~~~',url1)
  #   print('+++++++',response1.content)
  #   # response = self.client.get('/customer_list')
  #   # print(url)
  #   # print('+++++++++++++++++++++',response)
  #   # print('+++++++++++++++',response.context)
  #   # self.assertEqual(response.status_code,200)
  #   self.assertContains(response, "Their username is")
  #   self.assertContains(response, "and they live at")
  #   self.assertContains(response, ". You can reach them at ")

  # def test_dashboard_view(self):
  #   url=reverse('dashboard')
  #   response=self.client.get(url)
  #   self.assertEqual(response.status_code,200)
  #   self.assertContains(response, "Account numbers")

  # def test_order_list_view(self):
  #   url=reverse('order_list')
  #   response=self.client.get(url)
  #   self.assertEqual(response.status_code,200)
  #   self.assertContains(response, "Order List")

  # def test_purchase_view(self):
  #   url=reverse('purchase')
  #   response=self.client.get(url)
  #   self.assertEqual(response.status_code,200)
  #   self.assertContains(response, "The total for all of video game(s) is: ")