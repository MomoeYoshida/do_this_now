"""
"Do This Now"
Ask the user for their name. Tell them how many vowels are in their name.
Example output:
Name: Bobby McAardvark
Out of 16 letters, Bobby McAardvark has 4 vowels
"""
VOWELS = ["a", "i", "u", "e", "o"]

name = input("Enter you name: ")
total = 0
number_of_vowels = 0
for letter in name.lower():
    total += 1
    if letter in VOWELS:
        number_of_vowels += 1
print("Name: {}".format(name))
print("Out of {} letters, {} has {} vowels".format(total, name, number_of_vowels))
