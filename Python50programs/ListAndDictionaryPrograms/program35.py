# 35. Count Frequency of List Elements
nums = list(map(int, input("Enter numbers: ").split()))
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1
print(freq)
