# Created by jbettenh at 1/12/2021
Feature: showing off calculator

  Scenario Outline: Check addition
    Given Calculator app is running
    When User inputs "<a>" + "<b>" to calculator
    Then Result is "<out>"

    Examples:
      | a   | b   | out |
      | 1   | 2   | 3   |
      | 0   | 5   | 5   |
      | 1   | 6   | 7   |
      | 5   | 10  | 15  |
      | 95  | 100 | 195 |


  Scenario Outline: Check subtraction
    Given Calculator app is running
    When User inputs "<a>" - "<b>" to calculator
    Then Result is "<out>"

    Examples:
      | a   | b   | out |
      | 10  | 5   | 5   |
      | 0   | 5   | -5  |
      | 7   | 6   | 1   |
      |  25 | 10  | 15  |
      | 100 | 50  | 50  |


  Scenario: Check multiplication
    Given Calculator app is running
    When User inputs "5" * "5" to calculator
    Then Result is "25"


  Scenario: Check division
    Given Calculator app is running
    When User inputs "50" / "5" to calculator
    Then Result is "10"


  Scenario: Check modulo
    Given Calculator app is running
    When User inputs "88" % "2" to calculator
    Then Result is "0"