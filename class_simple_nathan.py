# Nathan McGraw
# Introduction to Programming with Python
# Script 18: "Simple Class Declaration"

# (1) Create a properly configured (with headers) python file named: class_simple_yourname.py

# (3)Above the main function create a python class named Person that contains two string data members; preferred_name and life_goal.
class Person:
    """..."""

    preferred_name = ''
    life_goal = ''

    # (4)The class constructor should take two string variables and use those values to update preferred_name and life_goal, using Python's 'self.' syntax.
    def __init__(self, name, goal):
        """..."""
        self.preferred_name = name
        self.life_goal = goal
        return

    # (5)Create a method for the class called describe_person which, when called, will print out the string: "The goal of {preferred_name} is to {life_goal}.", which prints values instead of the {variable} names.
    def describe_person(self):
        print(f"The goal of {self.preferred_name} is to {self.life_goal}.")
        return


# (2)Create and call a function named main that takes no data and returns no data.
def main():
    print("\nWelcome to the 'Simple Class File' Lab")

    # (6)Inside main, create a new object of type Person, giving it both a name and a goal (as strings).
    me = Person("Happy", "to be good")

    # (7)Once the new object is created, call the .describe_person() method to see the two traits printed to the screen.
    me.describe_person()
    return


main()
