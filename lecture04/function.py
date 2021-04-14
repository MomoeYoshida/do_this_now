"""
"Do This Now"
Write a function that returns the average value of a list of numbers passed
in to it

Write a function that returns the median value (middle when sorted) of a
list of numbers passed in to it
"""
import statistics


def main():
    numbers = [2, 3, 5, 7, 9]
    print("The average value of a list of numbers is {}".format(calculate_average(numbers)))
    print("The median value of a list of numbers is {}".format(get_median(numbers)))


def calculate_average(numbers):
    count = 0
    total = 0
    for number in numbers:
        count += 1
        total += number
    return total / count


def get_median(numbers):
    return statistics.median(numbers)


main()
