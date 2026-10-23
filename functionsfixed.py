import math

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):

    temp = str(temp)
    temp = temp.lower()

    test = temp[::-1]
    if(test == temp):
        return True
    else:
        return False
   
    
## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        div = num1 / num2
        return ("Your numbers divided is: ", div)
    except ZeroDivisionError:
        return("Your numbers divided is: Undefined")
    except ValueError:
        return ("Invalid Input")

## returns the log base 2 of a particular number
def log2(num):
    try:
        result = math.log2(num)
        return (result)
    except ValueError:
        return ("Error: Input must be a positive number")
    except TypeError:
        return ("Error: Input must be a number.")

## fuction calls


