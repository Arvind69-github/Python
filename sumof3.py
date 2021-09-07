"""Write a Python program to calculate the sum of three given numbers, if the values are equal then return three
times of their sum """
x: int = int(input("enter x value:"))
y: int = int(input("enter y value:"))
z: int = int(input("enter z value:"))
if x == y == z:
    print((x + y + z) * 3)
else:
    print(bool())
