import pytest
import math
from functions import *


# test function 4
#what happens when asserting a palidrome
@pytest.mark.parametrize("temp", ["abba", "ata", "eye"])
def test_isPalidrome(temp):
    assert isPalindrome(temp) == True
@pytest.mark.parametrize("temp", ["hello", "world", "python", "programming"])
def test_isNotPalidrome(temp):
    assert isPalindrome(temp) == False
@pytest.mark.parametrize("temp", ["", "a", "aa", "aba"])
def test_isPalidrome_edge_cases(temp):
    assert isPalindrome(temp) == True
@pytest.mark.parametrize("temp", ["019", 123, 1.2341, "hello my name is hello"])
def test_isNotPalidrome_edge_cases(temp):   
    assert isPalindrome(temp) == False

#testing the devide function
@pytest.mark.parametrize("num1, num2", [(10, 2), (20, 4), (15, 3), (100, 5), (50, 10)])
def test_divide(num1, num2):
        assert divide(num1, num2) == num1 / num2
@pytest.mark.parametrize("num1, num2", [(10, 0), (20, 0), (15, 0), (100, 0), (50, 0)])
def test_divide_by_zero(num1, num2):
        assert divide(num1, num2) == num1 / num2
@pytest.mark.parametrize("num1, num2", [("hello", 2), (20, "world"), ("foo", "bar")])
def test_divide_invalid_input(num1, num2):
        assert divide(num1, num2) == num1 / num2
@pytest.mark.parametrize("num1, num2", [(0,0)])
def test_divide_zero_by_zero(num1, num2):
        assert divide(num1, num2) == num1 / num2


#testing the log2 function
@pytest.mark.parametrize("num", [1, 2, -1,0])
def test_int_log2(num):
    assert log2(num) == math.log2(num)
@pytest.mark.parametrize("num", [-1, 0])
def test_log2_invalid_input(num):
    result = log2(num)
    assert log2(num) == result
@pytest.mark.parametrize("num", [1.5, 2.5, 3.5])
def test_float_log2(num):
    assert log2(num) == math.log2(num)
@pytest.mark.parametrize("num", ["hello", "world", "python"])
def test_log2_invalid_input_string(num):
    result = log2(num)
    assert log2(num) == result
def test_log2_large_number():
    num = 1000000
    assert log2(num) == math.log2(num)
def test_log2_small_number():
    num = 0.0001
    assert log2(num) == math.log2(num)

