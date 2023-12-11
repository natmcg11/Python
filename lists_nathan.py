# Nathan McGraw
# Introduction to Programming with Python
# Script 12: "Arrays as Mutable Lists and Immutable Tuples"

# (1) Create a properly configured (with headers) python file named: lists_yourname.py
print("\nLab 12: 'Arrays as Mutable Lists and Immutable Tuples'")


# (2) Create and call a function named main that takes no data and returns no data
def main():
    # (3) Inside main, declare binary_numbers and one_to_ten
    binary_numbers = (1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111)
    one_to_ten = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")

    # (4) Print the contents (all the values) of both tuples
    print("\nSimple Array Index")
    print(f"\tThe value of binary_numbers is {binary_numbers}\n\tThe value of one_to_ten is {one_to_ten}")

    # (5) For each tuple, print out the third, fifth, and seventh value(s)
    print(f"\n\tThird Value [index = 2], {binary_numbers[2]}, {one_to_ten[2]}")
    print(f"\tFifth Value [index = 4], {binary_numbers[4]}, {one_to_ten[4]}")
    print(f"\tSeventh Value [index = 6], {binary_numbers[6]}, {one_to_ten[6]}")

    # (6) For each tuple print out the fourth, fifth, sixth, seventh and eighth value(s)
    print(f"\n\tValue at [index = 3], {binary_numbers[3]}, {one_to_ten[3]}")
    print(f"\tValue at [index = 4], {binary_numbers[4]}, {one_to_ten[4]}")
    print(f"\tValue at [index = 5], {binary_numbers[5]}, {one_to_ten[5]}")
    print(f"\tValue at [index = 6], {binary_numbers[6]}, {one_to_ten[6]}")
    print(f"\tValue at [index = 7], {binary_numbers[7]}, {one_to_ten[7]}")

    # (7) For either of the tuples, unpack (and print) the zeroth and last value(s)
    print(f"\n\tThe first value of binary_numbers is {binary_numbers[0]}, the final value is {binary_numbers[7]}")

    ''' (8) Declare a new list one_to_twelve = list() and then use a loop to populate values from zero to ten
    (so there will be eleven values in all) and insert each value into the list, in ascending order. '''
    one_to_twelve = list()
    for each in range(0,11):
        one_to_twelve.append(each)

    # (9) Use the array insert and append syntax to add values for 11 and 12
    one_to_twelve.insert(-1,11)
    one_to_twelve.append(12)

    # (10) Use the array.pop() syntax to remove the value (0) in the zeroth position.
    one_to_twelve.pop(0)

    # (11) Print the values of the list in ascending and descending order.
    # ascending
    print(f"\nValues of one_to_twelve {one_to_twelve}")

    # descending
    one_to_twelve.reverse()
    for each in list(one_to_twelve):
        print(f"\t{each}")


main()

print("\n[Exiting lab...]")
