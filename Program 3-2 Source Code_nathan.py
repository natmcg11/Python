# Nathan McGraw
# Introduction to Programming with Python
# Program 3-2: Source Code

# Code Summary:
""" This menu-driven program allows the user to manage a collection of objects (users).
 Each user contains a unique username, user id, and role. This program will provide the
 option to create, update and remove any/each user object. """

# # # # # # # #
# Change Log  #
# Removed create_user function
# Refactored update_user_role to update_user, allowing to update more than just the role
# # # # # # # #

from User import User  # import class file
system_users = list()  # list containing users


def main_menu():  # Main user menu
    print("\n\tMain Menu")
    print("\t\t1) View all Users")
    print("\t\t2) Create a New User")
    print("\t\t3) Select/View a User")
    print("\t\t4) Update a User")
    print("\t\t5) Deactivate/Remove a User")
    print("\t\t6) Exit")


def view_all_users():  # Function to see all created users
    if len(system_users) == 0:
        print("\nNo app users found.")
    else:
        print('\nSystem users report:')
        for user in system_users:
            print(f"\tid: '{user.get_user_id()}', name: '{user.get_user_name()}', role: '{user.get_user_role()}'")


def view_user():  # Function to view 1 user by ID
    if len(system_users) == 0:
        print("\nNo users found.")
    else:
        print('\nPrint User by ID')
        try:
            user_id = int(input("\nEnter User ID: "))
        except ValueError as ve:
            print(f"\nValue Error: '{ve}', try again")
            return
        except TypeError as te:
            print(f"\nType Error: '{te}', try again")
            return

        for user in system_users:
            if user.get_user_id() == user_id:
                print(f"\nUser report for User ID '{user_id}':")
                print(f"\n\tid: '{user.get_user_id()}', name: '{user.get_user_name()}', role: '{user.get_user_role()}'")
            else:
                print('\n\tUser not found. ')


def update_user():  # Function to update 1 user's data by ID
    if len(system_users) == 0:
        print("\nNo app users found.")
    else:
        print('\nUpdate User by ID')
        try:
            user_id = int(input("\nEnter User ID: "))
        except ValueError as ve:
            print(f"\nValue Error: '{ve}', try again")
            return
        except TypeError as te:
            print(f"\nType Error: '{te}', try again")
            return
        found_user = False
        for user in system_users:
            if user.get_user_id() == user_id:
                user_name = input('\nUpdate username: ')
                user_role = input("Enter user's role: ")
                user.set_user_name(user_name)
                user.set_user_role(user_role)
                print(f"\n\tid: '{user.get_user_id()}', name: '{user.get_user_name()}', role: '{user.get_user_role()}'")
                break
            if not found_user:
                print('\n\tUser not found. ')
                break


def remove_user():  # Function to remove user from system_users by ID
    if len(system_users) == 0:
        print("\nNo app users found.")
    else:
        print("\nRemove User by ID")
        try:
            user_id = int(input("\nEnter User ID: "))
        except ValueError as ve:
            print(f"\nValue Error: '{ve}', try again")
            return
        except TypeError as te:
            print(f"\nType Error: '{te}', try again")
            return
        for user in system_users:
            if user.get_user_id() == user_id:
                system_users.remove(user)
                print(f"\nUser {user_id} removed")


def save_to_file():  # File storage
    file_path = "system_users.txt"
    with open(file_path, 'wt') as file:
        for user in system_users:
            file.write(f"id: '{user.get_user_id()}', name: '{user.get_user_name()}', role: '{user.get_user_role()}'\n")


def main():  # Main program logic and menu
    user_input = 0
    user_id = 1

    print("\nWelcome to the Admin App!")

    while user_input != '6':
        main_menu()
        user_input = input("\n\tPlease make a selection: ")
        if user_input == '1':
            view_all_users()
        elif user_input == '2':
            user_name = input('\n\tEnter a username: ')
            user_role = input("\tEnter user's role: ")
            new_user = User(user_id, user_name, user_role)
            user_id += 1
            system_users.append(new_user)
            print(f"\nUser '{user_name}' created successfully!")
        elif user_input == '3':
            view_user()
        elif user_input == '4':
            update_user()
        elif user_input == '5':
            remove_user()

    save_to_file()


main()
print("\nThank you for using the Admin App!")
