# test_calculator.py 单元测试
import pytest
from src.Calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(1,2) == 3

def test_sub():
    calc = Calculator()
    assert calc.sub(5,2) == 3

def test_mul():
    calc = Calculator()
    assert calc.mul(2,3) == 6

def test_div():
    calc = Calculator()
    assert calc.div(6,2) == 3