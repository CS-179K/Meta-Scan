import pytest

def add(x, y):
    return x + y

def test_add():
    assert add(3, 3) == 6

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
