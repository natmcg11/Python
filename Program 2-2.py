# Nathan McGraw
# Introduction to Programming with Python
# Program 2-2: Source Code

""" Code Summary: This program needs to compare a user’s input against a set of requirements
 which meet the User Input Validation Rules listed below. The user will then either receive
 a message saying the combination is valid or be asked to reenter the data correctly. By the
 end the user will have a username/password combination that meets the requirements of the
 business rules. """

''' Change Log: '''
# Corrected variable "username_data" to "user_name" to match functions
# Improved validate_data function by removing nested if loops.


# Compare Inputs Function
def compare_inputs(user_name, pass_word):
    if user_name == pass_word:
        return False
    else:
        return True


# Validation Function
def validate_data(user_data):  # Function by chat.openai.com, via Program 2 Pseudocode.
    # Length requirements
    if len(user_data) < 5 or len(user_data) > 10:
        return False

    # Cannot start with numbers
    if user_data[0].isdigit():
        return False

    # Cannot contain spaces rule
    if ' ' in user_data:
        return False

    return True


# Main function
def main():

    # Welcome message / input rules
    print("\nWelcome,")
    print("\nThis app will help you generate a strong username/password combination.")
    input("\nPress enter to continue...")
    print("\nUsername/Password rules:")
    print("\t* Min 5 characters, max 10.")
    print("\t* Do not use spaces or start with a number.")
    print("\t* Username/Password cannot match.")

    # Prompt user for username and validate
    user_name = input("\nUsername: ")
    while not validate_data(user_name):
        print("Username Invalid. Refer to username/password rules and try again.")
        user_name = input("\nUsername: ")

    # Prompt user for password and validate
    pass_word = input("Password: ")
    while not validate_data(pass_word) or not compare_inputs(user_name, pass_word):
        if not validate_data(pass_word):
            print("Password Invalid. Refer to username/password rules and try again.")
        else:
            print("Username and password cannot be the same. Please try again.")
        pass_word = input("Password: ")

    # Final output
    print("\nYour username/password combination is:")
    print(f"\tUsername: {user_name}")
    print(f"\tPassword: {pass_word}")
    print("\nThank you, have a great day!")
    return


main()
