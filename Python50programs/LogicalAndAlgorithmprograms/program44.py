# 44. Prime Numbers in Range
low = int(input("Start: "))
high = int(input("End: "))
for num in range(low, high + 1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
