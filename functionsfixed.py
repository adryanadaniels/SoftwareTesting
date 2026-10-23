import math

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):

    #put the code into a try except block to catch any errors
    #or
    #convert the input to a string to handle non-string inputs
    #temp = str(temp)
    try:
        test = temp[::-1]
        if(test == temp):
            return True
        else:
            return False
    except TypeError:
        return False 
    
## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    check = False
    while check == False:
        try:
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
        except ValueError:
            print("Error: Invalid input. Please provide numeric values.")
            check = False
            continue
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            check = False
        elif not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            print("Error: Invalid input. Please provide numeric values.")
            check = False
        else:
            check = True
    div = num1 / num2
    print("Your numbers divided is:", div)

## returns the log base 2 of a particular number
def log2(num):
    try:
        return math.log2(num)
    except ValueError:
        return "Error: Input must be a positive number"
    except TypeError:
        return "Error: Input must be a number."

## fuction calls
##Palindrome test
print(isPalindrome("abba"))
print(isPalindrome("ata"))
print(isPalindrome("hey"))
print(isPalindrome("creep"))
print(isPalindrome("101"))
print(isPalindrome(1.2))
print(isPalindrome(505))
print("\n")
##divide test
divide()
print("\n")
##log2 test
print(log2(1))
print(log2(2))
print(log2("hello"))
print(log2(1.2))
print(log2(-1))
print(log2(0))

