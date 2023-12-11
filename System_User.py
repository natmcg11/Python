# Nathan McGraw
# Introduction to Programming with Python
# Script 21-File 1

# 1-1)  Create a python file (with header) as System_User.py which will be the Class file for System_User
class System_User:
    # 1-2)  The constructor for System_User takes three (optional) data members (variables) including; user_id = -1,
    # user_name = "default", user_role = "default" (set the string literal "default" as the default value).
    # Parameters with default values are optional. The constructor should update the data members when new data is received.
    def __init__(self, user_id=-1, user_name="default", user_role="default"):
        self.user_id = None
        self.user_name = None
        self.user_role = None
        self.set_user_id(user_id)
        self.set_user_name(user_name)
        self.set_user_role(user_role)
        print("\nDefault System_User Constructor Called")

    # 1-3)  Create getters and setters for each data member
    def set_user_id(self, new_id):
        try:
            cast_int = int(new_id)
            if type(cast_int) == int:
                self.user_id = cast_int
        except TypeError as te:
            print(f'Type Error: "{te}"')
            pass
        except ValueError as ve:
            print(f'Value Error: "{ve}"')
            pass

        return

    def get_user_id(self):
        return self.user_id

    def set_user_name(self, new_name):
        self.user_name = new_name
        return

    def get_user_name(self):
        return self.user_name

    def set_user_role(self, new_role):
        self.user_role = new_role
        return

    def get_user_role(self):
        return self.user_role
    