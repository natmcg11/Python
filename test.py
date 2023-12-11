int_99 = 99
int_1 = 1
total = 0

def myAdd(int_1, int_99):
    total = int_1 + int_99
    return total

def myPrint():
    print(f"The sum of {int_99} + {int_1} = {myAdd(int_1,int_99)}")
    return

myPrint()
