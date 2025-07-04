# 41. Binary Search
def binary_search(arr, x):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = sorted(list(map(int, input("Enter sorted list: ").split())))
x = int(input("Search element: "))
print("Found at index:" if (i := binary_search(arr, x)) != -1 else "Not found")
