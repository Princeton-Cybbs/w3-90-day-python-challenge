# Name inpput and age calculation based on current year
import datetime

#function to take in age and inputs
def greet():
    name = input(f"What is your name\n")
    age = int(input(f"How old are you?\n"))
    return name, age

#function to calculate age
def birth_year(age):
    current_year = datetime.datetime.now().year
    x = current_year - age
    return x

#used variables
name, age = greet()
x = birth_year(age)

#outputs the results
print (f"Hey {name}!\nYou are {age} years old\nYou were born in the year {x}")

