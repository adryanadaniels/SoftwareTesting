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
    return math.log2(num)


## calls to the functions if you want to run them to test things out can be placed below here
## please make sure they're not actually in the code (uncommented out) when running pytest --
## it can break things

