# Nathan McGraw
# Introduction to Programming with Python
# Program 3-2: Class file

class User:
    def __init__(self, user_id=-1, user_name="default", user_role="default"):
        self.user_id = None
        self.user_name = None
        self.user_role = None
        self.set_user_id(user_id)
        self.set_user_name(user_name)
        self.set_user_role(user_role)

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
