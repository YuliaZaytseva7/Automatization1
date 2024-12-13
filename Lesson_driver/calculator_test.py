import pytest
from calculator import Calculator

calculator = Calculator()

@pytest.mark.positive_test
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9
    

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-4, -5)
    assert res == -9

def test_sum_negative_and_positive_nums():
    calculator = Calculator()
    res = calculator.sum(-4, 1)
    assert res == -3

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(3.1, 1.5)
    assert res == 4.6

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(3.1, 1.5)
    assert res == 4.6

def test_sum_zero_nums():
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(3.1, 1.5)
    assert res == 4.6

@pytest.mark.positive_test
  def test_sum_div_positive():

    calculator = Calculator()
    res = calculator.div(10, 5)
    assert res == 2      

def test_sum_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)
    

def test_avg_empty_list():
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0

@pytest.mark.positive_test
def test_avg_positive():
    calculator = Calculator()

    numbers = [1,2,3,4,5,6,7,8,9,5]
    res = calculator.avg(numbers)
    assert res == 5

#res = calculator.sum(5.5, 6.6)
#res = round(res, 1) # округлить результат сложения до 1 знака после запятой
#print(res)
#assert res == 12.1


