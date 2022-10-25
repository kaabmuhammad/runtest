import pytest
from fib import Fib

def test_fib_1_equals_1():
    assert Fib(1) == 1

def test_fib_2_equals_1():
    assert Fib(2) == 1

def test_fib_6_equals_8():
    assert Fib(6) == 8

def test_fib_string():
    with pytest.raises(Exception) as err:
        Fib("Hello")
    assert err.type == TypeError
    assert err.value == 'Please enter as string not a number'
 