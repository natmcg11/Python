# Nathan McGraw
# Introduction to Programming with Python
# Script 3: Program Flow, Errors and Troubleshooting


# Insert three single line comments, which denote these steps: a) get data, b) compare data, 3) print data

# a): get data
user_input = input("Input any data: ")

# b): compare data
if len(user_input) > 0:
    print("Input Detected")
else:
    print("No user input detected")

# c): print data
if len(user_input) > 0:
    print("Input: '{}' has been validated".format(user_input))
else:
    print("Input: '{}' was invalid - empty string detected".format(user_input))


# Following the 'get data' comment, use input prompt to get a user to enter a word/name/string, save data as a variable.
# Following the 'compare data' comment, check (use if statement) to determine if valid data (length > 0) was received.
# If data==valid, follow a 'print data' comment use the .format() syntax to print a message with the data received.
# If data!=valid, follow a 'print data' comment with a message that invalid data was found.
