# Nathan McGraw
# Introduction to Programming with Python
# Script 19: "Python Class, Data Members and Methods"

# (1) Create a properly configured (with headers) python file named: class_data_yourname.py
# (3) Above the main function create a python class named User_Data that contains three  data members; user_name (string), user_role(string), user_id(int)
class User_Data:
    # Data members
    user_name = ''
    user_role = ''
    user_id = 0

    # (4) The class constructor, i.e., the __init__() method, should not take any data. Within the constructor print a message 'The User_Data class constructor has been called.'
    def __init__(self):
        print('\nThe User_Data class constructor has been called.')
        return

    # (5) Create a setter method for user_name
    def set_user_name(self, new_name):
        self.user_name = new_name
        return

    # (6) Create a getter method for user_name
    def get_user_name(self):
        return self.user_name

    # (7) Create a setter method for user_role
    def set_user_role(self, this_role):
        self.user_role = this_role
        return

    # (8) Create a getter method for user_role
    def get_user_role(self):
        return self.user_role

    # (9) Create a setter method for user_id
    def set_user_id(self, this_role):
        self.user_id = this_role
        return

    # (10) Create a getter method for user_id
    def get_user_id(self):
        return self.user_id

# (2) Create and call a function named main that takes no data and returns no data.
def main():
    print("\nWelcome to the 'Simple Class File' Lab")

    # (11) Inside main, create a new object of type User_Data.
    ud_1 = User_Data()

    # (12) Call .set_user_name() giving it string data.
    ud_1.set_user_name("meha")

    # (13) Call .get_user_name() to see the result.
    print(ud_1.get_user_name())

    # (14) Call .set_user_role() giving it string data.
    ud_1.set_user_role("admin")

    # (15) Call .get_user_role() to see the result
    print(ud_1.get_user_role())

    # (16) Call .set_user_id() giving it string data.
    ud_1.set_user_id("1")

    # (17) Call .get_user_id() to see the result
    print(ud_1.get_user_id())
    return


main()
