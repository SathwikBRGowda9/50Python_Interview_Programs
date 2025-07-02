# 42. Linear Search
arr = list(map(int, input("Enter list: ").split()))
x = int(input("Search element: "))
for i in range(len(arr)):
    if arr[i] == x:
        print("Found at index:", i)
        break
else:
    print("Not found")
