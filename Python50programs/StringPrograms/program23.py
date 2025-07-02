# 23. Count Vowels and Consonants
s = input("Enter string: ").lower()
vowels = 'aeiou'
vc, cc = 0, 0
for c in s:
    if c.isalpha():
        vc += c in vowels
        cc += c not in vowels
print(f"Vowels: {vc}, Consonants: {cc}")
