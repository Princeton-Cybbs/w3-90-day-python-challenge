#TASK: Create a simple "countdown" program that counts down from 10 to 1 using a while loop.

import time

"""
#counting down from 10 to 1 with a "for loop"
for i in range (10, 0, -1):
    print(i)
    time.sleep(1)
print(f"Countdown complete")

"""
#creating the maximum variable
count = 10
while count >= 1: #starts counting from in the loop
    print (count) 
    time.sleep(1) #delays the time by a second
    count -= 1 #dont stop counting when the value isnt 1
print(f"Countdown complete")
