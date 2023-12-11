# Nathan McGraw
# Introduction to Programming with Python
# Script 24: "Script 24: "Using Python Libraries (e.g., random)"

# (1) Create a properly configured (with headers) python file named: library_yourname.py
# (2) Create and call a function named main that takes no data and returns no data.
# (3) Above the main function, add an import statement (import random) separated from main by two blank lines.
import random


# (4) Create and call a function named random_simple that uses the Python random.randint()
# function to pick a number from one to ten. Print the result to the screen.
def random_simple():
    print(f'\n\t[Random integer: {random.randint(1,10)}]')
    return


# (5) Create and call a function named random_choice that uses the Python random.choice() function inside a loop that
# picks a value from a list named get_random_item with the values ["one", "two", "three", "four", "five"] five times.
# Print the results of each selection to the screen.
def random_choice():
    get_random_item = ["One", "Two", "Three", "Four", "Five"]
    for each in range(0, 5):
        print(f"\tRandom string: {random.choice(get_random_item)}")
    return


# (6) Create and call a function named random_float which implements Pythons random.random() function, nested inside a
# loop, which will continuously pick a random number until a number is selected which is greater-than-or-equal-to .50
# Save the value of each number less-than .50 selected into a Python list, and return the list to the caller once the
# loop has ended. Print the returned list to the screen.
def random_float():
    this_float = float(random.random())
    float_list = list()
    while this_float < 0.5:
        float_list.append(this_float)
        this_float = random.random()
    if len(float_list) == 0:
        print("\n\tNo float greater than .5 was generated")
    else:
        print(f"\n\tList of floats: {float_list}")
    return


# (7) Create and call an interactive function named random_dice that makes use of a Python random integer number function
# to simulate the roll of a dice. Each time the user ‘rolls the dice’, generate a number between 1 and 6 (inclusive) save the results to a python dictionary
def random_dice():
    roll_end = '0'
    roll_count = 1
    roll_name = 'Roll '
    roll_dictionary = dict()
    while roll_end != '1':
        dict_name = roll_name + str(roll_count)
        roll_dictionary[dict_name] = random.randint(1,6)
        print(f"\n\tDice Roll: {roll_dictionary[dict_name]}")
        roll_end = input("\nPress enter to roll again, or enter 1 to exit: ")
        roll_count += 1
    return print(roll_dictionary)


def main_menu():
    print("\nMain Menu")
    print("\t1) Display Random Number from 1-10")
    print("\t2) Display Five Randomly Selected Strings 1 - 5")
    print("\t3) Display Float Data Greate than .5")
    print("\t4) Dice Roll Simulator")
    print("\t5) Exit")


def main():
    user_select = 0
    while user_select != '5':
        main_menu()
        user_select = input("\nPlease make a selection: ")
        if user_select == '1':
            random_simple()
        elif user_select == '2':
            random_choice()
        elif user_select == '3':
            random_float()
        elif user_select == '4':
            random_dice()


main()
