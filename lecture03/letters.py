"""
"Do This Now"
Write a function to count the letters in string (i.e. count alphabetical
letters, not characters). Check if each char is a member (using in) of
string.ascii_lowercase. Need to import string. Use char.lower() to ignore case
"""
import string


def main():
    text = input("Enter text: ")
    count_letters(text)


def count_letters(text):
    """Count the number of letters in text."""
    letters = 0
    for character in text:
        if character.lower() in string.ascii_lowercase:
            letters += 1
    print("{} letters in the text".format(letters))


main()
