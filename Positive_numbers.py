Que. Write a Python program to print all positive numbers in a range.
INPUT:
# list(list1) of numbers/integers
list1 = [12, -7, 5, 64, -14]
num = 0
 
# For performing looping we use while loop
while(num < len(list1)):
     
    # Checking condition using if statement( if num is greater and equals to zero)
    if list1[num] >= 0:
        print(list1[num], end = " ")
        # Printing positive numbers i.e, zero or greater/no negative numbers

    # increment in num
    num += 1

OUTPUT:
12, 5, 64


INPUT2:
# list(list12) of numbers/integers
list2 = [12, 14, -95, 3]
num = 0
 
# For performing looping we use while loop
while(num < len(list2)):
     
    # Checking condition using if statement( if num is greater and equals to zero)
    if list2[num] >= 0:
        print(list2[num], end = " ")
        # Printing positive numbers i.e, zero or greater/no negative numbers

    # increment in num
    num += 1

OUTPUT2:
12, 14, 3
