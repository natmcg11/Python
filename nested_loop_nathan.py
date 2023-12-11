# Nathan McGraw
# Introduction to Programming with Python
# Script 9: "Outer and Inner Loops (Nested Loops)"

# (1) Create a properly configured (with headers) python file named: nested_loop_yourname.py
print('\nLab #9: "Outer and Inner Loops (Nested Loops)"')

# (2) Create and print these two variables (outer_count = 0, stop_at = 3)
outer_count, stop_at = 1, 4
print("\nNow printing incrementing nested loops")

# (3) Code a for loop that uses the range function
for each in range(1,stop_at):
    # (4) Within the loop, declare the variable (inner_count = 0)
    inner_count = 1
    # (5) Next, also in this loop, nest an additional loop (an inner for loop)
    for each in range(1,stop_at):
        # (6) Finally, inside this inner loop, print out the inner and outer loop counters.
        print("\tOuter Value {}: Inner Value {}".format(outer_count, inner_count))
        inner_count += 1
    print()
    outer_count += 1

# (7) Re-code the loop above, but decrementing the inner and outer loop counters (i.e., 3 to 1)
start_at = 3
outer_counter = 3
print("\nNow printing decrementing nested loops")
for each_outer in range(0, start_at):
    inner_counter = 3
    for each_inner in range(0, start_at):
        print("\tOuter Value {}: Inner Value {}".format(outer_counter, inner_counter))
        inner_counter -= 1
    print()
    outer_counter -= 1
print("Ending lab...")
