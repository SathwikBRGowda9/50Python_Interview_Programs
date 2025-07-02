# 39. List is Palindrome
lst = input("Enter list elements: ").split()
print("Palindrome" if lst == lst[::-1] else "Not Palindrome")
