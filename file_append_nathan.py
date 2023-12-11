# Nathan McGraw
# Introduction to Programming with Python
# Lab 16: "File IO: File Append and Update"

# (1)Create a properly configured (with headers) python file named: file_append_yourname.py
# (4)Before the main function definition, define the four functions listed below
def line_counter(file_name):
    '''  (5) Function line_counter: takes a single parameter, and returns an integer
    :param file_name
    :return counter '''
    ''' (6) Inside line_counter use the python built-in open() function to
    read the file that created in the previous exercise #14 Use a loop to
     count the total number of lines found in the file, and return the 
    integer value of the counter using the return statement. '''
    counter = 0
    line_counter = open(file_name, 'r')
    for line in line_counter:
        counter += 1
    line_counter.close()
    return counter


def append_file(file_name, counter):
    ''' (7) Function append_file takes both the string for the file name and an integer
     as number of lines, which can be captured as the return value from count_lines(file_name).
    :param file_name, counter '''
    # (8) Inside append_file: Use Python's built in open() function with 'a' mode to write a single line line of text to the file
    file_writer = open(file_name, 'a')
    ''' (9) The file write statement from above should use variable placement(s)
    so the values of the numbers are generated with a value of the variable 
    named counter and counter + 1 passed in as parameters. '''
    file_writer.write(f'\ndata_file.data had {counter} lines of data, and now it has {counter + 1}')
    file_writer.close()
    return


def confirm_append(file_name):
    ''' (10) Function confirm_append: takes the
    string variable name (file_name) and prints
    the contents of the text file to the screen.
    :param file_name '''
    file_reader = open(file_name, 'r')
    print(file_reader.read())
    file_reader.close()
    return


def append_to_ten(file_name):
    ''' (11) Function append_to_ten: takes a string variable (file_name)
    and has no return value. The function append_to_ten is called only
    once in the program, from inside the main function.
     :param file_name'''
    file_line_count = line_counter(file_name)
    ''' (12) Inside append_to_ten use a loop and call other functions until file_name contains the string "data_file.data
    had 9 lines of data, and now it has 10". Once file_name contains that string, call confirm_append to print the
    contents of the file to the screen, and exit the function. '''
    while file_line_count <= 9:
        append_file(file_name, file_line_count)
        file_line_count = line_counter(file_name)
    confirm_append(file_name)
    return


# (2) Create and call a function named main that takes no data and returns no data.
def main():
    print("\nWelcome to the File Append Lab")

    # (3) Inside main create a variable named file_name = "data_file.data", which will act as the name of the file being accessed and manipulated.
    file_name = "data_file.data"

    print("\nData found in data_file.data:")
    append_to_ten(file_name)
    return


# (13)Be sure to call main, which contains the only call to append_to_ten()
main()
