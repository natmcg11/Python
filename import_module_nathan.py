from System_User import System_User
# Nathan McGraw
# Introduction to Programming with Python
# Script 21-File 2

# 2-1)  Create a properly configured (with headers) python file named: import_module_yourname.py

# 2-2)  At the very top, above the header of this file, use an import statement (do not indent it)
# to access the System_User class found inside the System_User.py class file. (from System_User import System_User)

# 2-3)  Print a greeting in main and offer the user a menu which allows them to interact with the class.


def main():
    print("Welcome to the 'Two-File' Class Lab")

    user_input = 0
    while user_input != 2:
        print("\n\tMain Module Menu:")
        print("\t\t1) Create a New User")
        print("\t\t2) Exit")
        user_input = int(input("\n\tPlease make a selection: "))
# 2-4)  Wrap the Object Creation attempt in a try-catch block to handle any issues that might occur with bad user data.
        if user_input == 1:
            try:
                u_id = int(input("\n\tEnter a user id/number: "))
                u_name = input("\tEnter a user name: ")
                u_role = input("\tEnter a user role: ")
                u1 = System_User(u_id, u_name, u_role)
                print(f"\nSystem_User {u1.get_user_name()} with id {u1.get_user_id()}, has a role of {u1.get_user_role()}.")
            except ValueError as ve:
                print("Improper data entered, please try again.")
    print("\t\tGoodbye.")


# 2-5)  Call the main function or otherwise test the program to handle anticipated user data issues.
main()
