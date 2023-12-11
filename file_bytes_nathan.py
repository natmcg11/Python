# Nathan McGraw
# Introduction to Programming with Python
# Lab 17: "File IO: Read, Write Byte-Data

# (1) Create a properly configured (with headers) python file named: file_bytes_yourname.py
# (4) Define the functions write_bytes, print_bytes, print_strings
def write_bytes(file_name, string_data):
    ''' (5) Takes two string variables named file_name
    and string_data, and has no return value. '''
    ''' (6) Inside write_bytes use the 'with' file-handling syntax to open the file
    using 'wb' mode. Transform string_data into byte-data by using the built-in bytes() 
    function and write that byte-data to the file. The 'with' file-handling syntax will auto-close the file handle. '''
    with open(file_name, 'wb') as byte_file:
        byte_file.write(bytes(string_data, encoding='utf8'))
    return


def print_bytes(file_name):
    ''' (7) Function print_bytes takes a single string
     variable named file_name, and has no return value. '''
    # (8) Inside print_bytes use the 'with' file-handling syntax and 'rb' mode to open file_name.
    # Read the byte-data and print it to the screen.
    with open(file_name, 'rb') as byte_handle:
        print(f"\n\tByte data found in byte_file.bytes: [{byte_handle.read()}]")
    return


def print_strings(file_name):
    ''' (9) Function print_strings takes a single string
     variable named file_name, and has no return value. '''
    # (10) Inside print_strings use the 'with' file-handling syntax and 'rb' mode to open file_name.
    # This file contains byte-data, so read out byte-data then decode it using .decode("utf-8"), before printing that string to the screen.
    with open(file_name, 'rb') as string_reader:
        print(f"\n\tString formatted byte_files.bytes: [{string_reader.read().decode('utf8')}]")
    return


# (2) Create and call a function named main that takes no data and returns no data
def main():
    print("\nWelcome to the File Bytes Lab")
    # (3) Create a variable, which will act as the name of the file being accessed and manipulated.
    file_name = "byte_file.bytes"
    ''' (11) Inside the main function prompt the user (using input()) to enter a name or a word.
    Use write_bytes to save that as byte-data to file_name, and then call both print_bytes and
    print_string in order to show the data saved in the file to the user. '''
    byte_data = input("Please enter data for the byte string: ")
    write_bytes(file_name, byte_data)
    print_bytes(file_name)
    print_strings(file_name)
    return

main()
