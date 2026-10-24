# ISM3232 Midterm: Ridgeline Tool Rental

- **Name:** Kaden Brenning
- **Version:** Alpha
- **Date:** October 24, 2026

## What This Program Does
This program includes calculations for the tool rentals provided by Ridgeline Tool Rental. These calculations include a discount, inspection, deposit, and waiver check. Which then provides a summary that lists the rentals and any important information about those rentals.

## Business Rules
1. Uses the daily rate and the number of days and multiplies them to obtain the rental cost.
2. Uses the number of days to decide the discount provided. Fewer than three days is no discount, from three days to six days is ten percent discount, and seven days or above is twenty percent discount.
3. Uses a ten percent discount when the days are fewer than 3 and contractor is true.
4. After the discount is applied, if the cost is less than 150 dollars, there is a 25 dollar fee that is added.
5. After the discount is applied, if the cost is 1000 dollars or greater, then a deposit is required.
6. When the number of days is 5 or greater, and the quote is greater than 800 dollars, an inspection is required.

## How to Run
'''
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && python3 main.py
'''
## How to Test
'''
ruff format . && ruff check . && pytest -v
'''
Contains 25 Tests.
## Files in This Repository
tests/test_business_rules.py is for the 25 tests that ensure that any edge cases would work correctly.
tests/__init__.py is for initial Github setup.
.gitignore is for excluding the files that should not be commited to Github.
README.md is for explaining to a user what the program does and how to use it.
business_rules.py is for the 8 logical rules that calculate the input rentals.
commands.md is for showing a user what was required to build this project.
main.py is for printing the summary output.
requirements.txt is for allowing the correct versions to be installed by the user.

## AI Use Statement
I did not use AI on this exam.