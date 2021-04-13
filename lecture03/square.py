"""
"Do This Now"
Write a function (with a good docstring) that takes in a number and returns
the number squared
"""


def main():
    number = int(input("Enter number: "))
    square(number)
    print("{}^2 = {}".format(number, square(number)))


def square(number):
    """Square the number."""
    return number ** 2


main()
