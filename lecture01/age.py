"""
"Do This Now"
Write Python code for a program that asks the user for their age and continues
to do so until they enter a valid age (0 to 150). The program should then
display the user's age

Write Python code to ask the user for their age and tell them if they are an
adult or child.
"""

age = int(input("Enter your age: "))
while not 0 <= age <= 150:
    age = int(input("Enter your age: "))
print("Your age is {}".format(age))

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a child.")