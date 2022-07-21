import pytest

class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a + b
        
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")

def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    # Changing calculator's name
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)
    
    assert True

def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    
    assert True
    
def test_subtract():
    calc = Calculator("calculator") ## Convert class into Object
    assert calc.subtract(10,5) == 5
    assert calc.subtract(50,100) == -50
    assert calc.subtract(25,5) == 20
    
def test_multiply():
    calc = Calculator("calculator") ## Convert class into Object
    assert calc.multiply(2,3) == 6
    assert calc.multiply(-50,-100) == 5000
    assert calc.multiply(25,-5) == -125