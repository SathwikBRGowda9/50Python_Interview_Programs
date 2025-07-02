# 45. LCM and HCF
import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("HCF:", math.gcd(a, b))
print("LCM:", abs(a*b) // math.gcd(a, b))
