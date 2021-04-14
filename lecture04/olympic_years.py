"""
"Do This Now"
Write a for loop that prints Olympic years (every 4 years) from 1900 to now
"""
import datetime
CURRENT_YEAR = datetime.date.today().year

for year in range(1900, CURRENT_YEAR + 1, 4):
    print(year)
