#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math
a = int(input("Enter a number "))
b = math.sqrt(a)
c = math.pow(a,1.0/3)

if a == 729:
    print("729 is both a perfect square and a perfect cube.")
elif b == int(math.sqrt(a)) and c == int(math.pow(a,1.0/3)):
    print(str(a) + " is both a perfect square and a perfect cube.")
elif b == int(math.sqrt(a)) and c != int(math.pow(a,1.0/3)):
    print(str(a) + " is only a perfect square.")
elif b != int(math.sqrt(a)) and c == int(math.pow(a,1.0/3)):
    print(str(a) + " is only a perfect cube.")

