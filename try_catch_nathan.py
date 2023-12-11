# Nathan McGraw
# Introduction to Programming with Python
# Script 20: "Object Creation and Error Handling as Try-Except"

# (1) Create a properly configured (with headers) python file named: try_catch_yourname.py
# (3) Above the main function create a python class named Error_Class that takes no data.
class Error_Class:
    # (4) The constructor __init__() method, has no additional parameters, and when called prints a message 'The Error_Class constructor has been called.'
    def __init__(self):
        print("\nThe Error_Class constructor has been called.")
        return

    # (5) Inside the class definition, create three methods being named; catch_zero(), catch_file_not_found(), and catch_import_error(), which each takes and returns no data.
    def catch_zero(self):
        # (6) In the catch_zero method use a try-except block to handle the Python ZeroDivisionError. In the try block section try to divide a number by zero, and catch this error in the except block.
        try:
            bad_result = 1 / 0
        except ZeroDivisionError as e:
            print(f"\nIn the function 'catch_zero', a ZeroDivisionError was detected.\n\tThe ZeroDivisionError message is:\n\t\t{e}")
        return

# (7) In the catch_file_not_found method use try-except block to handle the Python FileNotFoundError Error. In the try block section call for a non-existent file, and catch this error in the except block.
    def catch_file_not_found(self):
        try:
            with open("notthere.txt", 'r') as nt:
                pass
        except FileNotFoundError as e:
            print(f"\nIn the function 'catch_file_not_found', a FileNotFound error was detected.\n\tThe FileNotFound error message is:\n\t\t{e}")
        return

#  (8) For the catch_import_error, use a try-except block to handle the Python ImportError Exception. In the try block section attempt to import a non-existent module, and catch this error in the except block.
    def catch_import_error(self):
        try:
            import not_a_library
        except ImportError as e:
            # (9) For each Error/Exception caught, print out the function name and the error that is caught.
            print(f"\nIn the function 'catch_import_error', a ImportError was detected.\n\tThe ImportError message is:\n\t\t{e}")
        return


# (2) Create and call a function named main that takes no data and returns no data.
def main():
    # (10) Inside the main function, instantiate an object of type Error_Class, and print a welcome message to the user.
    print("\nWelcome to the 'Try-Catch' with Classes Lab")
    e1 = Error_Class()

    # (11) After the object is created, display a menu-driven interface (using a loop) that allows a user to navigate the error functions. Provide an exit option to allow the user to exit the program.
    user_choice = -1
    while user_choice != 4:
        print("\n\tMain Error Menu:")
        print('\t\t1) FileNotFoundError')
        print('\t\t2) ZeroDivisionError')
        print('\t\t3) ImportError')
        print('\t\t4) Exit')

        user_choice = int(input("\nPlease make a selection: "))
        if user_choice == 1:
            e1.catch_file_not_found()
            input('\n...press enter to continue')
        elif user_choice == 2:
            e1.catch_zero()
            input('\n...press enter to continue')
        elif user_choice == 3:
            e1.catch_import_error()
            input('\n...press enter to continue')
        elif user_choice == 4:
            pass
        else:
            input('\nData invalid, please press enter...')

    return


main()
