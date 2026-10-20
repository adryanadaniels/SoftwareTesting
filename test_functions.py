import pytest
from functions import *


# test function 4
#what happens when asserting a palidrome
@pytest.mark.parametrize("temp", ["abba", "ata", "eye"])
def test_isPalidrome(temp):
    assert isPalindrome(temp) == True
@pytest.mark.parametrize("temp", ["hey", "creep", "shy"])
def test_isPalidrome(temp):
    assert isPalindrome(temp) == False
## testing outliars
@pytest.mark.parametrize("temp", ["alpha", "loll", "winw"])
def test_isPalidrome(temp):
    assert isPalindrome(temp) == True
@pytest.mark.parametrize("temp", ["1", "1.2", "303"])
def test_isPalidrome(temp):
    assert isPalindrome(temp) == True

