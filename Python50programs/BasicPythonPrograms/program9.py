# 9. Armstrong Number
n = int(input("Enter number: "))
temp = n
s = 0
while n > 0:
    digit = n % 10
    s += digit ** len(str(temp))
    n //= 10
print("Armstrong" if s == temp else "Not Armstrong")
