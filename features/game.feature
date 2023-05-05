Feature: purchase a game

Scenario: add Super Mario World to basket
 Given we want to add Super Mario World to basket
 When we click add to basket button
 Then it succeds

Scenario: update quantity of Super Mario World to two
  Given we have Super Mario World in basket
  When we change quantity to two
  Then total price is 100.6

Scenario: login required to purchase
  Given we are not login and press the purchase button
  When we are directed to login page
  Then we input registered account credentials
  Then we go to index page

Scenario: go to index page
  Given we have two Super Mario World in basket
  When we press continue shopping button
  Then we go to index page

Scenario: go to purchase page
  Given we have two Super Mario World in basket
  When we press purchase button
  Then we go to purchase page

Scenario: do payment action
  Given we go to purchase page
  When we input card type and number and press payment button
  Then we go to index page