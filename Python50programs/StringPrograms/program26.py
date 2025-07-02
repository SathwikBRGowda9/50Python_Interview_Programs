# 26. Character Frequency
s = input("Enter string: ")
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
print(freq)
