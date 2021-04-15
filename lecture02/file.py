"""
"Do This Now"
Write Python code for a program that opens a file and toggles "on" and "off"
each time it's  run. So, if the file contains "on", change it to "off" and
vice versa
"""

input_file = open("on_and_off.txt", "r")
line = input_file.read()
input_file.close()
if line == "on":
    line = "off"
else:
    line = "on"
output_file = open("on_and_off.txt", "w")
print(line, file=output_file)
output_file.close()
