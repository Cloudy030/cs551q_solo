Feature: compare 2 video games

Scenario: Wii Sports comparing to Super Mario Bros.
  Given we are on index page
  When press Comparision
  Then we see Wii Sports compared to Super Mario Bros.

Scenario: Wii Sports comparing to Super Mario Bros.
  Given we are on compare page
  When press Search
  Then we see Wii Sports compared to Super Mario Bros.

Scenario: Wii Sports comparing to Mario Kart Wii
  Given we are on compare page
  When choose Mario Kart Wii in first slot and press Search
  Then we see Wii Sports compared to Mario Kart Wii

Scenario: Mario Kart Wii comparing to Super Mario Bros.
  Given we are on compare page
  When choose Mario Kart Wii in second slot and press Search
  Then we see Mario Kart Wii compared to Super Mario Bros.

Scenario: Mario Kart Wii comparing to Wii Sports Resort
  Given we are on compare page
  When choose Mario Kart Wii and Wii Sports Resort and press Search
  Then we see Mario Kart Wii comparing to Wii Sports Resort