import pytest
import sys
sys.path.append('../WindowsStuff')  # Add the parent directory to the Python path
from app import validate_date  # Replace with the actual module name
from app import valid_address

def add(x, y):
    return x + y

def test_add():
    assert add(3, 3) == 6


#General Tests
#--Positive Num Check (including 0)
def is_positive_number(value):
    if value >= 0:
        return True
    elif value < 0:
        return False

def test_positive_number():
    assert is_positive_number(5) == True

def test_negative_number():
    assert is_positive_number(-2) == False

def test_zero():
    assert is_positive_number(0) == True

##--Date Validation
#--year
def is_valid_year(value):
    if value >= 2025:
        return False
    elif value <= 1900:
        return False
    else:
        return True
    
def test_year_too_high():
    assert is_valid_year(2025) == False    

def test_year_too_low():
    assert is_valid_year(1890) == False  

def test_year_valid():
    assert is_valid_year(1966) == True  

    
#--month
def is_valid_month(value):
    if value >= 13:
        return False
    elif value <= 0:
        return False
    else:
        return True

def test_month_too_high():
    assert is_valid_month(13) == False    

def test_month_too_low():
    assert is_valid_month(0) == False  

def test_month_valid():
    assert is_valid_month(5) == True  

#day
def is_valid_day(value):
    if value >= 32:
        return False
    elif value <= 0:
        return False
    else:
        return True
    
def test_day_too_high():
    assert is_valid_day(33) == False    

def test_day_too_low():
    assert is_valid_day(0) == False  

def test_day_valid():
    assert is_valid_day(2) == True  


#--Testing directly from ../WindowsStuff/app.py
#Date Format Regex Validation
@pytest.mark.parametrize("date_string, expected_result", [
    ("12-31-2023", True),
    ("01-01-2024", True),
    ("13-01-2024", False),  # Invalid month
    ("11-34-2024", False),  # Invalid day
    ("2024-08-26", False),  # Incorrect format
    ("08-26", False),  # Missing year
])
def test_validate_date_format(date_string, expected_result):
    """Tests the validate_date_format function."""
    assert validate_date(date_string) == expected_result

#Address format Regex Validation
@pytest.mark.parametrize("address, expected_result", [
    # Valid address test cases
    ("123 Main St, Springfield, IL 62701", True),
    ("456 Elm St, Anytown, CA 90210", True),
    ("789 Broadway Ave, New York, NY 10001", True),
    ("1010 5th Ave, Los Angeles, CA 90001", True),
    ("1600 Pennsylvania Ave NW, Washington, DC 20500", True),
    
    # Invalid address test cases
    ("123 Main St Springfield, IL 62701", False),  # Missing comma after street
    ("456 Elm St, Anytown, California 90210", False),  # Full state name instead of abbreviation
    ("789 Broadway Ave, NY 10001", False),  # Missing city
    ("Main St, Springfield, IL 62701", False),  # Missing street number
    ("123 Main St, Springfield, IL", False),  # Missing ZIP code
    ("123 Main St, Springfield, IL 6270", False),  # Invalid ZIP code length
    ("", False),  # Empty string
    ("123", False),  # Incomplete address
    ("123 Main St, Springfield, ILL 62701", False),  # Invalid state abbreviation (3 letters)
])
def test_valid_address(address, expected_result):
    """Tests the valid_address function."""
    assert valid_address(address) == expected_result


print("end")