# Nathan McGraw
# Introduction to Programming with Python
# Script 23: "Polymorphism and Object Inheritance"

from System_User import System_User
from datetime import datetime


# 1-1)  Use Object Inheritance to define App_User as a child class of System_User.py (created in a previous lab).
class App_User(System_User):
        # 1-2)  Add two data members (variables) to the App_User class including email_address as a string and last_login as a python datetime object.
    def __init__(self, user_id, user_name, user_role, email_address):
        # 1-5) Use the constructor to update all the data members for the new App_User object.
        super().__init__(user_id, user_name, user_role)
        self.user_email = email_address
        self.user_login = None
        self.set_user_login()

    # 1-3)  Create getters and setters for each of the data members
    def set_user_email(self, new_email):
        self.user_email = new_email
        return

    def get_user_email(self):
        return self.user_email

    def set_user_login(self):
        # 1-4)  In the set_last_login (setter) query the current 'now' datetime timestamp and save that data using self.last_login
        self.user_login = datetime.now()
        return

    def get_user_login(self):
        return self.user_login
