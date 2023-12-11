# Nathan McGraw
# Introduction to Programming with Python
# Script #6: "If statements (employing AND and OR)"

# Create and print these variables (min = 0, max = 256)
input_min = 0
input_max = 256

# Assign to a new variable user_data the result of an input statement
# that prompts the user for an byte-sized int (from zero - 255).
user_data = int(input("\nPlease input an integer between 0-255 :"))

# Use a compound AND evaluation that checks int(data) is greater than or
# equal to min AND less than max. Print the result.
if (user_data >= input_min) and (user_data < input_max):
    print("\n\t[Input Valid]\n\nGreater than or equal to min, or less than max.")

# Use a compound OR evaluation that checks int(data) is not less than min OR greater
# than or equal to max. Print the result.
elif (user_data < input_min) or (user_data >= input_max):
    print("\n\t[Input Invalid]\n\nLess than zero, or greater than or equal to max.")
else:
    print("You will never get here")
print("\nThank you")
