#TASK: Build a simple age checker: Ask the user for their age and tell them if they are eligible for certain 
#services (e.g., "You are eligible to vote" or "You are too young to vote")

#name checker
def name_checker():
    name = input(f"Hey there!\nYou are WELCOMED to ModiCybbs Age_Verifier.\nCan you tell me your names?\n")
    return name

#exclaim names with expressions
name = name_checker()
print (f"You are astounding, {name}!.\n")

#function to verify age of individuals
def age_checker():
    while True: #ensures the program keeps asking for inputs until the user keys in the valid age

        try: # tries converting the users input to an integer, if successful, the value is stored

            age = int(input(f"What is your current age\n"))

            break #exit the loop when the value entered is valid

        except ValueError: #detect invalid input (non-integer)
            print(f"Invalid value entered") 
    return age

#age variable to call the function
age = age_checker()

#conditional statements to verify what to do next
if int(age < 18):
    print(f"You are {age} years old, therefore ineligible to vote\n")

elif int(age == 18):
    print(f"You recently turned {age} years. You have legal rights to vote\n")

else: 
    print(f"You have lived for {age} years, go on and vote")