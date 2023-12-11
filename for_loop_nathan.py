# Nathan McGraw
# Introduction to Programming with Python
# Script 8: "For Loops, and List Enumeration"

# Code a for loop using the range() function to print one to ten
for each in range(1, 11):
    print("This is step {}".format(each))
print("-Finish-")

# Create and print the variable (countdown = 10)
countdown = 10
print("\nCountdown from [{}]".format(countdown))

# Code another 1-10 loop using range()
for item in range(1, 10):
    # In this loop decrement countdown each time the for loop runs
    countdown -= 1
    # With each pass of the loop print the value of countdown and the range index
    print("Step: {}\nCountdown: [{}]".format(item, countdown))

# Create and print these variables (user_input = '', alpha = ["abcd", "efg", "hijk", "lmnop", "qrs", "tuv", "wxyz"]
alpha = ["abcd", "efg", "hijk", "lmnop", "qrs", "tuv", "wxyz"]
print("\nThe values in alpha are... {}".format(alpha))
user_input = input("\nSearch for a value: \n")

# Code a for loop that evaluates a string (user_input) against each of the values in alpha python list.
# Code an enumerated for loop to evaluate user_input against each value in alpha list.
for each, value in enumerate(alpha):
    # Inside the loop print out the evaluation
    # (i.e., "User string abc, is NOT the same as "abcd", or "User string abcd is the same as "abcd").
    if user_input == value:
        print("\n\tFound the value: [{}], in the collection.".format(user_input))
        # Use break to exit the loop if the string is matched
        break
    else:
        print("\tSearching value [{}]... not found.".format(value))
else:
    print("Value [{}] was not found in the collection.".format(user_input))

print("\nExiting... Have A Nice Day.")
