# 48. Perfect Number
n = int(input("Enter number: "))
divisors = [i for i in range(1, n) if n % i == 0]
print("Perfect" if sum(divisors) == n else "Not Perfect")
