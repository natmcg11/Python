# Nathan McGraw
# Introduction to Programming with Python
# Script 15: "File IO: File Create, Write and Close"

# (1) Create a properly configured (with headers) python file named: file_write_yourname.py

# (4) Before the main function definition, define the three functions listed below (5,6,8)
# (5) Create a function named create_file that takes a string variable (for the name of the file), as its only parameter.
def create_file(file_name):
    file_handle = open(file_name, 'x')
    file_handle.close()
    return


# (6) Create a function named write_data that takes a string variable (for the name of the file), as its only parameter.
def write_data(file_name):
    file_writer = open(file_name, 'wt')
    file_writer.write('Steps to file management:'
                      '\n\t1: Create or open a file.'
                      '\n\t2: Write or read data from the file.'
                      '\n\t3: Close the file connection or handle.\n')
    # (7) Once the data (four lines above) are written to the file, close the file handle and exit the function.
    file_writer.close()
    return


# (8) Create a function named print_data that takes a string variable (for the name of the file), as its only parameter.
def print_data(file_name):
    """ (9) Inside the print_data function use python's built-in open() function with the
    'r' mode to loop through the file to read and print any text found in the file to
    the screen. Close the file handle before exiting the function. """
    file_reader = open(file_name, 'r')
    print(file_reader.read())
    file_reader.close()
    return


# (2) Create and call a function named main that takes no data and returns no data.
def main():
    print("\nWelcome to the File I/O Lab\n")

    # (3) Inside the main function create a variable named file_name = "data_file.data", which will act as the name of the file being created.
    file_name = "data_file.data"

# (10) Inside the main function properly call the three functions (described above), passing the value of the file name to each.
# Finally, make sure to call/run the main function.
    create_file(file_name)
    write_data(file_name)
    print_data(file_name)
    return


main()
