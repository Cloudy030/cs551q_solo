Feature: purchase a game

Scenario: add Super Mario World to basket
 Given we want to add Super Mario World to basket
 When we click add to basket button
 Then it succeds
 Then we change quantity to two
 Then total price is 100.6
