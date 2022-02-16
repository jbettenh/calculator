Feature: showing off calculator

  Scenario Outline: Check addition
    Given Calculator app is running
    When User inputs "<a>" + "<b>" to calculator
    Then Result is "<out>"

    Examples:
      | a  | b   | out |
      | 1  | 2   | 3   |
      | 0  | 5   | 5   |
      | 1  | 6   | 7   |
      | 5  | 10  | 15  |
      | 95 | 100 | 195 |


  Scenario Outline: Check subtraction
    Given Calculator app is running
    When User inputs "<a>" - "<b>" to calculator
    Then Result is "<output>"

    Examples:
      | a   | b  | output |
      | 10  | 5  | 5      |
      | 0   | 5  | -5     |
      | 7   | 6  | 1      |
      | 25  | 10 | 15     |
      | 100 | 50 | 50     |


  Scenario Outline: Check multiplication
    Given Calculator app is running
    When User inputs "<a>" * "<b>" to calculator
    Then Result is "<output>"

    Examples:
      | a  | b   | output |
      | 0  | 100 | 0      |
      | 1  | 36  | 36     |
      | 5  | 5   | 25     |
      | -1 | 5   | -5     |
      | -6 | -7  | 42     |


  Scenario: Check division
    Given Calculator app is running
    When User inputs "50" / "5" to calculator
    Then Result is "10"


  Scenario Outline: Check modulo
    Given Calculator app is running
    When User inputs "<a>" % "<b>" to calculator
    Then Result is "<output>"

    Examples:
      | a | b | output |
      | 0 | 2 | 0      |
      | 3 | 2 | 1      |
      | 4 | 2 | 0      |