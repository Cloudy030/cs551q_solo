Feature: staff or admin account features

Scenario: go to login page
  Given we are not login
  When go to basket page
  Then we see Log In button

Scenario: login with wrong credentials
  Given we are in login page
  When input wrong credentials
  Then we see "Your username and password didn't match. Please try again."

Scenario: login with correct credentials
  Given we are in login page
  When input correct credentials
  Then we go to index page

Scenario: check basket after login
  Given we are already login
  When we go to basket page
  Then we see "Welcome back, " with our first name on the basket page

Scenario: see available links in basket page
  Given we are in customer account
  When we are in basket page
  Then we see "Dashboard | Basket | Customers | Orders |", "Log Out", "Purchase", "Continue shopping"

Scenario: see dashboard graph for Super Mario World
  Given we are in dashboard page
  When we choose Super Mario World in the filter
  Then it show sales data for Super Mario World