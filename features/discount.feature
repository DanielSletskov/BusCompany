Feature: Get discount rate
  As a bus fare calculator
  I want to return the correct discount rate
  So that different customer types are charged appropriately

  Scenario Outline: Return correct discount for each customer type
    Given I have a customer of type "<customer_type>"
    When I ask for the discount rate
    Then the discount should be <expected_discount>

    Examples:
      | customer_type              | expected_discount |
      | adult                     | 0.0               |
      | student                   | 0.2               |
      | child, above 6 years old | 0.4               |
      | todler, less than 6 years old | 1.0         |
      | pensioner                | 0.25              |
      | unknown                  | 0.0               |
