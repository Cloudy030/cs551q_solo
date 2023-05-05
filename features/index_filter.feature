Feature: filter function on index.html

Scenario: filter Super Mario World with one parameter
  Given we have one filter parameter
  When press Search
  Then we see Super Mario World in result table

Scenario: filter Super Mario World with two parameters
  Given we have two filter parameters
  When press Search
  Then we see Super Mario World in result table

Scenario: filter Super Mario World with three parameters
  Given we have three filter parameters
  When press Search
  Then we see Super Mario World in result table

Scenario: filter Super Mario World with four parameters
  Given we have four filter parameters
  When press Search
  Then we see Super Mario World in result table