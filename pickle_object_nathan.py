# Nathan McGraw
# Introduction to Programming with Python
# Script 25: "Object Serialization using Python 'pickle'"

# (1) Create a properly configured (with headers) python file
# (2) At the top of the file add two import statements
from App_User import App_User
import pickle

# (5) Code a menu
def main_menu():
    print("\n\tMain Menu")
    print("\t\t1) Add an App_Users Object to the file")
    print("\t\t2) Read all the App_User data in the file")
    print("\t\t3) Exit")


def read_person(person_file):
    object_list = list()
    with open(person_file, 'rb') as file_data:
        found_data = pickle.load(file_data)
        for each, item in enumerate(found_data):
            print(f"User {item.get_user_name()} found with role {item.get_user_role}:")
            object_list.append(item)
    return object_list


# (3) Create and call a function named main
def main():



main()
