"""
"Do This Now"
Write a program that asks the user for their age and then prints whether it is
odd or even. The program should not crash if the user enters a non-number
(i.e. use exception handling). The program should not allow and invalid age
number. Re-prompt until a valid number is entered

Write a one-line function that determines if someone is an adult based on
their age, passed in. What type will it return? Therefore, what is a good
format for the name?
"""


def main():
    age = get_age()
    if is_adult(age):
        print("You are an adult")
    else:
        print("You are not an adult yet!")
    if is_even(age):
        print("Your age is even")
    else:
        print("Your age is odd")


def get_age():
    """Get age by using exception handling."""
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
    return age


def is_adult(age):
    return age >= 18


def is_even(age):
    return age % 2 == 0


main()
