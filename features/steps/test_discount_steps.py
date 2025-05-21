from behave import given, when, then
from app.calculator.discounts import get_discount_rate

@given('I have a customer of type "{customer_type}"')
def step_given_customer_type(context, customer_type):
    context.customer_type = customer_type

@when("I ask for the discount rate")
def step_when_ask_discount(context):
    context.result = get_discount_rate(context.customer_type)

@then("the discount should be {expected_discount:g}")
def step_then_check_discount(context, expected_discount):
    assert context.result == expected_discount, f"Expected {expected_discount}, got {context.result}"
