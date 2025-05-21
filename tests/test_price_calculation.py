import pytest
from unittest.mock import patch
from app.calculator.pricing import calculate_busCard_price


# Test standard price with no discount (e.g., adult)
@patch("app.calculator.pricing.validate_inputs")
@patch("app.calculator.pricing.get_discount_rate", return_value=0.0)
def test_adult_no_discount(mock_discount, mock_validate):
    price = calculate_busCard_price(num_zones=3, num_people=2, customer_type="adult")
    assert price == 72.0  # 3 zones * $12 = $36 per person, * 2 = $72


# Test minimum charged zones (should be 2 even if 1 is given)
@patch("app.calculator.pricing.validate_inputs")
@patch("app.calculator.pricing.get_discount_rate", return_value=0.0)
def test_minimum_zones(mock_discount, mock_validate):
    price = calculate_busCard_price(num_zones=1, num_people=1)
    assert price == 24.0  # Minimum 2 zones * $12 = $24


# Test discount applied (e.g., student with 25% discount)
@patch("app.calculator.pricing.validate_inputs")
@patch("app.calculator.pricing.get_discount_rate", return_value=0.25)
def test_discount_applied(mock_discount, mock_validate):
    price = calculate_busCard_price(num_zones=4, num_people=1, customer_type="student")
    expected = 4 * 12 * 0.75  # base price * (1 - discount)
    assert price == round(expected, 2)


# Test for rounding correctness
@patch("app.calculator.pricing.validate_inputs")
@patch("app.calculator.pricing.get_discount_rate", return_value=0.3333)
def test_rounding(mock_discount, mock_validate):
    price = calculate_busCard_price(num_zones=3, num_people=1, customer_type="custom")
    assert price == round(3 * 12 * (1 - 0.3333), 2)


# Test validation call
@patch("app.calculator.pricing.validate_inputs")
@patch("app.calculator.pricing.get_discount_rate", return_value=0.0)
def test_validate_inputs_called(mock_discount, mock_validate):
    calculate_busCard_price(3, 1)
    mock_validate.assert_called_once_with(3, 1)


# Test invalid input via validation exception
@patch("app.calculator.pricing.validate_inputs", side_effect=ValueError("Invalid input"))
def test_invalid_input(mock_validate):
    with pytest.raises(ValueError, match="Invalid input"):
        calculate_busCard_price(0, -1)
