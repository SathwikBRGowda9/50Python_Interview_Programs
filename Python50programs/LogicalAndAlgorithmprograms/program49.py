# 49. Strong Number
n = int(input("Enter number: "))
from math import factorial
print("Strong" if sum(factorial(int(d)) for d in str(n)) == n else "Not Strong")
