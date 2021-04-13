"""
"Do This Now"
Write Python code to ask the user for a number, and then print that number
multiplied by 2

Write Python code for a program to repeatedly ask the user for a number then
print that number squared. When the user enters zero or a negative number,
stop repeating.
"""

number = int(input("Enter a number: "))
new_number = number * 2
print("The answer is {}".format(new_number))


number = int(input("Enter a number: "))
number_squared = number ** 2
print("The answer is {}".format(number_squared))
while number > 0:
    number = int(input("Enter a number: "))
    number_squared = number ** 2
    print("The answer is {}".format(number_squared))
