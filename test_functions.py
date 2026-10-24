import pytest
import math
from functionsfixed import *


# test function 4
#what happens when asserting a palidrome, letter caseing, numbers, nothing
def test_isPalidrome():
    assert isPalindrome("abba") == True
def test_isNotPalidrome():
    assert isPalindrome("hello") == False
def test_letter_case():
    assert isPalindrome("Racecar") == True
def test_int_input():
    assert isPalindrome(12321) == True
    assert isPalindrome(12345) == False
def test_float_input():
    assert isPalindrome(1.21) == False
def test_floatTrue_input():
    assert isPalindrome(10.01) == True
def test_empty_string():
    assert isPalindrome("") == True
def test_list_input():
    assert isPalindrome([1,2,3]) == False
def test_none_input():
    assert isPalindrome(None) == False

#TEST 1
def geninputs():
    inputs = ["10", "2"]
    for item in inputs:
        yield item

GEN = geninputs()

def test_divideTrue(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    result = divide()

    assert result == ("Your numbers divided is: ", 5.0)

#TEST 2
def geninputs():
    inputs = ["10", "0"]
    for item in inputs:
        yield item

GEN_ZERO = geninputs()

def test_dividebyZERO(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN_ZERO))
    result = divide()
    
    
    assert result == ("Your numbers divided is: Undefined")  

##TEST 3
def geninputs():
     inputs = ["0", "0"]
     for item in inputs:
         yield item

GEN_ZEROS = geninputs()

def test_divide_zeros(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN_ZEROS))
    result = divide()
        
        
    assert result == ("Your numbers divided is: Undefined") 

##TEST 4
def geninputs():
     inputs = ["hello", "0"]
     for item in inputs:
         yield item

GEN_INVALID = geninputs()

def test_divide_invalid(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN_INVALID))
    result = divide()
        
        
    assert result == ("Invalid Input")  

#testing the log2 function

def test_int_log2():
    result = log2(8)
    assert log2(8) == result
def test_log2_invalid_input():
    assert log2(0) == "Error: Input must be a positive number"
def test_float_log2():
    assert log2(-1.2) == "Error: Input must be a positive number"
def test_floatpositive_log():
    result = log2(3.5)
    assert log2(3.5) == result
def test_log2_invalid_input_string():
    assert log2("hello") == "Error: Input must be a number."
def test_list_input():
    assert log2([1,3,4]) == "Error: Input must be a number."