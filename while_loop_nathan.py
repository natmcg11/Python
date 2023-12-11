# Nathan McGraw
# Introduction to Programming with Python
# Script #7: "While Loops, using Counter Variables"

print("Lab #7: While Loops, using Counter Variables")

# Create and print these variables (counter = 0, max = 10 min = 1)
counter, my_max, my_min, my_sum = 0, 10, 1, 0
print("\nCounter: {}, Max: {}, Min: {}".format(counter, my_max, my_min))

# Code a while loop that evaluates counter < max
# When the evaluation is true, use the intended loop area to increment the value of counter = counter + 1
# Also, in that code block print out the updated value of counter
print("\n[Counting up]")
while counter <= my_max:
    print("\tCounter is {}".format(counter))
    counter += 1

# Code another while loop, this one evaluating counter >= min
# When the evaluation is true, use the intended loop area to decrement the value of counter = counter - 1
# Also, in that code block print out the updated value of counter
print("\n[Counting down]")
while counter >= my_min:
    counter -= 1
    print("\tCounter is {}".format(counter))

# Declare and print the variables user_input = 1 user_counter = 0
# Combine a user prompt with a while loop evaluation.
user_input, user_counter = 1, 0

# Code a while loop, that runs until the value of user_input is a negative number (i.e., -1)
# Inside the loop increment (+1) the value of the counter but do not print the value.
# Also update user_input with a casting prompt int(input()) that asks the user to enter a positive or negative number.
while user_input >= 0:
    user_input = int(input("\nPlease enter a positive or negative number: "))
    user_counter += 1
    my_sum += user_input

# Exit the loop by entering a negative number.
# At the end of the loop print out the user_counter value to the screen.
print("\nUser_Counter = {}, Sum of User_Input(s) = {}".format(user_counter, my_sum))

print("\nScript ended. Thank you.")
