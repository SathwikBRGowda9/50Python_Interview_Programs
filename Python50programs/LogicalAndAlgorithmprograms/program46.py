# 46. Armstrong in Range
low = int(input("Start: "))
high = int(input("End: "))
for num in range(low, high + 1):
    power = len(str(num))
    if num == sum(int(d)**power for d in str(num)):
        print(num, end=" ")
