import math

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    div = num1 / num2

    print("Your numbers divided is:", div)

## returns the log base 2 of a particular number
def log2(num):
    try:
        return math.log2(num)
    except ValueError:
        return "Error: Input must be a positive number."
    except TypeError:
        return "Error: Input must be a number."

## fuction calls
##Palindrome test
isPalindrome("abba")
isPalindrome("ata")
isPalindrome("hey")
isPalindrome("creep")
isPalindrome("101")
isPalindrome("1.2")