#TASK 6: LISTS AND TUPLES FOR SUM AND AVERAGE CALCULATIONS
#make = list(('apply','make','solve'))
#for items in make:
    #print(items)

#yoke = ['sel','forr','sacred','hot']
#items=0
#while items<len(yoke):
 #   print (yoke[items])
  #  items += 1
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)'''
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)'''

def calculate_sum_and_average():
    # Take a list of numbers as input from the user
    numbers = input("Enter a list of numbers separated by spaces:\n")
    
    # Convert the input string into a list of floats
    try:
        number_list = [float(num) for num in numbers.split()]
        
        # Calculate the sum
        total_sum = sum(number_list)
        
        # Calculate the average
        average = total_sum / len(number_list) if number_list else 0 #if a value is entered solve the problem else return 0 
                                                                    #as the result when nothing is entered. note: empty=false, non-empty=true
        
        # Print the results
        print(f"Sum of numbers: {total_sum}\nAverage of numbers: {average}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Call the function
calculate_sum_and_average()

