import pytest
import math
from functions import *


# test function 4
#what happens when asserting a palidrome
@pytest.mark.parametrize("temp", ["abba", "ata", "eye", "hey", "creep", "shy", "alpha", "loll", "winw", "1", "1.2", "303",400,4.5])
def test_isPalidrome(temp):
    assert isPalindrome(temp) == True

#testing the log2 function
@pytest.mark.parametrize("num", [1, 2, "hello", 8, 5.5, -1,0])
def test_log2(num):
    assert log2(num) == math.log2(num)
