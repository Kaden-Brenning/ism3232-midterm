# Terminal Record: Ridgeline Tool Rental

## 1. Building the project
```
cd ism3232/
mkdir midterm/
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
pip freeze > requirements.txt
echo '.venv/' > .gitignore
echo '__pycache__' >> .gitignore
touch business_rules.py
touch commands.md
touch main.py
touch README.md
mkdir tests/
cd tests/
touch test_business_rules.py
git init
git remote add origin https://github.com/Kaden-Brenning/ism3232-midterm.git
git branch -m main
git push -u origin main
```
## 2. The virtual environment
```
which python3
```
```
/home/brenning_kaden/ism3232/midterm/.venv/bin/python3
```
This output shows that the virtual environment is active by the path .venv/bin/python3 being at the end.
## 3. The project structure
```
tree -L 2
```
```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
```
The folder __pycache__ is on my computer and not on Github, since it was automatically created and .gitignore stops git add from including it.
## 4. Every function and test
```
rg 'def'
```
```
business_rules.py
20:def calculate_rental_cost(daily_rate: float, days: int) -> float:
25:def get_rental_discount(days: int, contractor: bool = False) -> float:
41:def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
63:def requires_deposit(quote: float) -> bool:
68:def needs_inspection(days: int, quote: float) -> bool:
73:def total_quoted(rentals: list) -> float:
83:def largest_rental(rentals: list) -> str:
99:def format_rental_line(

tests/test_business_rules.py
15:def test_calculate_rental_cost_correct():
19:def test_calculate_rental_cost_one():
23:def test_discount_with_two_days():
27:def test_discount_with_three_days():
31:def test_discount_with_six_days():
35:def test_discount_with_seven_days():
39:def test_discount_contractor_two_days():
43:def test_discount_contractor_six_days():
47:def test_discount_contractor_seven_days():
51:def test_waiver_is_applied_below_limit():
55:def test_waiver_not_applied_above_limit():
59:def test_discount_contractor_applied_correctly():
63:def test_discount_applied_correctly():
67:def test_deposit_is_required():
71:def test_deposit_not_required():
75:def test_inspection_is_required_over_limit():
79:def test_inspection_not_required_under_day_limit():
83:def test_inspection_not_required_at_limit():
87:def test_largest_rental_tie():
95:def test_largest_rental_empty():
100:def test_total_quoted():
108:def test_format_line_with_double_no():
113:def test_format_line_with_double_yes():
118:def test_format_line_with_deposit_yes_and_inspection_no():
123:def test_format_line_with_deposit_no_and_inspection_yes():
```
Business rules defines 8 functions, and test_business_rules defines 25 tests.  
## 5. Which files print
```
rg -l 'print'
```
```
main.py
commands.md
```
The main.py file prints, and business_rules.py is not included, since it runs the logic and not the printing.
## 6. The commit history


