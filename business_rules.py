# business_rules.py
# Author: Kaden Brenning

FEWER_DAYS = 3
MIDDLE_DAYS = 6
MORE_DAYS = 7

LOW_DISCOUNT = 0
MIDDLE_DISCOUNT = 0.10
HIGH_DISCOUNT = 0.20

DEPOSIT = 1000
INSPECTION_QUOTE = 800
INSPECTION_DAYS = 5

DAMAGE_WAIVER_ADD = 25
DAMAGE_WAIVER_REQ = 150


def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Return rental cost based on rate and number of days"""
    return daily_rate * days


def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Return rental discount based on days and contractor"""
    if contractor is True:
        if days <= MIDDLE_DAYS:
            return MIDDLE_DISCOUNT
        elif days >= MORE_DAYS:
            return HIGH_DISCOUNT
    elif contractor is False:
        if days < FEWER_DAYS:
            return LOW_DISCOUNT
        elif days >= FEWER_DAYS and days <= MIDDLE_DAYS:
            return MIDDLE_DISCOUNT
        elif days >= MORE_DAYS:
            return HIGH_DISCOUNT


def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Returns quote after discount and damage waiver"""
    if (
        calculate_rental_cost(daily_rate, days)
        * (1 - get_rental_discount(days, contractor))
        >= DAMAGE_WAIVER_REQ
    ):
        return calculate_rental_cost(daily_rate, days) * (
            1 - get_rental_discount(days, contractor)
        )
    if (
        calculate_rental_cost(daily_rate, days)
        * (1 - get_rental_discount(days, contractor))
        < DAMAGE_WAIVER_REQ
    ):
        return (
            calculate_rental_cost(daily_rate, days)
            * (1 - get_rental_discount(days, contractor))
            + DAMAGE_WAIVER_ADD
        )


def requires_deposit(quote: float) -> bool:
    """Returns true or false if requires deposit"""
    return quote >= DEPOSIT


def needs_inspection(days: int, quote: float) -> bool:
    """Returns true or false if needs inspection"""
    return quote > INSPECTION_QUOTE and days >= INSPECTION_DAYS


def total_quoted(rentals: list) -> float:
    """Returns the total by adding each quote together"""
    total = 0
    for rental in rentals:
        total += calculate_quote(
            rental["daily_rate"], rental["days"], rental["contractor"]
        )
    return total


def largest_rental(rentals: list) -> str:
    """Returns the largest quote and keeps the first largest"""
    largest = ""
    current_max = 0
    for rental in rentals:
        if (
            calculate_quote(rental["daily_rate"], rental["days"], rental["contractor"])
            > current_max
        ):
            current_max = calculate_quote(
                rental["daily_rate"], rental["days"], rental["contractor"]
            )
            largest = rental["customer"]
    return largest


def format_rental_line(
    customer: str, quote: float, deposit: bool, inspection: bool
) -> str:
    """Returns the customer, quote, deposit, and inspection in one line."""
    if deposit is True:
        deposit_string = "yes"
    else:
        deposit_string = "no"
    if inspection is True:
        inspection_string = "yes"
    else:
        inspection_string = "no"

    return f"{customer}: ${quote:.2f} | deposit: {deposit_string} | inspection: {inspection_string}"
