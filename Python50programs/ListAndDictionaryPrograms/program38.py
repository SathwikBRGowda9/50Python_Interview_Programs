# 38. Common Elements in Lists
l1 = set(map(int, input("List 1: ").split()))
l2 = set(map(int, input("List 2: ").split()))
print("Common:", list(l1 & l2))