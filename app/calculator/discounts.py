def get_discount_rate(customer_type: str) -> float:
    discount_rates = {
        "adult": 0.0,  # No discount
        "student": 0.2,  # 20% discount
        "child, above 6 years old": 0.4,  # 40% discount
        "todler, less than 6 years old": 1.0,  # 100% discount
        "pensioner": 0.25  # 25% discount
    }
    return discount_rates.get(customer_type.lower(), 0.0)
