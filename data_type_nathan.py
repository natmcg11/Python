# Nathan McGraw
# Introduction to Programming with Python
# Script 4: User Input, Data Type(s)


string_data = "20"
print("string_data:", string_data)

integer_data = 10
print("integer_data:", integer_data)

modify_data = 5.0
print("modify_data:", modify_data)


# Attempt to add string_data to modify data. Do this inside a print statement to see the result.
# print(string_data + modify_data)

# Attempt to add integer_data to modify data. Do this inside a print statement to see the result.
print("integer_data + modify_data =", integer_data + modify_data)

# Cast (change from a string to an integer) string data, and then attempt to add string_data to modify data (via print)
new_int = int(string_data)
print("modify_data + new_int =", modify_data + new_int)

# Create a new variable, user_data to catch the return value as an integer prompt that asks the user for a number.
user_data = int(input("Please enter an integer: "))

# After data is received print out user_data and its type.
print("User entered:", user_data, type(user_data))

# In a single formatted print statement show user_data added to modify_data, and the sum (values as an expression).
print("user_data ({}) + modify_data ({}) = {}".format(user_data, modify_data, user_data + modify_data))
