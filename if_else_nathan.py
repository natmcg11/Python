# Nathan McGraw
# Introduction to Programming with Python
# Script #5: "If, Elif, Else"

# Create and print these variables (year = 2023)
year = 2023

print("The current year is ", year)

# Assign to a new variable user_data the result of an input statement that prompts the user for a year (4-digit int).
user_data = input("\nPlease enter a year (4 digit integer, ex: 2015): ")

# Convert the data received (from string to int) and print out a confirmation with its value and data type.
int_user_data = int(user_data)

print("\tint_user_data is {} {}".format(int_user_data, type(int_user_data)))

if year == int_user_data:
    print("\nInput year is the same!")
elif year > int_user_data:
    print("\nYear {} is greater than {}.".format(year, int_user_data))
else:
    print("\nYear {} is less than {}.".format(year, int_user_data))
