# test_business_rules.py

from business_rules import (
    calculate_quote,
    calculate_rental_cost,
    format_rental_line,
    get_rental_discount,
    largest_rental,
    needs_inspection,
    requires_deposit,
    total_quoted,
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


def test_discount_contractor_six_days():
    assert get_rental_discount(6, contractor=True) == 0.10


def test_discount_contractor_seven_days():
    assert get_rental_discount(7, contractor=True) == 0.20


def test_waiver_is_applied_below_limit():
    assert calculate_quote(149.00, 1, contractor=False) == 174.00


def test_waiver_not_applied_above_limit():
    assert calculate_quote(150.00, 1, contractor=False) == 150.00


def test_discount_applied_correctly():
    assert calculate_quote(200, 2, contractor=True) == 360.00


def test_deposit_is_required():
    assert requires_deposit(1000) is True


def test_deposit_not_required():
    assert requires_deposit(999) is False


def test_inspection_is_required_over_limit():
    assert needs_inspection(5, 801) is True


def test_inspection_not_required_under_day_limit():
    assert needs_inspection(4, 801) is False


def test_inspection_not_required_at_limit():
    assert needs_inspection(5, 800) is False


def test_largest_rental_tie():
    rentals = [
        {"customer": "One", "daily_rate": 100.00, "days": 5, "contractor": True},
        {"customer": "Two", "daily_rate": 100.00, "days": 2, "contractor": True},
    ]
    assert largest_rental(rentals) == "One"


def test_largest_rental_empty():
    rentals = []
    assert largest_rental(rentals) == ""


def test_total_quoted():
    rentals = [
        {"customer": "One", "daily_rate": 100.00, "days": 1, "contractor": False},
        {"customer": "Two", "daily_rate": 50.00, "days": 2, "contractor": False},
    ]
    assert total_quoted(rentals) == 250.00


def test_format_line_with_double_no():
    test = format_rental_line("Max", 200.00, False, False)
    assert test == "Max: $200.00 | deposit: no | inspection: no"


def test_format_line_with_double_yes():
    test = format_rental_line("Max", 200.00, True, True)
    assert test == "Max: $200.00 | deposit: yes | inspection: yes"


def test_format_line_with_deposit_yes_and_inspection_no():
    test = format_rental_line("Max", 200.00, True, False)
    assert test == "Max: $200.00 | deposit: yes | inspection: no"


def test_format_line_with_deposit_no_and_inspection_yes():
    test = format_rental_line("Max", 200.00, False, True)
    assert test == "Max: $200.00 | deposit: no | inspection: yes"
