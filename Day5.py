#TASK: Write a function that takes a number as input and returns the factorial of that number.
import math

def factorial_of_number(): #function to find the factorial of a value
    num = int(input(f"Choose numbers ranging from 1 to 1000 that you wish to find its factorial\n")) #get user input

    while True:
        try:
            if 1 <= num <= 1000: #check if the number is within the valid range
                num1 = math.factorial(num) #module that calculates the factorial of a values
                print(f"Factorial of {num} is {num1}")
                return num, num1
            else:
                print(f"ONLY choose values ranging from 1 to 1000")
            break
        except ValueError:
            print(f"Invalid input")
    
result = factorial_of_number()
if result:
    num, num1 = result