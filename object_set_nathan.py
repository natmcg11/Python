# Nathan McGraw
# Introduction to Programming with Python
# Script 22: "Class Object Collections; Array of Objects"

# (1) Create a properly configured (with headers) python file named: object_set_yourname.py
# (2) Above (at the top of the file) properly include System_User class (previous lab)
from System_User import System_User


def main_menu():
    print("\nObject Collection Menu:")
    print("\t1) Create a New Object")
    print("\t2) Print All Objects")
    print("\t3) User Menu")
    print("\t4) Exit")
    return


def user_menu():
    print("\nUser Menu:")
    print("\t1) Print user details")
    print("\t2) Update user name")
    print("\t3) Update user role")
    return


# (3) Create and call a function named main that takes no data and returns no data.
def main():
    # (4) Inside main print a welcome message to the user,
    print("\nWelcome to the Object Collection Lab")

    main_list = list()
    # (5) Establish an integer variable named user_id = 1. When each new System_User object is created, this variable
    # will be passed in as the first data member. Remember to increase by one, this this variable for each new object created.
    user_id = 1
    main_select = 0
    # (6) Code a menu (i.e., loop) and prompt the user for enough data to create at least three objects (pass user_id++)
    # into the constructor, along with the strings returned for prompted data on name and role.
    while main_select != 4:
        main_menu()
        main_select = int(input("\tPlease make a selection: "))
        if main_select == 1:
            new_name = input(f"Enter a new name: ")
            new_role = input(f"Enter a new role: ")
            new_user = System_User(user_id, new_name, new_role)
            user_id = user_id + 1
            # (7) For each object created, append it to a Python list object_list = list()
            main_list.append(new_user)
            pass
        elif main_select == 2:
            for each, user in enumerate(main_list):
                # (8) When the list is populated, neatly print out the data of each object in the list.
                print(f"\nid: {user.get_user_id()}, name: {user.get_user_name()}, role: {user.get_user_role()}")
        elif main_select == 3:
            # (9) Create a menu that allows the user to manage users, including updating names and roles
            user_menu()
            user_select = int(input("\nPlease make a selection: "))
            select_id = int(input("Enter the number of the user to change: "))
            user_exist = False
            array_index = 0
            for each, user in enumerate(main_list):
                if select_id == user.get_user_id():
                    user_exist = True
                    array_index = each
            if user_exist and user_select == 1:
                    print(f"id: {main_list[array_index].get_user_id()}, name: {main_list[array_index].get_user_name()}, role: {main_list[array_index].get_user_role()}")
            elif user_exist and user_select == 2:
                new_name = input(f"Enter a new name: ")
                main_list[array_index].set_user_name(new_name)
            elif user_exist and user_select == 3:
                new_role = input(f"Enter a new role: ")
                main_list[array_index].set_user_role(new_role)
            else:
                print("\nInvalid selection, returning to main menu...")


main()
