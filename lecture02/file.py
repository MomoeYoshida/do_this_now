"""
"Do This Now"
Write Python code for a program that opens a file and toggles "on" and "off"
each time it's  run. So, if the file contains "on", change it to "off" and
vice versa
"""

input_file = open("on_and_off.txt", "r")
line = input_file.readline()
input_file.close()

output_file = open("on_and_off.txt", "w")
if line == "on":
    output_file.write("off")
else:
    output_file.write("on")
output_file.close()
