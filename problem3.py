#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
a = int(input("Enter an integer "))
b = int(input("Enter an integer "))
c = int(input("Enter an integer "))
if a < c and b < c and a ** 2 + b ** 2 == c ** 2:
    print(str(a) + "," + str(b) + "," + str(c) + " form a Pythagorean triple")
elif a < b and c < b and a ** 2 + c ** 2 == b ** 2:
    print(str(a) + "," + str(c) + "," + str(b) + " form a Pythagorean triple")
elif b < a and c < b and b ** 2 + c ** 2 == a ** 2:
    print(str(a) + "," + str(b) + "," + str(c) + " form a Pythagorean triple")
else:
    print(str(a) + "," + str(b) + "," + str(c) + " do not form a Pythagorean triple")
