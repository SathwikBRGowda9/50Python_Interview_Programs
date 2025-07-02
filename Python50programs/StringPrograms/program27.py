# 27. Pangram Check
s = input("Enter sentence: ").lower()
print("Pangram" if all(chr(c) in s for c in range(97, 123)) else "Not Pangram")
