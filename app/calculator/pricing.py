from .validation import validate_inputs
from .discounts import get_discount_rate

def calculate_busCard_price(
    num_zones: int,
    num_people: int,
    customer_type: str = "adult"
) -> float:
    validate_inputs(num_zones, num_people)

    charged_zones = max(num_zones, 2)
    base_zone_price = 12.0
    base_price_per_person = charged_zones * base_zone_price
    discount = get_discount_rate(customer_type)
    final_price_per_person = base_price_per_person * (1 - discount)

    total_price = final_price_per_person * num_people
    return round(total_price, 2)
