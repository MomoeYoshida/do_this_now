"""
"Do This Now"
Write a program that asks the user for their age and then prints whether it is
odd or even. The program should not crash if the user enters a non-number
(i.e. use exception handling). The program should not allow and invalid age
number. Re-prompt until a valid number is entered
"""
is_valid_input_of_age = False
while not is_valid_input_of_age:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age must be >= 0")
        else:
            is_valid_input_of_age = True
    except ValueError:
        print("Invalid age number")

if age % 2 == 0:
    print("Your age is even")
else:
    print("Your age is odd")
