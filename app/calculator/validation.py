def validate_inputs(num_zones: int, num_people: int):
    if num_zones < 1 or num_people < 1:
        raise ValueError("Zones and number of people must be at least 1.")
