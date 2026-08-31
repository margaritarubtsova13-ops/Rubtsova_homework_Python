import pytest
from calculator import Calculator

#@pytest.mark.skip(reason="Все в порядке, проверяем функцию skip")
#@pytest.mark.xfail

# Сложение
@pytest.mark.parametrize( 'num_1, num_2, sum', [(4, 5, 9), (-6,-10,-16)])
def test_sum_positive_nums(num_1, num_2, sum):
    calculator = Calculator()
    res = calculator.sum(num_1, num_2)
    print(f"Результат сложения: {res}")
    assert res == sum

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    print(f"Результат сложения: {res}")
    assert res == -16

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    print(f"Результат сложения: {res}")
    assert res == 0

def test_sum_fractions_nums():
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)
    print(f"Результат сложения: {res}")
    assert res == 9.9

def test_sum_positive_and_zero_nums():
    calculator = Calculator()
    res = calculator.sum(10, 0)
    print(f"Результат сложения: {res}")
    assert res == 10

# Деление
def test_div_positive_nums():
    calculator = Calculator()
    res = calculator.div(10, 2)
    print(f"Результат деления: {res}")
    assert res == 5, f"Ожидалось 5, но получено {res}"

# Деление на ноль
def test_div_positive_and_zero_nums():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)
    
        
# Среднее арифметическое
def test_average_nums():
    calculator = Calculator()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    res = calculator.avg(numbers)
    print(res)
    assert res == 5
