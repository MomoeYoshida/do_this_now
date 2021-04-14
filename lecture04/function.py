"""
"Do This Now"
Write a function that returns the average value of a list of numbers passed
in to it
"""


def main():
    numbers = [2, 3, 5, 7, 9]
    print("The average value of a list of numbers is {}".format(calculate_average(numbers)))


def calculate_average(numbers):
    count = 0
    total = 0
    for number in numbers:
        count += 1
        total += number
    return total / count


main()
