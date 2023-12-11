# Nathan McGraw
# Introduction to Programming with Python
# Script 10: "Functions as Reusable/Callable Code"

# (1) Create a properly configured (with headers) python file named: functions_yourname.py
# (2) Create and call a function named main that takes no data and returns no data.
# (3) Before the main function definition, define the three functions listed below:
# (4) Code the function test_call that does not take or return any data (still use the return keyword)
def test_call():
    # (5) From inside test_call print a message, for example, "Now inside of test_call."
    print("Now inside of test_call.")
    return


# (7) Code the function test_return that takes an integer, updates it, and returns it to the caller
def test_return(raw_int):
    # (8) From inside test_return print a message, for example, "Found {int}, updating and returning {int + 1}"
    print("Found {}, updating (+1) and returning {}".format(raw_int, raw_int + 1))
    # (9) Also, inside test_return update the value of the integer value += 1
    raw_int += 1
    return raw_int + 1


def empty_or_max(user_data, status):
    # (12) Code the function empty_or_max taking (user_data, status) that returns the value status (possibly updated)
    # (13) Add a definition, you can use the one below, which describes exactly what this function does.
    """empty_or_max takes, user_data:string, status:integer.
    The value of status is 1 or 0. user_data is valid if status = 1.
    If user_data is more than 10 characters in length status = 0
    If user_data = "", status = 0."""
    # (14) Code the function based on the description.
    print("\nCalling empty_or_max(user+data, 1):")
    user_data = input("\tPlease enter character data: ")
    max_len = 10
    if user_data == "" or len(user_data) > max_len:
        status = 0
        validity = "Invalid"
    else:
        status = 1
        validity = "Valid"
    print("\t\tStatus = {}, User Data is {}".format(status, validity))
    return status


def main():
    print('\nWelcome to the main function')
    print("\nCalling test_call()")
    # (6) Call test_call (to this the message) from inside main.
    test_call()
    print("\nCalling test_return(12):")
    # (11)Code a call to test_return that calls, catches and prints the proper values, from inside main.
    test_return(12)
    # (15) In the main function create a dialogue calling empty_or_max and evaluating user data
    empty_or_max("zest", 1)
    print("\nExiting lab...")
    return


main()
