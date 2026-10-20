# business_rules.py
# Author: Kaden Brenning

FEWER_DAYS = 3
MIDDLE_DAYS = 6
MORE_DAYS = 7

LOW_DISCOUNT = 0
MIDDLE_DISCOUNT = 0.10
HIGH_DISCOUNT = 0.20


def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Return rental cost based on rate and number of days"""
    return daily_rate * days


def get_rental_discount(days: int, contractor: bool = False) -> float:
    if contractor is True:
        if days < FEWER_DAYS or days >= FEWER_DAYS and days <= MIDDLE_DAYS:
            return (1 - MIDDLE_DISCOUNT) * calculate_rental_cost
        elif days >= MORE_DAYS:
            return (1 - HIGH_DISCOUNT) * calculate_rental_cost
    elif contractor is False:
        if days < FEWER_DAYS:
            return (1 - LOW_DISCOUNT) * calculate_rental_cost
        elif days >= FEWER_DAYS and days <= MIDDLE_DAYS:
            return (1 - MIDDLE_DISCOUNT) * calculate_rental_cost
        elif days >= MORE_DAYS:
            return (1 - HIGH_DISCOUNT) * calculate_rental_cost


# def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:

# def requires_deposit(quote: float) -> bool:

# def needs_inspection(days: int, quote: float) -> bool:

# def total_quoted(rentals: list) -> float:

# def largest_rental(rentals: list) -> str:

# def format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str:
