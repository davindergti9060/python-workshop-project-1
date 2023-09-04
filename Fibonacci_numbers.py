Que. Write a Python Program for Fibonacci numbers.
INPUT:
# Accepting number of terms by user as input as nterms
>>> nterms = int(input("Enter number of terms: "))
# First two terms of numbers
>>> n1, n2 = 0, 1
>>> count = 0
""" To check if the number of terms is valid
If the number is equal to 00 it will ask you to enterr a positive number"""
>>> if nterms <= 0:
>>>    print("Enter a positive integer")
# If there is only one term, it will return n1
>>> elif nterms == 1:
>>>   print("Fibonacci sequence upto",nterms,":")
>>>    print(n1)
# Generating fibonacci sequence of numbers
>>> else:
>>>    print("Fibonacci sequence:")
>>>   while count < nterms:
>>>        print(n1)
>>>       nth = n1 + n2
# Updating values to generate series
>>>        n1 = n2
>>>        n2 = nth
>>>        count += 1

OUTPUT:
# try1:
Enter number of terms: 5
Fibonacci sequence:
0
1
1
2
3
# try 2:
Enter number of terms: 8
Fibonacci sequence:
0
1
1
2
3
5
8
13
#try 3:
Enter number of terms: 7
Fibonacci sequence:
0
1
1
2
3
5
8
