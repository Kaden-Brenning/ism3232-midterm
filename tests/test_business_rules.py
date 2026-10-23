# test_business_rules.py

from business_rules import (
    calculate_quote,
    format_rental_line,
    largest_rental,
    needs_inspection,
    requires_deposit,
    total_quoted,
    calculate_rental_cost,
    get_rental_discount,
)
def test_calculate_rental_cost_correct():
    assert calculate_rental_cost(50.00, 5) == 250.00

def test_calculate_rental_cost_one():
    assert calculate_rental_cost(50.00, 1) == 50.00

def test_discount_with_two_days():
    assert get_rental_discount(2) == 0.00

def test_discount_with_three_days():
    assert get_rental_discount(3) == 0.10

def test_discount_with_six_days():
    assert get_rental_discount(6) == 0.10

def test_discount_with_seven_days():
    assert get_rental_discount(7) == 0.20

def test_discount_contractor_two_days():
    assert get_rental_discount(2, contractor=True) == 0.10

def test_discount_contractor_seven_days():
    assert get_rental_discount(7, contractor=True) == 0.20

def test_waiver_is_applied_below_limit():
    assert calculate_quote(149.00, 1, contractor=False) == 174.00

def test_waiver_not_applied_above_limit():
    assert calculate_quote(150.00, 1, contractor=False) == 150.00

def test_deposit_is_required():
    assert requires_deposit(1000) is True

def test_deposit_not_required():
    assert requires_deposit(999) is False

def test_inspection_is_required():
    assert needs_inspection(5,801) is True

def test_inspection_not_required():
    assert needs_inspection(4, 801) is False