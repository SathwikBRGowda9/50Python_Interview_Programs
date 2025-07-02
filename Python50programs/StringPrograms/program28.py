# 28. Longest Word
words = input("Enter sentence: ").split()
print("Longest word:", max(words, key=len))
