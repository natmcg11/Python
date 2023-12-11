# Nathan McGraw
# Introduction to Programming with Python
# Script 23: File 2: New Source Code File

# 2-1)  Create a properly configured (with headers) python file named: object_poly_yourname.py
# 2-2)  Above (at the top of the file) properly include App_User class (the other file)

from App_User import App_User


def object_menu():
    print('\nObject Collection Menu:')
    print('\t1) Create a New Object')
    print('\t2) Print All Objects')
    print('\t3) Print Object (by id)')
    print('\t4) Update Object (by id)')
    print('\t5) Exit')


# 2-3)  Create and call a function named main that takes no data and returns no data.
def main():
    print("\nWelcome to App User")

    # 2-4)  Inside main create a list system_app_users where new App_User objects will be saved to.
    # 2-5)  Establish an integer variable named user_id = 1.
    user_id = 1
    system_app_users = list()
    user_input = 0

    # 2-6)  Code a menu (i.e., loop) which allows a user to add new App_Users to the system_app_user list
    while user_input != 5:
        object_menu()
        user_input = input("\n\tPlease make a selection: ")
        if user_input == '1':
            user_name = input('\n\tEnter a username: ')
            user_role = input("\tEnter user's role: ")
            email_address = input("\tEnter user's email address: ")
            # 2-7)  When calling the App_User constructor give it four pieces of data where name, role,
            # and email address are all collected via input menu prompts.
            new_app_user = App_User(user_id, user_name, user_role, email_address)
            system_app_users.append(new_app_user)
            print(f"\nUser '{user_name}' created successfully!")
            user_id += 1
        elif user_input == '2':
            if len(system_app_users) == 0:
                print("\nNo app users found.")
            else:
                print('\nSystem users report:')
                for user in system_app_users:
                    print(f"\tid: '{user.get_user_id()}', name: '{user.get_user_name()}', role: '{user.get_user_role()}', email: '{user.get_user_email()}', last login: '{user.get_user_login()}'")
        elif user_input == '3':
            if len(system_app_users) == 0:
                print("\nNo app users found.")
            else:
                print('\nPrint User by ID')
                user_id = int(input("\nEnter User ID: "))
                found_user = False
                for user in system_app_users:
                    if user.get_user_id() == user_id:
                        print(f"\nUser report for User ID '{user_id}':")
                        print(f"\n\tid: '{user.get_user_id()}', name: '{user.get_user_name()}', role: '{user.get_user_role()}', email: '{user.get_user_email()}', last login: '{user.get_user_login()}'")
        elif user_input == '4':
            if len(system_app_users) == 0:
                print("\nNo app users found.")
            else:
                print('\nUpdate User by ID')
                user_id = int(input("\nEnter User ID: "))
                found_user = False
                for user in system_app_users:
                    if user.get_user_id() == user_id:
                        user_name = input('\nUpdate username: ')
                        user_role = input("Enter user's role: ")
                        email_address = input("Enter user's email address: ")
                        user.set_user_login()
                        user.set_user_name(user_name)
                        user.set_user_role(user_role)
                        user.set_user_email(email_address)
                        print(f"\n\tid: '{user.get_user_id()}', name: '{user.get_user_name()}', role: '{user.get_user_role()}', email: '{user.get_user_email()}")
                        print(f"\tLast login time for '{user.get_user_name()}' updated: {user.get_user_login()}")
                        break
                    if not found_user:
                        print('\n\tUser not found. ')
        elif user_input == '5':
            exit()

# 2-8)  Run object_poly_yourname.py and create three new objects. Once the objects are created, print the three objects (using the menu) to the screen.
main()
