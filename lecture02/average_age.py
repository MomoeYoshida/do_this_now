"""
"Do This Now"
Write a program to calculate the average age of a group of people, of unknown
size. Use a negative number as the 'sentinel' (when to stop)
"""

total = 0
count = 0
age = int(input("Enter your age: "))
while age >= 0:
    total += age
    count += 1
    age = int(input("Enter your age: "))
average_age = total / count
print("The average age of a group of people is {}".format(average_age))
